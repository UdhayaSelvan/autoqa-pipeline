import requests

BASE_URL = "https://restful-booker.herokuapp.com"


def test_create_booking():
    payload = {
        "firstname": "Udhaya",
        "lastname": "Selvan",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(f"{BASE_URL}/booking", json=payload)

    assert response.status_code == 200
    assert "bookingid" in response.json()


def test_get_booking():
    response = requests.get(f"{BASE_URL}/booking/1")

    assert response.status_code == 200
    assert "firstname" in response.json()