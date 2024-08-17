import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


response = post_new_user(data.user_body).json()
auth_token = response['authToken']

auth_header = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {auth_token}'
}


def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=auth_header)


response = post_new_client_kit(data.kit_body)
