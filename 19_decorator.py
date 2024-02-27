import datetime
import time

def logged(functionToLog):
    def logger():
        start = datetime.datetime.now()
        functionToLog()
        execution_time  = datetime.datetime.now()-start
        print(f"Function {functionToLog.__name__} was started {start} and finnished after {execution_time.total_seconds()} s")
    return logger


@logged
def do_this():
    print("Doing this")
    time.sleep(2)



@logged
def do_that():
    print("Doing that")
    time.sleep(1)

do_this()
do_that()