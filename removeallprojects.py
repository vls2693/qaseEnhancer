import methods.getallprojects as get
import methods.removeprojectbycode as remove
import json


def remove_all_projects(token):
    data = json.loads(get.get_all_projects(token).text)
    amount_of_projects = data['result']['total']
    project_list = []
    for i in range(0, amount_of_projects):
        project_list.append(data['result']['entities'][i]['code'])

    for project_code in range(0, len(project_list)):
        remove_response = remove.remove_project_by_code(token, project_code)
        remove_status = json.loads(remove_response.text)['status']
        print(remove_status)
        print(remove_response.text)
        if remove_status is False:
            break
