# RESTinPy
Ultra-lightweight test suite focused on REST API continuous integration.

## Usage
```shell
restin.py [-h] [-p PACKAGE] [-v VERBOSITY]
 -p PACKAGE / --package PACKAGE
        the name of the package containing the modules to process
 -v VERBOSITY / --verbosity VERBOSITY
        the desired output verbosity (0, 1 or 2)
```

## Test a webservice in two lines

It's that simple :

```python
def testPingGoogleHome(self):
  """
  He pings http://google.com
  """
  response = self.get('/')
  return self.expect(response, code=200)
```

Returns :

```shell
[OK] [code : 200] [0:00:00.076603ms]    He pings http://google.com
```

## One dependency

The only dependency of the RESTinPy project is `requests`.

## Doc

### Sample test set

```python
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

  def setDown(self):
    print 'Goodbye testitest :('
```

### Output signification

[OK] : response was as expected.
[KO] : response wasn't as expected.
[KO] [DIRTY] : your code raised an exception. Correct it and try again.

### TestSet.* prototypes

```python
# Overridable
TestSet.setUp(self)
TestSet.setDown(self)

# Usable
TestSet.get(self, end_url, **kwargs)
TestSet.post(self, end_url, data=None, json=None, **kwargs)
TestSet.put(self, end_url, data=None, **kwargs)
TestSet.patch(self, end_url, data=None, **kwargs)
TestSet.delete(self, end_url, **kwargs)
```
