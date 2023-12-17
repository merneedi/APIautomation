
def payload_create_booking():
    {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

def payload_create_token():
    payload = {
        "username" : "admin",
        "password" : "password123"
    }
    return payload