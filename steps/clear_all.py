from steps import remove_all_attachments as attachments, remove_all_projects as projects


def clear_all(tokens):
    for token in tokens:
        attachments.remove_all_attachments(token)
        projects.remove_all_projects(token)
