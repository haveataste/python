#!/bin/bash
:<<!
#实验楼Django项目 删除软链接python，创建指向python3.5的软链接,安装Django
sudo rm /usr/bin/python
sudo ln -s /usr/bin/python3.5 /usr/bin/python
#sudo pip install --upgrade pip
sudo pip install Django==1.11
python
>>>import django
>>>django.get_version()
'1.11'
>>>django.VERSION
!

#git clone https://github.com/kuugagoku/django.git
sudo rm /usr/bin/python && sudo ln -s /usr/bin/python3.5 /usr/bin/python && sudo pip install django==1.11 && clear

#下载脚本并执行；下载django.txt
:<<!
sudo sh -c "echo '151.101.72.133  raw.githubusercontent.com' >> /etc/hosts"
wget https://raw.githubusercontent.com/kuugagoku/django/master/run.sh -O- | sh
wget -P ~ https://raw.githubusercontent.com/kuugagoku/django/master/django.txt
clear
!
