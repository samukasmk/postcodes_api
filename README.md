# postcodes_api

This is a (very) simple Rest API in python/django to validate the uk postcodes format,
having an understanding of which specific part of the postcode is incorrect.

All validation rules are being made in a separate library: https://github.com/samukasmk/postcodes

## Sample Rest API on PythonAnywhere

You can validate your postcodes on the sample Rest API on PythonAnywhere

Follow a example of validating giants causeway postcode with `requests`:

```python
>>> import requests
>>> response = requests.get('http://samukasmk.pythonanywhere.com/api/postcodes/uk/',
                            params={'postcode': 'BT57 8SU'})

>>> response.json()
{'postcode': 'BT57 8SU',
 'is_valid': True,
 'attributes': {'area': 'BT', 'district': '57', 'sector': '8', 'unit': 'SU'},
 'sides': {'outward': 'BT57', 'inward': '8SU'},
 'errors': {}}
```

## Installing

On your local machine (virtualenv)

```
$ pip install requirements.txt
```

## Running

On dev mode

```
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 13, 2021 - 07:34:26
Django version 3.1.6, using settings 'core.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Testing

```
$ python setup.py pytest
WARNING: The wheel package is not available.
running pytest
running egg_info
writing postcodes_api.egg-info/PKG-INFO
writing dependency_links to postcodes_api.egg-info/dependency_links.txt
writing requirements to postcodes_api.egg-info/requires.txt
writing top-level names to postcodes_api.egg-info/top_level.txt
reading manifest file 'postcodes_api.egg-info/SOURCES.txt'
writing manifest file 'postcodes_api.egg-info/SOURCES.txt'
running build_ext
============================================ test session starts ============================================
platform linux -- Python 3.9.1, pytest-6.2.2, py-1.10.0, pluggy-0.13.1 -- /home/smk/.pyenv/versions/postcodes_api/bin/python
cachedir: .pytest_cache
django: settings: core.settings (from ini)
rootdir: /home/smk/Projects/postcodes_api, configfile: pyproject.toml, testpaths: tests
plugins: django-4.1.0, cov-2.11.1, flakes-4.0.3
collected 44 items                                                                                          

tests/__init__.py::flake-8 PASSED
tests/settings.py::flake-8 PASSED
tests/test_api_postcodes_uk.py::flake-8 PASSED
tests/test_api_postcodes_uk.py::test_api_valid_postcodes_uk[AA9A 9AA] PASSED
tests/test_api_postcodes_uk.py::test_api_valid_postcodes_uk[A9A 9AA] PASSED
tests/test_api_postcodes_uk.py::test_api_valid_postcodes_uk[A9 9AA] PASSED
tests/test_api_postcodes_uk.py::test_api_valid_postcodes_uk[A99 9AA] PASSED
tests/test_api_postcodes_uk.py::test_api_valid_postcodes_uk[AA9 9AA] PASSED
tests/test_api_postcodes_uk.py::test_api_valid_postcodes_uk[AA99 9AA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_area[9 9AA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_area[9A 9AA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_area[99 9AA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_area[AAA9A 9AA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_area[AAAA9A 9AA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_area[AAAAA9A 9AA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_area[AAA99 9AA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_area[AAAA99 9AA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_area[AAAAA99 9AA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_district[A 9AA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_district[AA 9AA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_sector[AA9A AA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_sector[A9A AA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_sector[A9 AA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_sector[A99 AA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_sector[AA9 AA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_sector[AA99 AA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_unit[AA9A 9] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_unit[A9A 9] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_unit[A9 9] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_unit[A99 9] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_unit[AA9 9] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_unit[AA99 9] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_unit[AA9A 9AAA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_unit[A9A 9AAA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_unit[A9 9AAA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_unit[A99 9AAA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_unit[AA9 9AAA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_unit[AA99 9AAA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_unit[AA9A 9AAAA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_unit[A9A 9AAAA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_unit[A9 9AAAA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_unit[A99 9AAAA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_unit[AA9 9AAAA] PASSED
tests/test_api_postcodes_uk.py::test_api_postcodes_uk_invalid_unit[AA99 9AAAA] PASSED

----------- coverage: platform linux, python 3.9.1-final-0 -----------
Name                                                                                     Stmts   Miss  Cover
------------------------------------------------------------------------------------------------------------
/home/smk/.pyenv/versions/3.9.1/envs/postcodes_api/src/postcodes/postcodes/__init__.py       4      0   100%
/home/smk/.pyenv/versions/3.9.1/envs/postcodes_api/src/postcodes/postcodes/uk.py           103      4    96%
------------------------------------------------------------------------------------------------------------
TOTAL                                                                                      107      4    96%


============================================ 44 passed in 0.52s =============================================
```
