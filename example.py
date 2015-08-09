import time
from timeout_scheduler import TimeoutScheduler
import timeout_scheduler

def SayHello():
  print "Hello! The time is", time.time()

ts = TimeoutScheduler(1.0, SayHello)

ts.Start()
