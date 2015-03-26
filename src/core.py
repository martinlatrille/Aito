# -*- coding: utf-8 -*-

# Python imports
import re, requests

# Local imports
import settings
from colors import printout

class TestSet:
  """
  All TestSets must inherit from this class
  """
  def setUp(self):
    """
    Called before the beginning of the test set
    """
    return

  def setDown(self):
    """
    Called after the end of the test set
    """
    return

  def expect(self, response, code=None, body=None):
    """
    Return whether the response corresponds to what is expected or not
    """
    success = True

    if code != None and code != response.status_code:
      success = False

    if body != None and body != response.body:
      success = False

    return {'success': success, 'code': response.status_code, 'elapsed': response.elapsed}

class App:
  """
  Main entry
  """

  def printErrorNoSetFound(self):
    """
    Print 'ErrorNoSetFound' error message
    """
    print printout(settings.strings['errorNoSetFound'], settings.colors['errors'])

  def printIntro(self):
    """
    Print the intro sentence, before testing starts
    """
    print printout(settings.strings['intro'], settings.colors['intro'])

  def printSetIntro(self, u):
    """
    Print the set intro sentence, before the beginning of each test set
    """
    print printout(u.__class__.__name__ + ': ' + u.__doc__, settings.colors['setIntro'])

  def printSetResult(self, test_set, nb_tests, nb_ok, total_response_time):
    """
    Print set results, after the end of each test set
    """
    percent = int(100 * (float(nb_ok) / float(nb_tests)))
    print printout(
      settings.strings['setResult'].format(nb_tests_passed=nb_ok,
                                           nb_tests_total=nb_tests,
                                           percent=percent,
                                           className=test_set.__class__.__name__),
      settings.colors['setResult'])

  def printTotalResult(self, nb_tests, nb_ok, total_response_time):
    """
    Print total results, after the end of all test sets
    """
    percent = int(100 * (float(nb_ok) / float(nb_tests)))
    print printout(
      settings.strings['totalResult'].format(nb_tests_passed=nb_ok,
                                             nb_tests_total=nb_tests,
                                             percent=percent),
      settings.colors['totalResult'])

    if percent == 100:
      print printout(settings.strings['buildOk'], settings.colors['buildOk'])
    else:
      print printout(settings.strings['buildKo'], settings.colors['buildKo'])

  def process(self, test_sets):
    """
    Process testsets
    """
    dataTotal = {}
    dataTotal['index'] = 0
    dataTotal['nb_ok'] = 0

    if len(test_sets) == 0:
      self.printErrorNoSetFound()
      return

    self.printIntro()

    for u in test_sets:

      self.printSetIntro(u)

      dataTestSet = {}
      dataTestSet['index'] = 0
      dataTestSet['nb_ok'] = 0

      for f in dir(u):
        if re.match('test_*', f):
          dataTestSet['index'] += 1
          func = getattr(u, f)
          func_doc = func.__doc__.strip('\n')

          try:
            dataTest = func()

            if dataTest['success']:
              success = printout(settings.strings['testSuccess'], settings.colors['testSuccess'])
              dataTestSet['nb_ok'] += 1
            else:
              success = printout(settings.strings['testFailure'], settings.colors['testFailure'])

            output = settings.strings['testOutputFormat'].format(success=success, return_code=dataTest['code'], elapsed=dataTest['elapsed'], doc=func_doc)

          except Exception as e:
            output = printout(settings.strings['testDirtyFailure'], settings.colors['testDirtyFailure']) + func_doc + str(e)

          print output

      dataTotal['index'] += dataTestSet['index']
      dataTotal['nb_ok'] += dataTestSet['nb_ok']
      self.printSetResult(u, dataTestSet['index'], dataTestSet['nb_ok'], 0)

    self.printTotalResult(dataTotal['index'], dataTotal['nb_ok'], 0)
