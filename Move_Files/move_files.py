''' File that actually trackes and moves files '''

import os
import pathlib
import subprocess
import sys
import time

import config

subprocess.check_call([sys.executable, "-m", "pip", "install", "watchdog"])
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class Myhandler(FileSystemEventHandler):
    ''' Holds the actions goint to be executed on the tracked folder '''

    def __init__(self, download_path):
        self.download_path = download_path

    def what_file(self, filename):
        ''' determine file destination based on extension '''
        path = os.path.join(self.download_path, filename)
        extension = pathlib.Path(path).suffix
        if extension in config.text_extensions:
            new_path = config.TEXT
        elif extension in config.images_extensions:
            new_path = config.IMAGES
        elif extension in config.images_extensions:
            new_path = config.OFFICE
        else:   # dont move
            dest_path = self.download_path
        new_path = os.path.join(dest_path, filename)
        return extension, new_path

    def on_modified(self, event):
        '''
        called on trackers regirsters a modification
        sends any new file to the correct destination
        '''
        for filename in os.listdir(self.download_path):
            initial_path = os.path.join(self.download_path, filename)
            extension, new_path = self.what_file(filename)
            file_already_exists = os.path.isfile(new_path)
            i = 0
            while file_already_exists:
                i += 1
                new_path = new_path.replace(extension, f"_{i}{extension}")
                file_already_exists = os.path.isfile(new_path)
            os.rename(initial_path, new_path)


def start_tracking():
    '''
    initiate a tracker on that directory
    will register every modification made
    '''
    download_path = f'/home/{config.user_name}/Desktop'
    event_handler = Myhandler(download_path)
    # event_handler.on_modified= on_modified
    observer = Observer()
    observer.schedule(event_handler, download_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(3)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


start_tracking()
