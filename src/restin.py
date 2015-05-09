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

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Ultra-lightweight test suite focused on REST API continuous integration.")
  parser.add_argument('-p', '--package', help='the package containing your test sets')
  parser.add_argument('-v', '--verbosity', help='the verbosity of the output', type=int)
  args = parser.parse_args()

  if args.package:
    test_sets = getTestSets(args.package)
  else:
    print printout(settings.strings['errorNoSetFound'], settings.colors['errors'])
    sys.exit(1)

  if len(test_sets) != 0:
    app = core.App(args.verbosity)

    code = app.process(test_sets)
    sys.exit(code)
  else:
    print printout(settings.strings['errorNoSetFound'], settings.colors['errors'])
    sys.exit(1)
