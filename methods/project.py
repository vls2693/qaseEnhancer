import requests
import urls


def get_all_projects(token):
    url = "{}project?limit=100&offset=0".format(urls.qase)
    headers = {"accept": "application/json", "token": token}
    return requests.get(url, headers=headers)


def remove_project_by_code(token, code):
    url = "{}project/{}".format(urls.qase, code)
    headers = {"accept": "application/json", "token": token}
    return requests.delete(url, headers=headers)
