# -*- coding: utf-8 -*-

import core
import requests

class Set1(core.TestSet):
  """
  Martin wants to ping http://www.google.com
  """

  def setUp(self):
    self._base_url = 'http://www.google.com'

  def testPingGoogleHome(self):
    """
    He pings http://www.google.com
    """
    response = self.get('/')
    return self.expect(response, code=200)

  def testPingGoogleImage(self):
    """
    He pings https://www.google.com/imghp
    """
    response = self.get('/imghp')
    return self.expect(response, code=200)

  def testPingGoogleNotFound(self):
    """
    He pings https://www.google.com/imghpqsd
    """
    response = self.get('/imghpqsd')
    return self.expect(response, code=200)

  def testPingGoogleHome2(self):
    """
    He pings http://www.google.com
    """
    response = self.get('/')
    return self.expect(response, code=200)

class Set2(core.TestSet):
  """
  Martin wants to ping stackoverflow.com
  """
  _base_url = 'http://stackoverflow.com'

  def testPingStackOvHome(self):
    """
    He pings stackoverflow.com
    """
    response = self.get('/')
    return self.expect(response, code=200)


  def testPingStackOvHome2(self):
    """
    He pings stackoverflow.com
    """
    response = self.get('/')
    return self.expect(response, code=200)


  def testPingStackOvHome3(self):
    """
    He pings stackoverflow.com
    """
    response = self.get('/')
    return self.expect(response, code=200)
