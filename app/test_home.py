import pytest
from matchapp import app

@pytest.fixture
def client():
    return app.test_client()

def test_index(client):
    resp = client.get('/')
    assert resp.status_code==200

def test_bad_index_method(client):
    resp = client.post('/')
    assert resp.status_code==405

