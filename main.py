from steps import clear_all
import tokens
import threading

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    t1 = threading.Thread(clear_all.clear_all(tokens.red))
    t2 = threading.Thread(clear_all.clear_all(tokens.green))
    t3 = threading.Thread(clear_all.clear_all(tokens.yellow))
    t4 = threading.Thread(clear_all.clear_all(tokens.white))
    t5 = threading.Thread(clear_all.clear_all(tokens.black))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
