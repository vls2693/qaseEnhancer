import removeallattachmentsmultithreadingversion
import tokens
import threading

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    t1 = threading.Thread(removeallattachmentsmultithreadingversion.remove_all_attachments(tokens.red))
    t2 = threading.Thread(removeallattachmentsmultithreadingversion.remove_all_attachments(tokens.green))
    t3 = threading.Thread(removeallattachmentsmultithreadingversion.remove_all_attachments(tokens.yellow))
    t4 = threading.Thread(removeallattachmentsmultithreadingversion.remove_all_attachments(tokens.white))
    t5 = threading.Thread(removeallattachmentsmultithreadingversion.remove_all_attachments(tokens.black))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
