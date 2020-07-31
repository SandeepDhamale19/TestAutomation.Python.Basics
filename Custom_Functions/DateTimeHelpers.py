import time
print("Current time: " + time.ctime())

def show_time_mutable_arguments(argTime=time.ctime()):
    currentTime = argTime
    return argTime

def show_time_immutable_arguments(argTime=None):
    if argTime is None:
        currentTime = time.ctime()
    else:
        currentTime = argTime
    return currentTime

