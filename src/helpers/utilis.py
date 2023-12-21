#Common headers


def common_headers_json():
    headers = {
        "Content-Type" :"application/json",
    }
    return headers

def common_headers_for_put_Delete_Patch():
    headers = {
          "Content-Type": "application/json",
          "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
    }
    return headers
def common_headers_xml():
    headers ={
        "Content-Type" :"application/xml",
    }
    return headers

#Read data from excel,json,yaml - keep the functions in future

