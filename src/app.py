# -*- coding: utf-8 -*-

# Python import
import re, sys, os

sys.path.append(os.path.realpath(__file__))

# Local import
import core, settings
from colors import printout

def getTestSets():
  """
  Get test sets from files in ./test_sets/
  """
  test_sets = []
  __package__ = __import__('test_sets', level=0)

  for mod_name in dir(__package__):
    __module__ = getattr(__package__, mod_name)
    for class_name in dir(__module__):
      if re.match('Set*', class_name):
        obj = getattr(__module__, class_name)
        test_sets.append(obj())

  return test_sets

if __name__ == "__main__":
  test_sets = getTestSets()

  if len(test_sets) != 0:
    app = core.App()
    app.process(test_sets)
  else:
    print printout(settings.strings['errorNoSetFound'], settings.colors['errors'])
