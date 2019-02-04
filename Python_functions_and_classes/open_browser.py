""" This is a simple function that allows you to open a url of your choice at specific time intervals.
    This is to help an individual working to take some break.
"""

import time
import webbrowser

total_breaks = 3
break_num = 0

print("This program started: "+ time.ctime())
while (break_num < total_breaks):
    # time is in seconds
    time.sleep(7200)
    # this opens a youtube video, but you can change it to your preference
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=klZ0nJZ9fO8" + 'doc/')
    break_num += 1