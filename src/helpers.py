# -*- coding: utf-8 -*-
import re, sys, os

def getTestSets(package):
  """
  Get test sets from files in ./test_sets/
  """
  if '/' in package:
    package_path, package_name = package.rsplit('/', 1)
  else:
    package_path = '.'
    package_name = package
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
