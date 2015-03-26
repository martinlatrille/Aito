# -*- coding: utf-8 -*-

import core
import requests

class Set1(core.TestSet):
  """
  Martin wants to ping google.com
  """

  def testPingGoogle(self):
    """
    He pings google.com
    """
    response = requests.get('http://google.com/')
    return self.expect(response, code=200)

class Set2(core.TestSet):
  """
  Martin wants to ping facebook.com
  """

  def testPongGoogle(self):
    """
    He pings facebook.com
    """
    response = requests.get('http://facebook.com/')
    return self.expect(response, code=200)
