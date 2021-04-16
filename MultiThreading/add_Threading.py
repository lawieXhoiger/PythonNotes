import threading

def show_threading():
    print("threading active count:",threading.active_count())
    print("threading enumerate:",threading.enumerate())
    print("threading current thread",threading.current_thread())

def thread_jod():
    print("this is a thread of {}".format(threading.current_thread()))

def main():
    thread = threading.Thread(target=thread_jod(),)
    thread.start()

if __name__ == "__main__":
    show_threading()
    main()