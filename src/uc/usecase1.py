# -*- coding: utf-8 -*-

import core
import requests

class UseCase1(core.UseCase):
  """
  Martin wants to register to letsbro
  """

  def test_1(self):
    """
    He tries something
    """
    response = requests.get('http://google.com/')
    return self.expect(response, code=200)

class UseCase5(core.UseCase):
  """
  Martin wants to register to letsbro
  """

  def test_1(self):
    """
    He tries something
    """
    response = requests.get('http://google.com/')
    return self.expect(response, code=200)
