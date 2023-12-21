#Read the csv or excel file
#create a function create_token which can take valus from the excel file
#verify the expected result

import requests
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.utilis import common_headers_json

# Read the Excel - openpyxl
import openpyxl


# Step 1 Read the File and put the content into a []

def read_credentials_from_excel(file_path):
     # username and password
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row  in sheet.iter_rows(min_row=2, values_only=True):
        username,password = row
        credentials.append({"username" : username, "password" : password})
    return credentials









def make_request_auth(username,password):
    payload ={
        "username" : username,
        "password" : password

    }
    headers ={
        "Content-Type" : "application/json"
    }
    response = requests.post(APIConstants.url_create_token(),
                             headers = common_headers_json(), json = payload)
    assert response.status_code == 200
    return response


@pytest.mark.parametrize("user_cred", read_credentials_from_excel("testdata_ddt.xlsx"))
def test_post_create_token(user_cred):
    username = user_cred["username"]
    password = user_cred['password']
    print(username, password)
    response = make_request_auth(username, password)
    assert response.status_code == 200


