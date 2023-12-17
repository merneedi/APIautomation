from src.constants.api_constants import Base_url,base_url,APIConstants

def test_crud():
    print(Base_url)

    url_dir = base_url()
    print(url_dir)

    url_api = APIConstants().base_url()
    print(url_api)