### Setup your myaccess/ login

- First step is to set your login email in the line of code.py where it shows as below <br/>
  `LOGIN_EMAIL = "ajsharm@microsoft.com"`

### Setup python environment

- Make sure [python is installed](https://www.python.org/downloads/windows/).
- Run the setup.bat file. It will create a virtual environment and setup all the needed packages.
- If you get "Permission denied error" or "Access denied error" while running the setup.bat for first time, open an elevated command prompt (**Run as Administrator**), navigate to the SuperfastAccess directory and execute setup.bat.

## RUN THE SCRIPT

- Make sure that the entire setup is complete as above. Simply double click run.bat file and everything should work fine. If you end up in some errors related to python then you probably need to check your python installation.


## HotKey Setup (optional)

- If you want to trigger this with the use of HotKeys, the repository contains the hotkeylauncher files. You will need to install [AutoHotKey tool](https://www.autohotkey.com/) on your machine first and then double click the hotkeylauncher.ahk file to activate the hot key detection. Currently the key combination for running the access approval is ```Ctrl+Alt+t``` which you can modify if needed my simply updating the hotkeylauncher.ahk file in notepad with your desired key combination.