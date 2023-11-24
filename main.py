import removeallattachments
import removeallattachmentsmultithreadingversion
import tokens
import threading
import time
import examplewiththreads

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_time = time.time()
    # removeallattachments.remove_all_attachments()

    # removeallattachmentsmultithreadingversion.remove_all_attachments(tokens.red)
    # removeallattachmentsmultithreadingversion.remove_all_attachments(tokens.green)
    # removeallattachmentsmultithreadingversion.remove_all_attachments(tokens.yellow)
    # removeallattachmentsmultithreadingversion.remove_all_attachments(tokens.white)
    # removeallattachmentsmultithreadingversion.remove_all_attachments(tokens.black)

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

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()


    # examplewiththreads.example_with_threads()

    # examplewiththreads.example_without_threads()

    end_time = time.time()

    execution_time = (end_time - start_time) * 1000
    print('')
    print(f'execution time is {execution_time}')
