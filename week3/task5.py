import numpy as np

today = np.datetime64("today", "D")
print("Today:",today)

yesterday = today - np.timedelta64(1, "D")
print("Yesterday:",yesterday)

tomorrow = today + np.timedelta64(1, "D")
print("Tomorrow:",tomorrow)