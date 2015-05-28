#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python import
import re, sys, os, argparse

sys.path.append(os.path.dirname(os.path.realpath('.')))

# Local import
from libaito import core, settings, printers
from libaito.helpers import getTestSets

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
  parser = argparse.ArgumentParser(prog="aito", description="Aito // Ultra-lightweight test suite focused on REST API end-to-end tests.")
  subparsers = parser.add_subparsers()

  local_parser = subparsers.add_parser('runtest', help='run the test suite')
  local_parser.add_argument('-p', '--package', metavar='P', help='the path to the package containing your test sets, default at "./tests"', default='tests')
  local_parser.add_argument('-v', '--verbosity', metavar='V', help='set the verbosity of the output : 0, 1 or 2 (default)', type=int, default=2)
  local_parser.set_defaults(func=run)

  args = parser.parse_args()
  args.func(args)
