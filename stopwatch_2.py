import threading
import time
import variables


def update_time():
    while variables.running:
        time.sleep(0.01)
        variables.one_tenth_of_a_second += 1

        if variables.one_tenth_of_a_second >= 95:
            variables.one_tenth_of_a_second = 0
            variables.seconds += 1

        if variables.seconds >= 60:
            variables.seconds = 0
            variables.minutes += 1

        if variables.minutes >= 60:
            variables.minutes = 0
            variables.hours += 1



def start():
    if not variables.running:

        variables.running = True
        thread = threading.Thread(target=update_time, daemon=True)
        thread.start()

def stop():
    variables.running = False

def reset():
    if not variables.running:
        variables.one_tenth_of_a_second = 0
        variables.seconds = 0
        variables.minutes = 0
        variables.hours = 0
    elif variables.running:
        variables.one_tenth_of_a_second = -1
        variables.seconds = 0
        variables.minutes = 0
        variables.hours = 0
        variables.running = False