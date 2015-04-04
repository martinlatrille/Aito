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
  _base_url = ""

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

  def get(self, end_url, **kwargs):
    url = self._base_url + end_url
    return requests.get(url, **kwargs)

  def post(self, end_url, data=None, json=None, **kwargs):
    url = self._base_url + end_url
    return requests.post(url, data, json, **kwargs)

  def put(self, end_url, data=None, **kwargs):
    url = self._base_url + end_url
    return requests.put(url, data, **kwargs)

  def patch(self, end_url, data=None, **kwargs):
    url = self._base_url + end_url
    return requests.patch(url, data, **kwargs)

  def delete(self, end_url, **kwargs):
    url = self._base_url + end_url
    return requests.delete(url, **kwargs)

  def expect(self, response, code=None, body=None):
    """
    Return whether the response corresponds to what is expected or not
    """
    success = True

    if code != None and code != response.status_code:
      success = False

    if body != None and body != response.body:
      success = False
      print body

    return {'success': success, 'code': response.status_code, 'elapsed': response.elapsed}

class App:
  """
  Main entry
  """
  def __init__(self, verbosity):
    self.verbosity = verbosity

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
    if self.verbosity > 0:
      print printout(u.__class__.__name__ + ': ' + u.__doc__, settings.colors['setIntro'])

  def printTestOutput(self, output):
    """
    Print the output of a test
    """
    if self.verbosity > 1:
      print output

  def printSetResult(self, test_set, nb_tests, nb_ok, total_response_time):
    """
    Print set results, after the end of each test set
    """
    if self.verbosity > 0:
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

  def process(self, modules):
    """
    Process modules
    """
    data_total = {}
    data_total['index'] = 0
    data_total['nb_ok'] = 0

    if len(modules) == 0:
      self.printErrorNoSetFound()
      return

    self.printIntro()

    for test_set in modules:

      self.printSetIntro(test_set)

      data_test_set = {}
      data_test_set['index'] = 0
      data_test_set['nb_ok'] = 0

      test_set.setUp()

      for f in dir(test_set):
        if re.match('test_*', f):
          data_test_set['index'] += 1
          func = getattr(test_set, f)
          func_doc = func.__doc__.strip('\n')

          try:
            data_test = func()

            if data_test['success']:
              success = printout(settings.strings['testSuccess'], settings.colors['testSuccess'])
              data_test_set['nb_ok'] += 1
            else:
              success = printout(settings.strings['testFailure'], settings.colors['testFailure'])

            output = settings.strings['testOutputFormat'].format(success=success, return_code=data_test['code'], elapsed=data_test['elapsed'], doc=func_doc)

          except Exception as e:
            output = printout(settings.strings['testDirtyFailure'], settings.colors['testDirtyFailure']) + func_doc + str(e)

          self.printTestOutput(output)

      test_set.setDown()

      data_total['index'] += data_test_set['index']
      data_total['nb_ok'] += data_test_set['nb_ok']
      self.printSetResult(test_set, data_test_set['index'], data_test_set['nb_ok'], 0)


    self.printTotalResult(data_total['index'], data_total['nb_ok'], 0)
    return 0 if data_total['index'] == data_total['nb_ok'] else 1
