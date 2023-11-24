import json
import methods.getallattachments as get
import methods.removeattachmentbyhash as delete


def remove_all_attachments(token):
    # parse get response
    data = json.loads(get.get_all_attachments(token).text)
    total_amount_of_attachments = data['result']['total']
    amount_of_calls = (total_amount_of_attachments // 100) + 1
    for call in range(0, amount_of_calls):
        response = get.get_all_attachments(token)
        print(response.text)
        # parse get response
        data = json.loads(response.text)
        amount_of_attachments = data['result']['count']
        if amount_of_attachments != 0:
            # collect all attachment objects from response
            attachments = data['result']['entities']
            # collect hashes
            hashes = []
            for attachment in attachments:
                hashes.append(attachment['hash'])
            for hash_to_show in hashes:
                print(hash_to_show)
            # remove attachments
            for attachment_hash in range(0, len(hashes)):
                remove_response = delete.remove_attachment_by_hash(token, hashes[attachment_hash])
                remove_status = json.loads(remove_response.text)['status']
                print(remove_status)
                print(remove_response.text)
                if remove_status is False:
                    break
