# -*- coding: utf-8 -*-

import core
import requests

class Set1(core.TestSet):
  """
  Martin wants to register to letsbro
  """

  def testPingGoogle(self):
    """
    He tries something
    """
    response = requests.get('http://google.com/')
    return self.expect(response, code=200)

class Set2(core.TestSet):
  """
  Martin wants to register to letsbro
  """

  def testPongGoogle(self):
    """
    He tries something
    """
    response = requests.get('http://google.com/')
    return self.expect(response, code=200)
