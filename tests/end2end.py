import os
import pytest
import requests


main_url = "http://localhost:8000"


@pytest.fixture
def teardown():
    yield
    files = os.listdir("assets")
    for file in files:
        os.remove(os.path.join("assets", file))


@pytest.mark.dependency()
def test_fetch_image():
    headers = {"Content-Type": "application/json",
               "Accept": "application/json"}
    bbox = {"minLong": 24.644842122715147,
            "minLat": 42.06253714023231,
            "maxLong": 24.89038637385545,
            "maxLat": 42.19082231860318}
    url = main_url + "/fetch_image"
    response = requests.post(url, headers=headers, json=bbox)
    print(response.text, bbox)
    assert response.status_code == 200


@pytest.mark.dependency(depends=["test_fetch_image"])
def test_custom_image_upload():
    file = [('file', ('test.jpg', open('tests/assets/test.jpg', 'rb'),
                      'image/jpeg'))]
    bbox = {"minLong": 1.1, "minLat": 1.1, "maxLong": 1.1, "maxLat": 1.1}
    url = main_url + "/custom_image_upload"
    response = requests.post(url, params=bbox, files=file)
    assert response.status_code == 201


@pytest.mark.dependency(depends=["test_custom_image_upload"])
def test_fetch_custom_image():
    headers = {"Content-Type": "application/json",
               "Accept": "application/json"}
    bbox = {"minLong": 1.1, "minLat": 1.1, "maxLong": 1.1, "maxLat": 1.1}
    url = main_url + "/fetch_image"
    response = requests.post(url, headers=headers, json=bbox)
    assert response.status_code == 200


@pytest.mark.dependency(depends=["test_fetch_custom_image"])
def test_get_image_colour(teardown):
    headers = {"Content-Type": "application/json",
               "Accept": "application/json"}
    bbox = {"minLong": 1.1, "minLat": 1.1, "maxLong": 1.1, "maxLat": 1.1}
    url = main_url + "/get_image_colour"
    response = requests.post(url, headers=headers, json=bbox)
    assert response.status_code == 200
    assert response.json()["colour"] == "white"
