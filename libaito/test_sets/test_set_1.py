# -*- coding: utf-8 -*-

from core import TestSet

class SetDoesGoogleWork(TestSet):
  """
  Martin wants to ping http://google.com
  """

  def setUp(self):
    self._base_url = 'http://google.com'

  def testPingGoogleHome(self):
    """
    He pings http://google.com
    """
    response = self.get('/')
    return self.expect(response, code=200)

  def testPingGoogleImage(self):
    """
    He pings http://google.com/imghp
    """
    response = self.get('/imghp')
    return self.expect(response, code=200)

  def testPingGoogleNotFound(self):
    """
    He pings http://google.com/imghpqsd
    """
    response = self.get('/imghpqsd')
    return self.expect(response, code=200)

  def testPingGoogleHome2(self):
    """
    He pings http://google.com
    """
    response = self.get('/')
    return self.expect(response, code=200)

class SetDoesStackOverflowWork(TestSet):
  """
  Martin wants to ping http://stackoverflow.com
  """
  _base_url = 'http://stackoverflow.com'

  def testPingStackOvHome(self):
    """
    He pings http://stackoverflow.com
    """
    response = self.get('/')
    return self.expect(response, code=200)


  def testPingStackOvHome2(self):
    """
    He pings http://stackoverflow.com
    """
    response = self.get('/')
    return self.expect(response, code=200)


  def testPingStackOvHome3(self):
    """
    He pings http://stackoverflow.com
    """
    response = self.get('/')
    return self.expect(response, code=200)
