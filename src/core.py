# -*- coding: utf-8 -*-

# Python imports
import re, requests

# Local imports
import settings
from colors import printout

class UseCase:
  """
  All UseCases must inherit from this class
  """
  def setUp(self):
    return

  def setDown(self):
    return

  def expect(self, response, code=None, body=None):
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
    print printout(settings.strings['errorNoSetFound'], settings.colors['errors'])

  def printIntro(self):
    print printout(settings.strings['intro'], settings.colors['intro'])

  def printSetIntro(self, u):
    print printout(u.__class__.__name__ + ': ' + u.__doc__, settings.colors['setIntro'])

  def printSetResult(self, use_case, nb_tests, nb_ok, total_response_time):
    percent = int(100 * (float(nb_ok) / float(nb_tests)))
    print printout(
      settings.strings['setResult'].format(nb_tests_passed=nb_ok,
                                           nb_tests_total=nb_tests,
                                           percent=percent,
                                           className=use_case.__class__.__name__),
      settings.colors['setResult'])

  def printTotalResult(self, nb_tests, nb_ok, total_response_time):
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

  def process(self, useCases):
    """
    Process UseCases
    """
    dataTotal = {}
    dataTotal['index'] = 0
    dataTotal['nb_ok'] = 0

    if len(useCases) == 0:
      self.printErrorNoSetFound()
      return

    self.printIntro()

    for u in useCases:

      self.printSetIntro(u)

      dataUseCase = {}
      dataUseCase['index'] = 0
      dataUseCase['nb_ok'] = 0

      for f in dir(u):
        if re.match('test_*', f):
          dataUseCase['index'] += 1
          func = getattr(u, f)
          func_doc = func.__doc__.strip('\n')

          try:
            dataTest = func()

            if dataTest['success']:
              success = printout(settings.strings['testSuccess'], settings.colors['testSuccess'])
              dataUseCase['nb_ok'] += 1
            else:
              success = printout(settings.strings['testFailure'], settings.colors['testFailure'])

            output = settings.strings['testOutputFormat'].format(success=success, return_code=dataTest['code'], elapsed=dataTest['elapsed'], doc=func_doc)

          except Exception as e:
            output = printout(settings.strings['testDirtyFailure'], settings.colors['testDirtyFailure']) + func_doc + str(e)

          print output

      dataTotal['index'] += dataUseCase['index']
      dataTotal['nb_ok'] += dataUseCase['nb_ok']
      self.printSetResult(u, dataUseCase['index'], dataUseCase['nb_ok'], 0)

    self.printTotalResult(dataTotal['index'], dataTotal['nb_ok'], 0)
