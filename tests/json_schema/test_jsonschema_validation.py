# import requests
import pytest

import json
import os

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_requests
from src.helpers.common_verifications import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utilis import common_headers_json

from jsonschema import validate
from jsonschema.exceptions import ValidationError


class TestCreateBooking(object):


    def load_schema(self,schema_file):
        with open(schema_file, 'r') as file:
            return json.load(file)


    @pytest.mark.positive
    # url, headers, payload
    def test_create_booking_tc1(self):

        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload=payload_create_booking(), in_json=False)
        print(response)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        verify_response_key_should_not_be_none(response.json()['bookingid'])
        verify_http_status_code(response, 200)
        response_json = response.json()

        file = os.getcwd() + "/schema_json"
        schema = self.load_schema(file)

        try:
            validate(instance = response_json, schema = schema)
        except ValidationError as e:
            print(e.message)