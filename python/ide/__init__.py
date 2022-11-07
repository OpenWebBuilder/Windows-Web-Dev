import os
import subprocess as sp
from getpass import getpass


def askPassword():
    # passwd = getpass('Password:')
    passwd = "123cocoa"
    return passwd

def runAsAdmin():
    altrunAsAdmin()

def altrunAsAdmin():
    app = "atom"

    passwd = askPassword()
    run = f"choco.exe info {app}"
    passw = "123cocoa%"

    # prog = sp.Popen(['runas', '/noprofile', '/user:Administrator', f"choco.exe info {app}"],stdin=sp.PIPE)
    prog = sp.Popen(['runas', '/user:Administrator', 'notepad.exe'],stdin=sp.PIPE)
    prog.stdin.write(passw.encode())
    prog.communicate()

# Run as Admin
## works: https://stackoverflow.com/a/70300888
# error: https://stackoverflow.com/questions/47380378/run-process-as-admin-with-subprocess-run-in-python
## solution: https://stackoverflow.com/questions/62683706/typeerror-a-bytes-like-object-is-required-not-str-using-subprocess-python

# -> https://github.com/JetBrains/intellij-community/tree/master/native/WinElevator
# Alt:
# https://superuser.com/a/1330549


# Set Admin Password:
# https://www.ghacks.net/2021/10/01/how-to-enable-the-hidden-windows-11-administrator-account/#:~:text=The%20default%20administrator%20account%20of,and%20hit%20the%20Enter%2Dkey.

# Bug: PyCharm hangs with `getpass`
# Solution: https://stackoverflow.com/questions/28579468/how-to-use-the-python-getpass-getpass-in-pycharm