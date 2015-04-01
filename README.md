# RESTinPy
Extensible library to test REST APIs in Python

[DIRTY] : means that your code raised an exception. Correct it and try again.

## Two lines test

It's that simple :

    def testPingGoogleHome(self):
      """
      He pings http://google.com
      """
      response = self.get('/')
      return self.expect(response, code=200)

Returns :

    [OK] [code : 200] [0:00:00.076603ms]    He pings http://google.com
