# pysetinterval
Python class to call a callback on a new thread once every interval.

Makes up for the fact that the Python Standard Library doesn't have a good equivalent for JavaScript window.setInterval()

Tracks expected times and adjusts timeout lengths to manage impercise timers so that the callback is called as close
to once per interval as possible (a more intelligent implementation than the naive run, wait, run, wait loop, which can mistakenly include the callback's exec time or drift away from the set interval if the timer is inconsistent).
