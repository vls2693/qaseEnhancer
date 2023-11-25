import requests
import urls


def get_all_attachments(token):
    url = "{}attachment?limit=100&offset=0".format(urls.qase)
    headers = {"accept": "application/json", "token": token}
    return requests.get(url, headers=headers)


def remove_attachment_by_hash(token, attachment_hash):
    url = "{}attachment/{}".format(urls.qase, attachment_hash)
    headers = {"accept": "application/json", "token": token}
    return requests.delete(url, headers=headers)
