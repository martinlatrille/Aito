# -*- coding: utf-8 -*-

# Python import
import re, sys, os, argparse

sys.path.append(os.path.realpath(__file__))

# Local import
import core, settings
import printers
from helpers import getTestSets

def run(args):
  """
  Run the test suite
  """
  test_sets = getTestSets(args.package)
  printer = printers.LocalPrinter(args.verbosity)

  if len(test_sets) != 0:
    app = core.App(printer)

    code = app.process(test_sets)
    sys.exit(code)
  else:
    printer.printErrorNoSetFound()
    sys.exit(1)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="rip", description="RESTinPy: ultra-lightweight test suite focused on REST API continuous integration.")
  subparsers = parser.add_subparsers()

  local_parser = subparsers.add_parser('run', help='run the test suite')
  local_parser.add_argument('package', metavar='P', help='the path to the package containing your test sets')
  local_parser.add_argument('-v', '--verbosity', metavar='V', help='set the verbosity of the output : 0, 1 or 2 (default)', type=int, default=2)
  local_parser.set_defaults(func=run)

  args = parser.parse_args()
  args.func(args)
