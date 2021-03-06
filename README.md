# RTI Prediction Model in Python
Rowe Technologies Inc. Prediction Model for ADCP1 Hardware.  Software used to plan a deployement for a Rowe Technologies Inc. ADCP.  Battery usage, standard deviation (accuarcy), memory usage, maximum range and maximum velocity are estimated based on the configuration.  Multiple configurations can be created for a single deployment.  As values are changed, the predictions will give a live update.

![PredictR](http://rowetechinc.com/img/swfw/predictr.png)

# Installation of Source Code
The software is assumed to be in the path Documents\rti\python.  You will need to modify the .spec files with the correct paths to create an installer.

# Create PredictR application
OSX
```javascript
pyinstaller Predictr_installer_OSX.spec
```

Windows

You will need to install MSVC 2015 redistribution.


Then add C:\Program Files (x86)\Windows Kits\10\Redist\ucrt\DLLs\x64 to environment PATH. Then the warning message about api-ms-win-crt-***.dll will disappear and all works correctly.

```javascript
venv\Scripts\pyinstaller.exe Predictr_installer_WIN.spec
```

This will create a dist and build folder.  The exe in is the dist folder.


#To create a new Pyinstaller spec file
OSX
```javascript
pyinstaller /path/to/mainwindow.py --windowed --onefile
```

Windows
```javascript
venv\Scripts\pyinstaller.exe  --windowed --onefile --paths C:\Users\XXX\AppData\Roaming\Python\Python35\site-packages\PyQt5\Qt\bin /path/to/mainwindow.py

or

pyi-makespec --onefile --windowed yourprogram.py
```

If you need to debug the application, set the `console=True`

You will need to add the predictor.json to the data=[] in the spec file.
Use the spec files as an example for the data=[] settings.

Windows must include the path to PyQT5 DLL files.


#Compile QT5 .UI files
OSX
```javascript
pyuic5 -x file.ui -o file.py
```

Windows
```javascript
python -m PyQt5.uic.pyuic -x filename.ui -o filename.py

C:\Users\XXX\AppData\Local\Programs\Python\Python35\Scripts\pyuic5.exe -x file.ui -o file.py
```

#Compile QT5 .qrc files
Add all the images included in the .qrc file.  Then compile it.
Also add the images to the spec file.

OSX
```javascript
pyrcc4 -o images.qrc images_qr.py
```

#Unit Testing
```python
cd ADCP\Predictor
pytest
```


#Install Virtualenv in Windows
```python
pip install virtualenv
pip install virtualenvwrapper-win
```

```python
virtualenv env

Windows
env\Scripts\activate
```


#Run Utilties Apps
OSX and Linux
```javascript
export PYTHONPATH=$PYTHONPATH:/path/to/rti_python

python3 Utilities/EnsembleFileReport.py -i file -v
```

Windows
```javascript
set PYTHONPATH=%PYTHONPATH%;/path/to/rti_python
```
