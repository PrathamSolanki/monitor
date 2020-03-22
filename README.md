# Monitor

Detects changes in a given list of files and logs a message to the console. This message comprises of the filename, the date of change and the diff.

## How to use?

Put the names of the files that you want to monitor in `files_to_monitor.txt`. Note that this `files_to_monitor.txt` should be in the same directory as `monitory.py`. Also, if the files you want to monitor aren't in the same directory you will need to put absolute path + the filename inside `files_to_monitor.txt`.

After this, just run the script using `python monitor.py`. Note that the script requires `Python3`. It will log to the console as you make changes to the files mentioned in `files_to_monitor.txt`.

## OS tested on

- Ubuntu 18.04.2 LTS
- Windows 10
