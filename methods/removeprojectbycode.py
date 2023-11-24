import requests
import urls


def remove_project_by_code(token, code):
    url = "{}project/{}".format(urls.qase, code)
    headers = {"accept": "application/json", "token": token}
    return requests.delete(url, headers=headers)
