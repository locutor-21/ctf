#!/bin/bash
 █
python -c "import pyqrcode;cmd=pyqrcode.create('ls',version=2);print(cmd.text())" |, 
sed 's/0/█  /g;s/1/ /g;' 
