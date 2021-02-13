# postcodes_api

This is a (very) simple Rest API in python/django to validate the uk postcodes format,
having an understanding of which specific part of the postcode is incorrect.

All validation rules are being made in a separate library: https://github.com/samukasmk/postcodes

## Sample Rest API on PythonAnywhere

You can validate your postcodes on the sample Rest API on PythonAnywhere

Follow a example of validating giants causeway postcode with `requests`:

```
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
pip install requirements.txt
```

## Running

On dev mode

```
python manage.py runserver
```

## Testing

```
python setup.py pytest
```
