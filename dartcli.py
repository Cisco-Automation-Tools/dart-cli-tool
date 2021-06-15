import config
import os
import shutil
import subprocess
import time
from datetime import datetime

# This script executes the dartcli utility to collect logs for Cisco AnyConnect.
# Logs are copied locally, renamed to include host machine name and timestamp,
# and then pushed to a remote share.

# Capture current date and time
now = datetime.now()

# Get type of OS (nt = windows, posix = mac)_
os_type = os.name
print ("OS type is: ",os_type)

# Run the DARTCLI command and set filename, local and remote share.
# NT is device type for Windows
if os_type == "nt":
    print("Windows share is:", config.destshare_windows)
    targetfilename = os.getenv('COMPUTERNAME') + "_DARTBundle_" + now.strftime('%d%b%Y_%H%M%S' + ".zip")
    localdir = os.path.join('C:\\', os.environ['HOMEPATH'], 'Desktop\\')
    destshare = config.destshare_windows
    user = os.getlogin()
    subprocess.run(f'C:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client\DART\dartcli -dst "C:\\Users\{user}\\Desktop\\{targetfilename}"')
# Posix is device type for MacOS
elif os_type == "posix":
    print("Mac share is:", config.destshare_mac)
    targetfilename = os.uname().nodename + "_DARTBundle_" + now.strftime('%d%b%Y_%H%M%S' + ".zip")
    localdir = os.path.expanduser(os.path.join('~', 'Desktop/'))
    destshare = config.destshare_mac
    subprocess.run(f'/Applications/Cisco/"Cisco AnyConnect DART.app"/Contents/Resources/dartcli -dst {localdir}{targetfilename}', shell=True)

# Copy file from local to share.
sourcepath = localdir
destpath = destshare
filename = targetfilename

print (f"Copying {targetfilename} to {destpath}")
try: shutil.copyfile(sourcepath + filename, destpath + filename)
except OSError as err: print(err)

# Cleanup - remove local copy of DART zip file.
if os_type == "nt":
    print ("Removing local copy of DART zipfile: ", localdir + targetfilename)
    cleanuploc = localdir + targetfilename
    try: os.remove(f'{cleanuploc}')
    except OSError as err: print(err)
elif os_type == "posix":
    print("Removing local copy of DART zipfile: ", localdir + targetfilename)
    cleanuploc = localdir + targetfilename
    try: os.remove(f'{cleanuploc}')
    except OSError as err: print(err)

# Return complete message to user
print ("DARTCLI info collected and pushed to remote share")
# Sleep to allow user to see complete message before console closes.
time.sleep(3)







