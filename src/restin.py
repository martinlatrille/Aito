# -*- coding: utf-8 -*-

# Python import
import re, sys, os, argparse

sys.path.append(os.path.realpath(__file__))

# Local import
import core, settings
from colors import printout

def getTestSets(package):
  """
  Get test sets from files in ./test_sets/
  """
  package_path, package_name = package.rsplit('/', 1)
  sys.path.append(os.path.realpath(package_path))

  try:
    __package__ = __import__(package_name)
  except:
    print 'No such package.'
    sys.exit(1)

  test_sets = []
  for mod_name in dir(__package__):
    __module__ = getattr(__package__, mod_name)
    for class_name in dir(__module__):
      if re.match('Set*', class_name):
        obj = getattr(__module__, class_name)
        test_sets.append(obj())

  return test_sets

def run(args):
  test_sets = getTestSets(args.package)

  if len(test_sets) != 0:
    app = core.App(args.verbosity)

    code = app.process(test_sets)
    sys.exit(code)
  else:
    print printout(settings.strings['errorNoSetFound'], settings.colors['errors'])
    sys.exit(1)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="rip", description="Ultra-lightweight test suite focused on REST API continuous integration.")
  subparsers = parser.add_subparsers(help='run to run the test suite, runserver to run the test server')

  local_parser = subparsers.add_parser('run', help='run the test suite')
  local_parser.add_argument('package', metavar='P', help='the path to the package containing your test sets')
  local_parser.add_argument('-v', '--verbosity', help='the verbosity of the output', type=int)
  local_parser.set_defaults(func=run)

  server_parser = subparsers.add_parser('runserver', help='run the test server')
  server_parser.add_argument('PORT', help='the port on which the server must listens', type=int)

  args = parser.parse_args()
  args.func(args)
