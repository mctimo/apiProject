from utils.http_methods import Http_methods
"""Methodes for testing Goolge Maps API"""


base_url = "https://rahulshettyacademy.com"  # Base URL adress
key = "?key=qaclick123"  # Base key

class Google_maps_api():
    """Method for creating new location"""

    @staticmethod
    def creat_new_place():

        json_for_creat_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json"  #resourse for POST
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_creat_new_place)
        print(result_post.text)
        return result_post

    """Method for checking location"""

    @staticmethod
    def get_new_place(place_id):
        get_resourse = "/maps/api/place/get/json"  # resourse for get request

        get_url = base_url + get_resourse + key + "&place_id=" + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        return result_get

    """Method for update new location"""

    @staticmethod
    def put_new_place(place_id):
        put_resourse = "/maps/api/place/update/json"  # resourse for update request
        put_url = base_url + put_resourse + key

        print(put_url)

        put_body = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        result_put = Http_methods.put(put_url, put_body)
        return result_put

    """Method for deleting new location"""

    @staticmethod
    def delete_new_place(place_id):
        delete_resourse = "/maps/api/place/delete/json"  # resourse for delete request

        delete_url = base_url + delete_resourse + key

        delete_body = {
            "place_id": place_id,
        }
        print(delete_url)
        result_delete = Http_methods.delete(delete_url, delete_body)
        return result_delete
