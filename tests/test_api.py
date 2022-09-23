from http import client
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_search():
    response = client.get("/search?city=Pingshan&quantity=2")
    assert response.status_code == 200
    assert response.json() == "[[687,\"Berta\",\"Walkden\",\"bwalkdenj2@cdbaby.com\",\"Female\",\"Voonte\",\"Pingshan\"],[849,\"Irena\",\"Hugle\",\"ihuglenk@yandex.ru\",\"Female\",\"Rhyzio\",\"Pingshan\"]]"

def test_not_in_csv():
    response = client.get("/search?city=Pedro&quantity=2")
    assert response.status_code == 200
    assert response.json() == "[]"