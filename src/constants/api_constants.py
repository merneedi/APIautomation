#   Add your constants here
Base_url = "https://restful-booker.herokuapp.com"

def base_url():
    return "https://restful-booker.herokuapp.com"


class APIConstants(object):

    def base_url(self):
        return "https://restful-booker.herokuapp.com"
    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"
    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    # update,put,patch,delete -bokking id

    def url_patch_delete_booking(booking_id):
        return "https://restful-booker.herokuapp.com/booking" + str(booking_id)