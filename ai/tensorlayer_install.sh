#!/bin/sh
sudo pip install virtualenv
virtualenv --python=/usr/bin/python3.5 she
source she/bin/activate

#install TensorLayer 
pip install --upgrade pip && pip install numpy && pip install matplotlib && pip install scipy && pip install scikit-image && pip install tensorflow && pip install git+https://github.com/zsdonghao/tensorlayer.git && clear

