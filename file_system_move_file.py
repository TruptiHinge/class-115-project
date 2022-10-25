import os 
import shutil
import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/HP/Downloads"

class FileEventHandler(FileSystemEventHandler):
              
    def on_modified(self, event):
        print("Hey there!, {event.src_path) has been modified")

event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("running...")

except KeyboardInterrupt:
    print("stopped!")
    observer.stop()