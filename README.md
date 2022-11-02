The goal of this project is to rename photo files with a concatenation of the date taken and the original photo file name.
Code uses exif which must be installed via PIP.

py -m pip exifread

If using PyCharm, it must be added manually to the virtual environment. 
1. Open project settings (File > Settings...)
2. Project > Project Interpreter
3. Press the + button 
4. Type "exifread" in the top search box 
5. In the lower right corner choose "specify version" if needed 
6. Choose your version and press Install Package

Good discussion here:
https://stackoverflow.com/questions/41206850/how-can-i-update-pip-in-pycharm-when-i-have-two-versions-of-python
