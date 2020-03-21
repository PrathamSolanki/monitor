import os
import shutil
import argparse
import difflib
import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


BCKP_DIR = 'backup/'


def create_backup(files):
    if not os.path.isdir(BCKP_DIR):
        os.mkdir(BCKP_DIR)

    for file in files:
        shutil.copy(file,BCKP_DIR)


def get_diff(file):
    with open(file, 'r') as f:
        changed_file_lines = f.read().strip().splitlines()
        
    with open(BCKP_DIR+file, 'r') as f:
        bckp_file_lines = f.read().strip().splitlines()

    logging.info('')
    for line in difflib.unified_diff(changed_file_lines, bckp_file_lines, fromfile=file, tofile=BCKP_DIR+file, lineterm=''):
        print(line)


parser = argparse.ArgumentParser(description='Monitor files.')
parser.add_argument('--files', nargs='+', help='files to monitor')
args = parser.parse_args()

# create_backup(args.files)
get_diff(args.files[0])