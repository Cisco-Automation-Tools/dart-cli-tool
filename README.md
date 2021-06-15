# AnyConnect DART cli tool for Mac/Windows
Executes the Cisco AnyConnect dartcli command and pushes resulting zip file to remote repository.
 
## Introduction

DART is the AnyConnect Diagnostics and Reporting Tool that you can use to collect data for troubleshooting AnyConnect installation and connection problems. DART assembles the logs, status, and diagnostic information for Cisco Technical Assistance Center (TAC) analysis. 

Typically, launching DART, collecting the logs, and pushing the log file to remote file share was a multi-step process.  This DART cli tool script automates that process into a single executable that automatically does those steps.

The result is the simple collection of useful AnyConnect data into a .zip file that goes to a predetermined file share.  All the end-user has to do is double-click the DARTCLI executable and the script handles the rest.  Here is a summary of the script execution:

1. Create zip filename based on local machine name and date/time.
2. Execute dartcli utility to collect AnyConnect diagnostics and put them into predetermined zip file.
3. Copy the zip file into local user Desktop folder.  << this is necessary since the dartcli tool cannot copy to a remote share directly.
4. Push the file from the local desktop to the remote share.
5. Remove the local copy of the zip file.
 
## Disclaimer

This is not an officially supported tool and was developed as a side project, not as an official release by Cisco.  Any support received will be on an as-available timeframe and feature requests may not be fulfilled.

## Installation
 
No installation is required.  The python script can be downloaded or cloned from GitHub.

Ideally, an executable should then be created locally using [PyInstaller](https://www.pyinstaller.org/):
> pyinstaller --onefile --console .\dartcli.py

Using the dartcli.py file as a source for PyInstaller, a separate executable should be created for MacOS (.app) and Windows (.exe). The Python script driving the executable automatically detects the underlying OS when it is ran on the end user's device.

That executable .app or .exe should then be distributed to end-users as needed via a mechanism such as Software Center.

** IMPORTANT ** Prior to creating an executable, the remote share should be configured in the config.py file.  Open the config.py file in a text editor.  Locate the destshare variables for windows and mac.  Set both appropriately using the following examples as a guide:

destshare_windows = \\172.18.149.45\SHARE\AnyConnect_logs\\  
(SHARE = remote share name or parent directory, AnyConnect_logs = suggested subdirectory name)

destshare_mac = /Volumes/SHARE/AnyConnect_Logs/ \
(SHARE = remote share name or parent directory, AnyConnect_logs = suggested subdirectory name)

These share values will then be compiled into the executable so the user doesn't have to do manually.

The script will push the .zip file to either of these locations depending on which OS is detected.


## Usage

The end user will need to ensure a network drive is mapped to the predetermined remote share on the machine to run the dartcli tool.
 
To start the tool, simply double-click the executable.  The DARTCLI will run and will take a few minutes.  It will collect the appropriate files and the push them to the remote share.

In actuality, the script is pulling the files to a local directory on the user's device.  Then the file is pushed to the remote share.  Once done, the local copy is removed.

 
## DART for Mac example
The following is output while running dartcli script on Mac using the executable previously built w/PyInstaller:

![](/images/dart_cli_macos.png)

## DART for Windows example
The following is output while running dartcli script on Windows using the executable previously built w/PyInstaller:

![](/images/dart_cli_win_1.png)

Here you can see the final messaging stating the script was completed and the file pushed to remote share.

![](/images/dart_cli_win_2.png)
