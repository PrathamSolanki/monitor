import os
import shutil
import difflib
import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')
from multiprocessing import Pool


BCKP_DIR = 'backup/'
if not os.path.isdir(BCKP_DIR):
    os.mkdir(BCKP_DIR)

FILES_TO_MONITOR_FILENAME = 'files_to_monitor.txt'


def create_backup(file):
    shutil.copy(file,BCKP_DIR)


def get_diff(file):
    with open(file, 'r') as f:
        changed_file_lines = f.read().strip().splitlines()
        
    with open(BCKP_DIR+file, 'r') as f:
        bckp_file_lines = f.read().strip().splitlines()

    logging.info('')
    for line in difflib.unified_diff(bckp_file_lines, changed_file_lines, fromfile=BCKP_DIR+file, tofile=file, lineterm=''):
        print(line)


def get_files_to_monitor():
    with open(FILES_TO_MONITOR_FILENAME, 'r') as f:
        return f.read().splitlines()


def update_latest_change_time(file):
    latest_change_times[file] = os.stat(file).st_mtime


def detect_change(file):
    if latest_change_times[file] < os.stat(file).st_mtime: return True
    else: return False


def monitor_and_log(file):
    while True:
        try:
            if detect_change(file):
                update_latest_change_time(file)
                get_diff(file)
                create_backup(file)
        except KeyboardInterrupt:
            return KeyboardInterrupt


latest_change_times = {}

files_to_monitor = get_files_to_monitor()

for file in files_to_monitor:
    update_latest_change_time(file)
    create_backup(file)


if __name__ == '__main__':
    try:
        pool = Pool(processes=len(files_to_monitor))
        pool.map(monitor_and_log, files_to_monitor)
    except KeyboardInterrupt:
        os._exit(0)
