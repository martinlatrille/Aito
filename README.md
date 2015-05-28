# Aito
Ultra-lightweight test suite focused on REST API end-to-end tests.

## Usage
```shell

aito runtest [-h] [-p P] [-v V]
 -h, --help
        show this help message and exit
 -p P, --package P
        the path to the package containing your test sets, default at "./tests"
 -v V, --verbosity V
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

The only dependency of the Aito project is `requests`.

## Doc

### Basic setup
- install Aito in your development environment (`pip install aito`)
- create a `tests` directory which will contain all your tests (`mkdir tests`)
- in this directory, `touch __init__.py`, then create as many tests packages as you want (`mkdir user_case_1 && cd user_case_1 && touch __init__.py`)
- in those directories, or the root tests directory if you didn't create any packages, place your tests files (see below for an example of test file)
- go back to the root of your project, and `aito runtest`
- enjoy

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

* [OK] : response was as expected.
* [KO] : response wasn't as expected.
* [KO] [DIRTY] : your code raised an exception. Correct it and try again.

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

TestSet.expect(self, response, code=None, body=None)
```
