
# Passmarked Python Wrapper


This is a Python wrapper to use the [Passmarked](https://passmarked.com) API in your Python applications. Please note that this wrapper does not include any cli options, if required you can use the Node.js CLI/Module/Framework for the  [Passmarked](https://github.com/passmarked/passmarked) API.

## Install

A PIP package might be available in the future but for now it can be installed via the source/setup tools.

### Setup Tools From Source Installation
```bash
git clone git@github.com:passmarked/python.git passmarked-python
cd passmarked-python/
python setup.py install
```

## Usage
The returned values are by default a python dictionary with ```get()``` method.
This can be changed to JSON by calling ```get_json()``` instead. A specific key
inside collection can also be retrieved by adding the keyname as parameter. eg. ```get('key')```

# Config
```python
from passmarked.api import API

# Python dictionary with config options is required to be passed in as main constructor parameter.
# Its a good idea to retrieve these values from a separate file or env variables.
config = {'token': 'Your token here',
          'appname': 'Your application name',
          'device': 'terminal/library etc',
          'version': '2'} # Api version is 2 by default

passmarked = API(config)
```

### Create
```python
result = passmarked.create('http://example-website.com').get()
```

### Websites
```python
# Retrieve all websites
result = passmarked.websites().get()
# Retrieve all websites in JSON format
result = passmarked.websites().get_json()

# If more than one website ```at()``` can be used.
result = passmarked.websites().at(1).get()
```

### Website
```python
# Retrieve website with key
result = passmarked.website(key).get()
# Retrieve website with key in JSON format
result = passmarked.website(key).get_json()
```

### Report
```python
# Retrieve report with website uid.
result = passmarked.get(uid).get()
# Retrieve specific key in report with website uid.
result = passmarked.get(uid).get('crawled')
# Retrieve report with website uid in JSON format.
result = passmarked.get(uid).get_json()
```

### User Profile
```python
# Retrieve user profile
result = passmarked.user().get()
# Retrieve user profile in JSON format.
result = passmarked.user().get_json()
```

### Balance
```python
# Retrieve current balance
result = passmarked.balance().get()
# Retrieve current balance in JSON format
result = passmarked.balance().get_json()
```

### Credits
```python
# Retrieve credits/plans
result = passmarked.credits().get()
# Retrieve credits/plans in JSON format
result = passmarked.credits().get_json()
```

### Reports
```python
# Retrieve reports
result = passmarked.submit('http://example-website.com').get()
# Retrieve reports in JSON format
result = passmarked.submit('http://example-website.com').get_json()
```


## Main API Reference

* [Authentication](https://github.com/passmarked/passmarked/wiki/authentication)
* [create](https://github.com/passmarked/passmarked/wiki/create)
* [getReport](https://github.com/passmarked/passmarked/wiki/report)
* [getWebsites](https://github.com/passmarked/passmarked/wiki/websites)
* [getProfile](https://github.com/passmarked/passmarked/wiki/profile)
* [getBalance](https://github.com/passmarked/passmarked/wiki/balance)
* [createRunner](https://github.com/passmarked/passmarked/wiki/runner)

## Contributing
1. Fork the project
2. Write a test that reproduces the bug
3. Fix the bug without breaking any of the existing tests
4. Submit a pull request

We're busy building the tests and refactoring code as we go. If you spot any area that could use help feel free to open a PR.

## License

Copyright 2016 Passmarked Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
