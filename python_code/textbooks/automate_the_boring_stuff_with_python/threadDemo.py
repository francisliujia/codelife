import threading, time

def take_a_nap():
    time.sleep(5)
    print("wake up!")

print("start of the program")
threadObj = threading.Thread(target=take_a_nap)
threadObj.start()

print("end of the progam")
