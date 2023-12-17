#To make the post, put, patch, delete, get
import json

import requests

# HTTP Methods - Generic functions

def get_request(url,auth,in_json):
    response = requests.get(url=url,auth=auth)
    if in_json is True:
        return response.json()
    return response

#data > In return json, normal in json != True

def post_requests(auth,url,payload,headers,in_json):
    post_response = requests.post(url=url,headers=headers,auth=auth,data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response

def patch_requests(auth,url,payload,headers,in_json):
    patch_response = requests.patch(url=url,headers=headers,auth=auth,data=json.dumps(payload))
    if in_json is True:
        return patch_response.json()
    return patch_response

def put_requests(auth,url,payload,headers,in_json):
    put_response = requests.put(url=url,headers=headers,auth=auth,data=json.dumps(payload))
    if in_json is True:
        return put_response.json()
    return put_response

def delete_requests(auth,url,payload,headers,in_json):
    delete_response = requests.delete(url=url,headers=headers,auth=auth,data=json.dumps(payload))
    if in_json is True:
        return delete_response.json()
    return delete_response


# XML data -> Json data















