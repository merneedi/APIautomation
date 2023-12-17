import pytest

from src.helpers.api_requests_wrapper import post_requests,put_requests
from src.constants.api_constants import APIConstants
from src.helpers.utilis import common_headers_json
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verifications import verify_response_key_should_not_be_none, verify_http_status_code


class TestCreateBooking(object):


    def test_create_token(self):
        response = post_requests(url = APIConstants.url_create_token(),in_json =False,headers = common_headers_json(), auth = None, payload=payload_create_booking())
        verify_http_status_code(response,200)
        print(response.json)
        token = response.json()['token']
        print(token)
        verify_response_key_should_not_be_none(token)
        return token

    def test_create_booking(self):
            response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                     payload=payload_create_booking(), in_json=False)
            print(response)
            verify_response_key_should_not_be_none(response.json()['bookingid'])
            verify_http_status_code(response, 200)
            bookingid = response.json()["bookingid"]
            print(bookingid)
            return bookingid

    def test_update_booking(self): # bookingid and token from create booking
            token = "a2c8f5b710cb084"
            put_url = APIConstants.url_create_booking() +"/1021"
            auth =( "admin","password123")
            response = put_requests(url=put_url, auth=auth, headers=common_headers_json(),
                                     payload=payload_create_booking(), in_json=False)
            print(response.json())

    def test_delete_booking(self):
        pass