import pytest

from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    yield app.test_client()


def test_index(app, client):
    #assert something
    response = client.get('/')
    assert response.status_code == 302

def test_fortune(app, client):
    response = client.get('/fortune/')
    assert response.status_code == 200

def test_cowsay_message(app, client):
    message = 'Hello DevOps'
    response = client.get('/cowsay/%s/' % message)
    assert response.status_code == 200
    assert '(oo)' in response.get_data(as_text=True)
    assert 'Hello DevOps' in response.get_data(as_text=True)

def test_cowfortune(app, client):
    response = client.get('/cowfortune/')
    assert response.status_code == 200
    assert '(oo)' in response.get_data(as_text=True)
