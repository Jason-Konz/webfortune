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
    assert response.status_code == 200
    assert 'hello world' in response.get_data(as_text=True)

def test_fortune(app, client):
    pass

def test_cowsay_message(app, client):
    pass

def test_cowfotune(app, client):
    pass
