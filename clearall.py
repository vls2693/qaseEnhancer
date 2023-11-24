import removeallattachmentsmultithreadingversion as attachments
import removeallprojects as projects


def clear_all(token):
    attachments.remove_all_attachments(token)
    projects.remove_all_projects(token)
