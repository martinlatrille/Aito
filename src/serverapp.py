# -*- coding: utf-8 -*-

# Tornado imports
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import sys

# Local imports
import server.handlers

sys.path.append("/home/sealk/projs/RESTinPY/src/")

class TestServer:
  """
  Server to trigger and receive test session results
  """

  def __init__(self):
    self.settings = {
      "cookie_secret": "restincookies",
      "login_url": "/login",
      "template_path": "templates",
      "debug": True,
    }

    self.handlers = [
      # Regular Handlers
      (r'/', server.handlers.IndexPageHandler),
      (r'/version', server.handlers.VersionHandler),
      # Websocket Handlers
      #(r'/ws', server.handlers.WaveFlowHandler),
    ]

  def run(self, port):
    app = tornado.web.Application(self.handlers, **self.settings)
    server = tornado.httpserver.HTTPServer(app)
    server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
