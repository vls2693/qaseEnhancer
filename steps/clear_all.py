from steps import remove_all_attachments as attachments, remove_all_projects as projects


def clear_all(token):
    attachments.remove_all_attachments(token)
    projects.remove_all_projects(token)
