import pytest
from rest_framework.test import APIClient


@pytest.mark.parametrize('raw_postcode', ['AA9A 9AA', 'A9A 9AA', 'A9 9AA', 'A99 9AA', 'AA9 9AA', 'AA99 9AA'])
def test_api_valid_postcodes_uk(raw_postcode):
    client = APIClient()
    response = client.get('/api/postcodes/uk/', {'postcode': raw_postcode})
    assert response.status_code == 200
    assert response.data['is_valid'] is True
    assert len(response.data['errors']) == 0


@pytest.mark.parametrize('raw_postcode', ['9 9AA', '9A 9AA', '99 9AA',
                                          'AAA9A 9AA', 'AAAA9A 9AA', 'AAAAA9A 9AA',
                                          'AAA99 9AA', 'AAAA99 9AA', 'AAAAA99 9AA'])
def test_api_postcodes_uk_invalid_area(raw_postcode):
    client = APIClient()
    response = client.get('/api/postcodes/uk/', {'postcode': raw_postcode})
    assert response.status_code == 400
    assert response.data['is_valid'] is False
    assert 'area' in response.data['errors'].keys()
    assert len(response.data['errors']) == 1


@pytest.mark.parametrize('raw_postcode', ['A 9AA', 'AA 9AA'])
def test_api_postcodes_uk_invalid_district(raw_postcode):
    client = APIClient()
    response = client.get('/api/postcodes/uk/', {'postcode': raw_postcode})
    assert response.status_code == 400
    assert response.data['is_valid'] is False
    assert 'district' in response.data['errors'].keys()
    assert len(response.data['errors']) == 1


@pytest.mark.parametrize('raw_postcode', ['AA9A AA', 'A9A AA', 'A9 AA', 'A99 AA', 'AA9 AA', 'AA99 AA'])
def test_api_postcodes_uk_invalid_sector(raw_postcode):
    client = APIClient()
    response = client.get('/api/postcodes/uk/', {'postcode': raw_postcode})
    assert response.status_code == 400
    assert response.data['is_valid'] is False
    assert 'sector' in response.data['errors'].keys()
    assert len(response.data['errors']) == 1


@pytest.mark.parametrize('raw_postcode', ['AA9A 9', 'A9A 9', 'A9 9', 'A99 9', 'AA9 9', 'AA99 9',
                                          'AA9A 9AAA', 'A9A 9AAA', 'A9 9AAA', 'A99 9AAA', 'AA9 9AAA', 'AA99 9AAA',
                                          'AA9A 9AAAA', 'A9A 9AAAA', 'A9 9AAAA', 'A99 9AAAA', 'AA9 9AAAA',
                                          'AA99 9AAAA'])
def test_api_postcodes_uk_invalid_unit(raw_postcode):
    client = APIClient()
    response = client.get('/api/postcodes/uk/', {'postcode': raw_postcode})
    assert response.status_code == 400
    assert response.data['is_valid'] is False
    assert 'unit' in response.data['errors'].keys()
    assert len(response.data['errors']) == 1
