#!/bin/sh
sudo pip install virtualenv
virtualenv --python=/usr/bin/python3.5 she
source she/bin/activate

pip install --upgrade pip
pip install numpy matplotlib scipy scikit-image tensorflow
pip install git+https://github.com/zsdonghao/tensorlayer.git
clear
