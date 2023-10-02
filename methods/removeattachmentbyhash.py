import requests
import urls


def remove_attachment_by_hash(token, attachment_hash):
    url = "{}attachment/{}".format(urls.qase, attachment_hash)
    headers = {"accept": "application/json", "token": token}
    return requests.delete(url, headers=headers)
