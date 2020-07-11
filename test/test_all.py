import pytest
import requests
import tests

def test_test():
    assert True

@pytest.mark.parametrize(
    'label, test', 
    zip(list(map(lambda x: x['label'], tests.TESTS)), 
    tests.TESTS))
def test_all(label, test):
    if 'json' in test:
        r = requests.get('http://localhost:8080/calc', json=test['json'])
    else:
        r = requests.get('http://localhost:8080/calc')
    
    assert r.status_code == 200
    if 'key' in test:
        assert r.json()[test['key']] == test['value'] 
