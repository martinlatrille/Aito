# -*- coding: utf-8 -*-

# Python imports
import re, requests

# Local imports
import settings
import printers

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
      #print body

    return {'success': success, 'code': response.status_code, 'elapsed': response.elapsed}

class App:
  """
  Main entry
  """
  def __init__(self, printer):
    self.printer = printer

  def process(self, modules):
    """
    Process modules
    """
    data_total = {}
    data_total['index'] = 0
    data_total['nb_ok'] = 0

    if len(modules) == 0:
      self.printer.printErrorNoSetFound()
      return

    self.printer.printIntro()

    for test_set in modules:

      self.printer.printSetIntro(test_set)

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
              data_test_set['nb_ok'] += 1


            self.printer.printTestOutput(data_test, func_doc)
          except Exception as e:
            self.printer.printTestDirtyFailure({'success': False, 'exception': e})


      test_set.setDown()

      data_total['index'] += data_test_set['index']
      data_total['nb_ok'] += data_test_set['nb_ok']
      self.printer.printSetResult(test_set, data_test_set['index'], data_test_set['nb_ok'], 0)


    self.printer.printTotalResult(data_total['index'], data_total['nb_ok'], 0)
    return 0 if data_total['index'] == data_total['nb_ok'] else 1
