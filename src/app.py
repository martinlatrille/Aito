# -*- coding: utf-8 -*-

# Python import
import re, sys, os

sys.path.append(os.path.realpath(__file__))

import uc.usecase1

# Local import
import core, settings

def getUseCases():
  test_sets = []

  for mod_name in settings.sets:
    __mod__ = __import__(mod_name)
    for class_name in dir(__mod__):
      if re.match('UseCase*', class_name):
        obj = getattr(__mod__, class_name)
        test_sets.append(obj())

  return test_sets

if __name__ == "__main__":
  useCases = getUseCases()
  app = core.App()
  app.process(useCases)
