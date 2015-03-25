#!/usr/bin/python
#coding: utf-8

import re, requests
from colors import *

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
useCases = []
          
class UseCase:
  """
  Abstract parent class of all use cases
  """
  def __init__(self):
    useCases.append(self)
  
  def __str__(self):
    return "AbstractUseCase"
  
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
      

class UseCase1(UseCase):
  """
  Martin wants to register to letsbro
  """
  
  def test_1(self):
    """
    He tries something
    """
    response = requests.get('http://google.com/')
    return self.expect(response, code=200)
  
class UseCase5(UseCase):
  """
  Martin wants to register to letsbro
  """
  
  def test_1(self):
    """
    He tries something
    """
    response = requests.get('http://google.com/')
    return self.expect(response, code=200)
  
class App:
  """
  Main entry
  """
  def printSetResult(self, use_case, nb_tests, nb_ok, total_response_time):
    percent = int(100 * (float(nb_ok) / float(nb_tests)))
    print printout("Total for {3} : {0} / {1} successful tests ({2}%)\n---\n".format(nb_ok, nb_tests, percent, use_case.__class__.__name__), CYAN)
    
  def printTotalResult(self, nb_tests, nb_ok, total_response_time):
    percent = int(100 * (float(nb_ok) / float(nb_tests)))
    print printout("Total : {0} / {1} successful tests ({2}%)".format(nb_ok, nb_tests, percent), MAGENTA)
    
    if percent == 100:
      print printout('\n\n  [BUILD: OK]\n\n', GREEN)
    else:
      print printout('\n\n  [BUILD: KO]\n\n', RED)
    
  def process(self, useCases):
    """
    Process UseCases
    """
    dataTotal = {}
    dataTotal['index'] = 0
    dataTotal['nb_ok'] = 0
    
    print printout('---\n', CYAN)
    
    for u in useCases:
      
      print printout(u.__class__.__name__ + ': ' + u.__doc__, CYAN)
      
      dataUseCase = {}
      dataUseCase['index'] = 0
      dataUseCase['nb_ok'] = 0
      
      for f in dir(u):
        if re.match('test_*', f):
          dataUseCase['index'] += 1
          func = getattr(u, f)
          to_print = func.__doc__.strip('\n')
          
          try:
            dataTest = func()
            
            if dataTest['success']:
              success = printout('[OK]', GREEN)
              dataUseCase['nb_ok'] += 1
            else:
              success = printout('[KO]', RED)
              
            to_print = success + ' [code: ' + str(dataTest['code']) + '] [' + str(dataTest['elapsed']) + 'ms] ' + to_print
            
          except Exception as e:
            to_print = printout('[KO] [DIRTY]', RED) + to_print + str(e)
            
          print to_print
        
      dataTotal['index'] += dataUseCase['index']
      dataTotal['nb_ok'] += dataUseCase['nb_ok']
      self.printSetResult(u, dataUseCase['index'], dataUseCase['nb_ok'], 0)
    self.printTotalResult(dataTotal['index'], dataTotal['nb_ok'], 0)
      
if __name__ == "__main__":
  app = App()
  UseCase1()
  UseCase5()
  app.process(useCases)