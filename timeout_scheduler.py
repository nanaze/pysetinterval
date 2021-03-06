import time
import threading

def _YieldEventTimes(start, interval):
  current = start
  while True:
    yield current
    current += interval

class TimeoutScheduler(object):
  """Utility class to call a callback once per interval."""

  def __init__(self, interval, callback):
    """Create a timeout scheduler.

    The callback will be called once per interval when Start()
    is called.

    interval: Time in seconds (can be float) indicating how
      often callback should be run.
    callback: The callback to call once per interval.
    """
    self.interval = interval
    self.callback = callback

  def Start(self):
    self.event_times = _YieldEventTimes(time.time(), self.interval)
    self._ScheduleNextEvent()

  def _ScheduleNextEvent(self):
    next_event = self.event_times.next()
    interval = max(next_event - time.time(), 0)
    timer = threading.Timer(interval, self._HandleTimer)
    timer.start()

  def _HandleTimer(self):
    self._ScheduleNextEvent()
    self._Run()

  def _Run(self):
    # Launch the callback on a new thread.
    thread = threading.Thread(target=self.callback)
    thread.start()
