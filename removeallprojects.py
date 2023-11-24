import methods.getallprojects as get
import json


def remove_all_projects():
    data = json.loads(get.get_all_projects("token").text)
    amount_of_projects = data['result']['total']
    project_list = []
    for i in range(0, amount_of_projects):
        project_list.append(data['result']['entities'][i]['code'])
    return project_list


print(remove_all_projects())
