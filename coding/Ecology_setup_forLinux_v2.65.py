#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import collections
import os
import sys
import re
import datetime, time
import socket
import codecs
from hashlib import md5
import readline
import commands
import xml.etree.ElementTree as ET
reload(sys)
sys.setdefaultencoding('utf8')
type_ = sys.getfilesystemencoding()
local_base_path = os.getcwd()

# Ecology_setup_forLinux_v2.0.py
# Linux下自动部署Ecology及配置相关参数
# author: WuQian

# 解压文件
unzip = lambda file: os.system('unzip -o -q "%s"'%file)
tar_gz = lambda file: os.system('tar -zxf "%s"  '%file)
# 当前文件夹下的所有文件及文件夹
show_all_files = lambda path: os.listdir(path)


class ShowProcess():
    """
    显示处理进度的类
    调用该类相关函数即可实现处理进度的显示
    """
    # i = 0 # 当前的处理进度
    max_steps = 0 # 总共需要处理的次数
    max_arrow = 15 #进度条的长度
    infoDone = 'done'

    # 初始化函数，需要知道总共的处理次数
    def __init__(self, current_step,max_steps,infoDone):
        self.current_step = current_step
        self.max_steps = max_steps
        self.infoDone = infoDone
    def show_process(self, current_step=None):
        if current_step is not None:
            self.current_step = current_step
        num_arrow = int(self.current_step * self.max_arrow / self.max_steps) #计算显示多少个'>'
        num_line = self.max_arrow - num_arrow #计算显示多少个'-'
        percent = self.current_step * 100.0 / self.max_steps #计算完成进度，格式为xx.xx%
        marked = 'Hold on...'
        # process_bar = '[' + '>' * num_arrow + '-' * num_line + ']'\
        #               + '%.2f' % percent + '%' + '\r' #带输出的字符串，'\r'表示不换行回到最左边
        sys.stdout.write(marked) #这两句打印字符到终端

        sys.stdout.flush()
        if self.current_step >= self.max_steps:
            self.close()

    def close(self):
        print('')
        print(self.infoDone)
        self.current_step = 0

def check_Resin_version(resin_conf):
	if os.path.exists(os.path.join(resin_conf,'resin.properties')) and os.path.exists(os.path.join(resin_conf,'resin.xml')):
		return True
	else:
		return False

def ModifyXmlFile(xml_name):
	if os.path.exists(xml_name):
		print 'Removing session-config element from %s'%xml_name
		try:
			tree = ET.parse(xml_name)
			root = tree.getroot()
			s =root.find('session-config') # Resin4需要删除<session-config>这个元素
			if s is not None:
				root.remove(s)
				tree.write(xml_name,'utf-8',True)
				print '%s has been Modified！\n'%xml_name
			else:
				print '%s does not need to be modified！\n'%xml_name
		except Exception as e:
			print e
def generate_file_md5value(fpath):
	'''以文件路径作为参数，返回对文件md5后的值'''
	m = md5()
	# 需要使用二进制格式读取文件内容
	a_file = open("%s.md5" % fpath, 'rb') 
	m.update(a_file.read())
	a_file.close()
	return m.hexdigest()
  
def generate_file_md5sumFile(fpath):
	fname = os.path.basename(fpath)
	fpath_md5 = "%s.md5" % fpath
	fout = open(fpath_md5, "w")
	fout.write("%s" %generate_file_md5value(fpath))
	fout.flush()
	fout.close()

def Unzip_file():
	"""进入当前目录解压缩安装包"""
	print '[1]Preparing to unzip Ecology,Resin and JDK...'
	sum_zip=[]
	count=0
	for zip_item in show_all_files(local_base_path):
		if zip_item[-3:] == 'zip' or zip_item[-3:] == '.gz':
			sum_zip.append(zip_item)
	if len(sum_zip)>0:
		for zip_item in show_all_files(local_base_path):
			if zip_item[-3:] == 'zip':
				count+=1
				sys.stdout.write('\rinflating ... %s \n'%zip_item)
				process_bar = ShowProcess(count,len(sum_zip),'Unzip completely!')
				process_bar.show_process()
				unzip(zip_item)
				sys.stdout.flush()
			elif zip_item[-3:] == '.gz':
				count+=1
				sys.stdout.write('\rinflating ... %s \n'%zip_item)
				process_bar = ShowProcess(count,len(sum_zip),'Unzip completely!')
				process_bar.show_process()
				sys.stdout.flush()
				tar_gz(zip_item)
		return True
	else:
		return False
def Meminfo():
    """获取当前操作系统可用内存,为MemFree+Buffers+Cached"""
    orderdic = collections.OrderedDict()
    with open('/proc/meminfo') as f:
        for line in f:
            orderdic[line.split(':')[0]] = line.split(':')[1].strip()
    free_memory = int(re.sub("\D","",orderdic['MemFree']))/1024
    buffers = int(re.sub("\D","",orderdic['Buffers']))/1024
    Cached = int(re.sub("\D","",orderdic['Cached']))/1024
    MemAvailable = free_memory + buffers +Cached
    return MemAvailable

def Monitor_port(ip,port):
	"""判断指定端口是否被启用"""
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		s.connect((ip,int(port)))
		s.shutdown(2)
		print '*********************warning*********************'
		print '%d is occupied!' % port
		return True
	except:
		print '%d is available!' % port
		return False


def dos_to_unix(fileobj):
	"""将文件格式从dos转为unix"""
	with open(fileobj,'rb+') as f:
		data = f.read()
		data = data.replace('\r\n', '\n')
		f.seek(0, 0)
		f.truncate()
		f.write(data)

def Modify_keywords(fileobj,source,target,tip):
	"""根据指定的关键字修改"""
	if os.path.exists(fileobj):
		print 'Checking:'+tip
		with open(fileobj,'r+') as f:
			lines = f.read()
			if '\\' in target:
				target =target.replace('\\','\\\\')
			if '\\' in source:
				source =source.replace('\\','\\\\')
			if '*' in source:
				source = source.replace('*','\\*')
			re_txt = re.sub(source,target,lines)
			if '*' in source:
				print 'Change: '+source.replace('\\','')+' to: '+target.replace('\\','')
			else:
				print 'Change: '+source.replace('\\\\','\\')+' to: '+target.replace('\\\\','\\')
			f.tell()
			f.seek(0,0)
			f.truncate()
			f.write(re_txt)
		dos_to_unix(fileobj)
		time.sleep(0.5)
		print '...Modified successfully!'
	else:
		print '%s not exists，unable to configure!'%fileobj
	return 1
def Modify_port(p,file_obj,s_str,tip):
	"""修改默认端口"""
	if_input_port = True
	current_port = int(p)
	if Monitor_port('127.0.0.1',current_port):
		while if_input_port:
			new_port = raw_input('Please input a new port:')
			new_port = new_port.strip()
			if new_port.isdigit():
				new_port = int(new_port)
				if 0<new_port<65535:
					current_port = new_port
					if Monitor_port('127.0.0.1',current_port):
						if_input_port = True
					else:
						current_port = str(current_port)
						t_str = s_str.replace(p,current_port)
						Modify_keywords(file_obj,s_str,t_str,tip)
						print 'Port %s Will be used!'%current_port
						print os.linesep
						if_input_port = False
				else:
					print 'The port number must be 1 to 65535'
			else:
				print 'Port must be a integer!'
	else:
		print os.linesep
		print 'Would you like to change the port %d ?'%current_port
		# choice=["yes:change","no:cancel"]
		# print choice
		choice_self = raw_input('Please choice(y:confirm/any other keys:cancel):').strip()
		if choice_self == 'y':
			while if_input_port:
				new_port = raw_input('Please input a new port:')
				new_port = new_port.strip()
				if new_port.isdigit():
					new_port = int(new_port)
					if 0<new_port<65535:
						current_port = new_port
						if Monitor_port('127.0.0.1',current_port):
							if_input_port = True
						else:
							current_port = str(current_port)
							t_str = s_str.replace(p,current_port)
							Modify_keywords(file_obj,s_str,t_str,tip)
							print 'Port %s Will be used!'%current_port
							print os.linesep
							if_input_port = False
					else:
						print 'The port number must be 1 to 65535'
				else:
					print 'Port must be a integer!'
		else:
			current_port = str(current_port)
			print 'Port %s Will be used!'%current_port
			print os.linesep
			if_input_port = False
	return current_port



def Init_setup_Resin3(Ecology_dir,Resin_dir,JDK_dir,new_install = True):
	port_list_configuration =[]
	resin_bin = os.path.join(Resin_dir,'bin')
	resin_conf = os.path.join(Resin_dir,'conf')
	# jdk_home = os.path.join(local_base_path,'jdk1.8.0_151')
	# ecology_dir = os.path.join(local_base_path,'ecology')

	httpd_f = os.path.join(resin_bin,'httpd.sh')
	startresin_f = os.path.join(resin_bin,'startresin.sh')
	stopresin_f = os.path.join(resin_bin,'stopresin.sh')
	resin_conf_f = os.path.join(resin_conf,'resin.conf')

	tips = {1:' httpd.sh',
			2:' startresin.sh',
			3:' stopresin.sh',
			4:' resin.conf\'s Xmx',
			5:' resin.conf\'s Xms',
			6:' resin.conf\'s #INSTALLDIR#ecology',
			7:' resin.conf\'s javac compiler directory',
			8:' resin.conf\'s http listening port',
			9:' resin.conf\'s hmux listening port',
			10:' resin.conf\'s watchdog-port'
	}

	print os.linesep
	# #给ecology，Resin和JDK授权
	print '[2]To grant authorization for ecology,Resin and JDK:'
	os.system("chmod 775 ./* -R")
	print 'Grant succeeded.'
	print os.linesep
	print '[3]Modify related configuration file:'
	# 修改startresin.sh,stopresin.sh,httpd.sh
	# default_resin_path = r'/usr/weaver/resin/bin'
	# default_resin_path2 = r'/usr/weaver/Resin/bin'
	# default_jdk_home_path = r'/usr/weaver/jdk1.6.0_27'
	# Modify_keywords(httpd_f,default_jdk_home_path,jdk_home,tips[1])
	if os.path.exists(httpd_f):
		with open(httpd_f) as f:
			strs01 = f.read()
			java_home_list = re.findall(r'JAVA_HOME=.+\w',strs01)
			if len(java_home_list)>0:
				s_str = java_home_list[0]
				t_str = 'JAVA_HOME=%s'%JDK_dir
				Modify_keywords(httpd_f,s_str,t_str,tips[1])
	else:
		print '%s does not exist!'%httpd_f
	if os.path.exists(startresin_f):
		with open(startresin_f,'r+') as f:
			f.truncate()
			start_sh ='ulimit -n 65535\n'
			start_sh +='export LC_ALL=zh_CN.gbk\n'
			start_sh +='export LANG=zh_CN.gbk\n'
			start_sh +='%s start\n'%httpd_f
			f.write(start_sh)
			print 'The file "%s" has been Modified.'%startresin_f
	else:
		print '%s does not exist!'%startresin_f
	if os.path.exists(stopresin_f):
		with open(stopresin_f,'r+') as f:
			f.truncate()
			stop_sh ='%s stop\n'%httpd_f
			f.write(stop_sh)
			print 'The file "%s" has been Modified.'%stopresin_f
	else:
		print '%s does not exist!'%stopresin_f

	if os.path.exists(resin_conf_f):
		with open(resin_conf_f) as f:
			strs1 = f.read()
			Installation_ecology_list = re.findall(r'web-app id="/" root-directory="(.+?)"',strs1)
			if len(Installation_ecology_list)>0:
				Modify_keywords(resin_conf_f,Installation_ecology_list[0],Ecology_dir,tips[6])
		with open(resin_conf_f) as f:
			strs2 = f.read()
			Installation_jdk_list = re.findall(r'javac compiler="(.+?)"',strs2)
			if len(Installation_jdk_list)>0:
				Modify_keywords(resin_conf_f,Installation_jdk_list[0],'%s/bin/javac'%JDK_dir,tips[7])

		# 修改resin.conf下的内存参数，ecology目录
		free = Meminfo()
		if free<2048: # 可用内存必须大于或等于2G
			print 'The available memory is %dM.Warning memory is too small,unable to configure!'%free
			print "Stop configuration!"
		else:
			resin_proposal_memo = int(free*0.5)
			if 1024 <= resin_proposal_memo <=3550: # 如果可用内存为2048到3550之间就可以配置一半可程序使用
				print 'The available memory is %dM.Do you continue to modify memory parameters?'%free
				print 'We recommend available memory is %dM,would like to change default 3550M?'%resin_proposal_memo
				choice = raw_input('Please choice(y:confirm/any other keys:cancel):').strip()
				if choice == 'y':
					# Modify_keywords(resin_conf_f,'<jvm-arg>-Xmx3550m</jvm-arg>','<jvm-arg>-Xmx%dm</jvm-arg>'%resin_proposal_memo,tips[4])
					# Modify_keywords(resin_conf_f,'<jvm-arg>-Xms3550m</jvm-arg>','<jvm-arg>-Xms%dm</jvm-arg>'%resin_proposal_memo,tips[5])
					with open(resin_conf_f) as f:
						strs4 = f.read()
						xmx_list = re.findall(r'-Xmx(.+?)m',strs4)
						if len(xmx_list)>0:
							xmx_num = xmx_list[0]
							Modify_keywords(resin_conf_f,'<jvm-arg>-Xmx%sm</jvm-arg>'%xmx_num,'<jvm-arg>-Xmx%dm</jvm-arg>'%resin_proposal_memo,tips[4])
					with open(resin_conf_f) as f:
						strs5 = f.read()
						xms_list = re.findall(r'-Xms(.+?)m',strs5)
						if len(xms_list)>0:
							xms_num = xms_list[0]
							Modify_keywords(resin_conf_f,'<jvm-arg>-Xms%sm</jvm-arg>'%xms_num,'<jvm-arg>-Xms%dm</jvm-arg>'%resin_proposal_memo,tips[5])
				else:
					# print 'The current default memory parameter is 3550M, which can be changed manually if desired!'
					# print 'The current default memory parameter is 3550M, which can be changed manually if desired!'
					# print '当前内存参数仍然是3550M，如果需要调整请后续手动修改'.encode('gbk')
					with open(resin_conf_f) as f:
						strs4 = f.read()
						xmx_list = re.findall(r'-Xmx(.+?)m',strs4)
						if len(xmx_list)>0:
							xmx_num = xmx_list[0]
							print 'The current parameters %s\'s Xmx is not modified, the default is "%sm".If you need to adjust them, please modify them manually later!'%(resin_conf_f,xmx_num)
					with open(resin_conf_f) as f:
						strs5 = f.read()
						xms_list = re.findall(r'-Xms(.+?)m',strs5)
						if len(xms_list)>0:
							xms_num = xms_list[0]
							print 'The current parameters %s\'s Xms is not modified, the default is "%sm".If you need to adjust them, please modify them manually later!'%(resin_conf_f,xms_num)
			else: # 如果可用内存大于3550就默认不修改，为默认的3550M
				if new_install is True:
					print """The current physical memory available on the computer is larger than the default physical memory of 3550M that we need to install Ecology, 
so the -xmx and -xms parameters of %s will remain the default 3550M without modification."""%resin_conf_f
				else:
					print """The current physical memory available on the computer is greater than the default physical memory of 3550M that we need to install Ecology, 
so the -xmx and -xms parameters for %s will be reset to 3550M.\n"""%resin_conf_f
					with open(resin_conf_f) as f:
						strs4 = f.read()
						xmx_list = re.findall(r'-Xmx(.+?)m',strs4)
						if len(xmx_list)>0:
							xmx_num = xmx_list[0]
							Modify_keywords(resin_conf_f,'<jvm-arg>-Xmx%sm</jvm-arg>'%xmx_num,'<jvm-arg>-Xmx3550m</jvm-arg>',tips[4])
					with open(resin_conf_f) as f:
						strs5 = f.read()
						xms_list = re.findall(r'-Xms(.+?)m',strs5)
						if len(xms_list)>0:
							xms_num = xms_list[0]
							Modify_keywords(resin_conf_f,'<jvm-arg>-Xms%sm</jvm-arg>'%xms_num,'<jvm-arg>-Xms3550m</jvm-arg>',tips[5])
			with open(resin_conf_f) as f:
				strs5 = f.read()
				app_http_list = re.findall(r'http address=.+\d"',strs5)
				#re.findall(r'javac compiler="(.+?)"',strs2)
				print 'Cheking http addres port:'
				if len(app_http_list)>0:
					p = re.sub("\D","",app_http_list[0])
					s_str = app_http_list[0]
					port_list_configuration.append(Modify_port(p,resin_conf_f,s_str,tips[8]))
			
			# 检查resin.conf中<server id="" address="127.0.0.1" port="6800"/>端口是否可用
			with open(resin_conf_f) as f:
				strs7 = f.read()
				app_servers_list = re.findall(r'server id="".+\d"',strs7)
				print 'Cheking hmux listening port:'
				if len(app_servers_list)>0:
					p = re.sub("\D","",app_servers_list[0][app_servers_list[0].rfind("port")+1:])
					s_str = 'server id="" address="127.0.0.1" port="%s"'%p
					# port_list_configuration.append(Modify_port(p,resin_conf_f,s_str,tips[9])) # 此端口不用加到防火墙
					Modify_port(p,resin_conf_f,s_str,tips[9])

			# 检查resin.conf中 <watchdog-port>6600</watchdog-port>中端口是否可用
			with open(resin_conf_f) as f:
				strs6 = f.read()
				watchdog_list = re.findall(r'<watchdog-port>(\d+)</watchdog-port>',strs6)
				print 'Cheking watchdog-port:'
				if len(watchdog_list)>0:
					p = watchdog_list[0]
					s_str = '<watchdog-port>%s</watchdog-port>'%p
					# port_list_configuration.append(Modify_port(p,resin_conf_f,s_str,tips[10]))  # 此端口不用加到防火墙
					Modify_port(p,resin_conf_f,s_str,tips[10])
			if len(port_list_configuration)>0:
				ports = ','.join(port_list_configuration)
				print 'Cheking the port %s is opened in your firewall...'%ports
				open_ports(port_list_configuration)
				print os.linesep
				print "Success!"
	else:
		print '%s does not exist!'%resin_conf_f
def Init_setup_Resin4(Ecology_dir,Resin_dir,JDK_dir,new_install = True):
	port_list_configuration=[]
	resin_bin = os.path.join(Resin_dir,'bin')
	resin_conf = os.path.join(Resin_dir,'conf')
	xml_name = os.path.join(Ecology_dir,'WEB-INF/resin-web.xml')
	# jdk_home = os.path.join(local_base_path,'jdk1.8.0_151')
	# ecology_dir = os.path.join(local_base_path,'ecology')

	httpd_f = os.path.join(resin_bin,'resin.sh')
	startresin_f = os.path.join(resin_bin,'startresin.sh')
	stopresin_f = os.path.join(resin_bin,'stopresin.sh')
	resin_xml = os.path.join(resin_conf,'resin.xml')
	resin_p = os.path.join(resin_conf,'resin.properties')

	tips = {1:' resin.sh',
			2:' startresin.sh',
			3:' stopresin.sh',
			4:' resin.properties\'s Xmx',
			5:' resin.properties\'s Xms',
			6:' resin.xml\'s #INSTALLDIR#ecology',
			7:' resin.xml\'s #INSTALLDIR#JDK',
			8:' resin.properties\'s app.http port',
			9:' resin.properties\'s app_servers port',
			10:' resin.xml\'s watchdog-port',
			11:' resinstart.bat'
	}

	print os.linesep
	# #给ecology，Resin和JDK授权
	print '[2]To grant authorization for ecology,Resin and JDK:'
	os.system("chmod 775 ./* -R")
	print 'Grant succeeded.'
	print os.linesep
	print '[3]Modify related configuration file:'
	# 修改startresin.sh,stopresin.sh,resin.sh
	# default_resin_path = r'/usr/weaver/resin/bin'
	# default_resin_path2 = r'/usr/weaver/Resin/bin'
	# default_jdk_home_path = r'/usr/weaver/jdk1.8.0_151'
	if os.path.exists(httpd_f):
		with open(httpd_f) as f:
			strs01 = f.read()
			java_home_list = re.findall(r'JAVA_HOME=.+\w',strs01)
			if len(java_home_list)>0:
				s_str = java_home_list[0]
				t_str = 'JAVA_HOME=%s'%JDK_dir
				Modify_keywords(httpd_f,s_str,t_str,tips[1])
	else:
		print '%s does not exist!'%httpd_f
	if os.path.exists(startresin_f):
		with open(startresin_f,'r+') as f:
			f.truncate()
			start_sh ='ulimit -n 65535\n'
			start_sh +='export LC_ALL=zh_CN.gbk\n'
			start_sh +='export LANG=zh_CN.gbk\n'
			start_sh +='%s start\n'%httpd_f
			f.write(start_sh)
			print 'The file "%s" has been Modified.'%startresin_f
	else:
		print '%s does not exist!'%startresin_f
	if os.path.exists(stopresin_f):
		with open(stopresin_f,'r+') as f:
			f.truncate()
			stop_sh ='%s stop\n'%httpd_f
			f.write(stop_sh)
			print 'The file "%s" has been Modified.'%stopresin_f
	else:
		print '%s does not exist!'%stopresin_f
	if os.path.exists(resin_xml):
		with open(resin_xml) as f:
			strs1 = f.read()
			Installation_ecology_list = re.findall(r'web-app id="/" root-directory="(.+?)"',strs1)
			if len(Installation_ecology_list)>0:
				Modify_keywords(resin_xml,Installation_ecology_list[0],Ecology_dir,tips[6])
		with open(resin_xml) as f:
			strs2 = f.read()
			Installation_jdk_list = re.findall(r'javac compiler="(.+?)"',strs2)
			if len(Installation_jdk_list)>0:
				Modify_keywords(resin_xml,Installation_jdk_list[0],'%s/bin/javac'%JDK_dir,tips[7])
	else:
		print '%s does not exist!'%resin_xml
	# 修改resin.conf下的内存参数，ecology目录
	if os.path.exists(resin_p):
		free = Meminfo()
		if free<2048: # 可用内存必须大于或等于2G
			print 'The available memory is %dM.Warning memory is too small,unable to configure!'%free
			print "Stop configuration!"
		else:
			resin_proposal_memo = int(free*0.5)
			if 1024 <= resin_proposal_memo <=5550: # 如果可用内存为2048到5550之间就可以配置一半可程序使用
				print 'The available memory is %dM.Do you continue to modify memory parameters?'%free
				print 'We recommend available memory is %dM,would like to change default 5550M?'%resin_proposal_memo
				choice = raw_input('Please choice(y:confirm/any other keys:cancel):').strip()
				if choice == 'y':
					# Modify_keywords(resin_conf_f,'<jvm-arg>-Xmx3550m</jvm-arg>','<jvm-arg>-Xmx%dm</jvm-arg>'%resin_proposal_memo,tips[4])
					# Modify_keywords(resin_conf_f,'<jvm-arg>-Xms3550m</jvm-arg>','<jvm-arg>-Xms%dm</jvm-arg>'%resin_proposal_memo,tips[5])
					with open(resin_p) as f:
						strs4 = f.read()
						xmx_list = re.findall(r'-Xmx(.+?)m',strs4)
						if len(xmx_list)>0:
							xmx_num = xmx_list[0]
							Modify_keywords(resin_p,'-Xmx%sm'%xmx_num,'-Xmx%dm'%resin_proposal_memo,tips[4])
					with open(resin_p) as f:
						strs5 = f.read()
						xms_list = re.findall(r'-Xms(.+?)m',strs5)
						if len(xms_list)>0:
							xms_num = xms_list[0]
							Modify_keywords(resin_p,'-Xms%sm'%xms_num,'-Xms%dm'%resin_proposal_memo,tips[5])
				else:
					with open(resin_p) as f:
						strs4 = f.read()
						xmx_list = re.findall(r'-Xmx(.+?)m',strs4)
						if len(xmx_list)>0:
							xmx_num = xmx_list[0]
							print 'The current parameters %s\'s Xmx is not modified, the default is "%sm".If you need to adjust them, please modify them manually later!'%(resin_p,xmx_num)
					with open(resin_p) as f:
						strs5 = f.read()
						xms_list = re.findall(r'-Xms(.+?)m',strs5)
						if len(xms_list)>0:
							xms_num = xms_list[0]
							print 'The current parameters %s\'s Xms is not modified, the default is "%sm".If you need to adjust them, please modify them manually later!'%(resin_p,xms_num)

			else: # 如果可用内存大于5550就默认不修改，为默认的5550M
				if new_install is True:
					print """The current physical memory available on the computer is larger than the default physical memory of 5550M that we need to install Ecology, 
so the -xmx and -xms parameters of %s will remain the default 5550M without modification."""%resin_p
				else:
					print """The current physical memory available on the computer is greater than the default physical memory of 5550M that we need to install Ecology, 
so the -xmx and -xms parameters for %s will be reset to 5550M.\n"""%resin_p
					with open(resin_p) as f:
						strs4 = f.read()
						xmx_list = re.findall(r'-Xmx(.+?)m',strs4)
						if len(xmx_list)>0:
							xmx_num = xmx_list[0]
							Modify_keywords(resin_p,'-Xmx%sm'%xmx_num,'-Xmx5550m',tips[4])
					with open(resin_p) as f:
						strs5 = f.read()
						xms_list = re.findall(r'-Xms(.+?)m',strs5)
						if len(xms_list)>0:
							xms_num = xms_list[0]
							Modify_keywords(resin_p,'-Xms%sm'%xms_num,'-Xms5550m',tips[5])
			# 检查修改resin.properties中app.http          : 8888端口是否可用
			with open(resin_p) as f:
				strs5 = f.read()
				app_http_list = re.findall(r'app.http.+\d',strs5)
				print 'Cheking app.http port:'
				if len(app_http_list)>0:
					for i in app_http_list:
						if i[:9] !='app.https':
							p = re.sub("\D","",i)
							s_str = 'app.http          : %s'%p
							port_list_configuration.append(Modify_port(p,resin_p,s_str,tips[8]))
			
			# 检查resin.properties中app_servers      : 127.0.0.1:6800 端口是否可用
			with open(resin_p) as f:
				strs7 = f.read()
				app_servers_list = re.findall(r'app_servers.+\d',strs7)
				print 'Cheking app_servers port:'
				if len(app_servers_list)>0:
					p = app_servers_list[0][app_servers_list[0].rfind(":")+1:]
					s_str = 'app_servers      : 127.0.0.1:%s'%p
					# port_list_configuration.append(Modify_port(p,resin_p,s_str,tips[9])) # 此端口不用加到防火墙
					Modify_port(p,resin_p,s_str,tips[9])

			# 检查resin.xml中 <watchdog-port>6600</watchdog-port>中端口是否可用
			if os.path.exists(resin_xml):
				with open(resin_xml) as f:
					strs6 = f.read()
					watchdog_list = re.findall(r'<watchdog-port>(\d+)</watchdog-port>',strs6)
					print 'Cheking watchdog-port:'
					if len(watchdog_list)>0:
						p = watchdog_list[0]
						s_str =  '<watchdog-port>%s</watchdog-port>'%p
						# port_list_configuration.append(Modify_port(p,resin_xml,s_str,tips[10])) # 此端口不用加到防火墙
						Modify_port(p,resin_xml,s_str,tips[10])
			ports = ','.join(port_list_configuration)
			# print 'Make sure the relevant %s are open in your firewall!'%ports
			if len(port_list_configuration)>0:
				print 'Cheking the port %s is opened in your firewall...'%ports
				open_ports(port_list_configuration)
				print os.linesep
				print "Success!"
	else:
		print '%s does not exist!'%resin_p
	ModifyXmlFile(xml_name)

def Get_character_info():
	print os.linesep
	output = os.popen('locale -a |grep zh_CN.gbk | wc -l')
	output1 = os.popen('locale -a |grep zh_CN.utf8 | wc -l')
	a = output.read().strip()
	b = output1.read().strip()
	if int(a) + int(b) < 1 :
		return False
	else :
		return True

# 开启相关端口
def open_ports(ports):
	os_version = re.sub("\D","",os.popen("cat /etc/redhat-release").read())[:1]
	if int(os_version) <=6: # Centos6
		ip_tables_status = os.popen('/etc/init.d/iptables status').readlines()
		if len(ip_tables_status) ==1:
			print 'Firewall not running! You do not need to operate the above ports!'
		else:
			print 'Firewall running...'
			for p in ports : 
				print 'Opening the port: %s'%p
				os.system("iptables -I INPUT -m tcp -p tcp --dport %s -j ACCEPT && service iptables reload"%p)
	else: # Centos7及以上版本
		(status, output) = commands.getstatusoutput('firewall-cmd --state')
		if status == 0:
			print 'Firewall running...'
			for p in ports : 
				print 'Opening the port: %s'%p
				os.system("firewall-cmd --permanent --zone=public --add-port=%s/tcp  && firewall-cmd --reload"%p)
#全新安装含解压
def New_installation():
	fpath = os.path.join(local_base_path,'ecology/Ecology_setup') # 如果使用初始安装脚本执行过就会生成此文件
	fpath_md5 = "%s.md5" % fpath

	resin_lib_home = os.path.join(local_base_path,'Resin4/lib')
	java_sh = os.path.join(local_base_path,'jdk1.8.0_151/bin/java')

	character_info = Get_character_info()
	if character_info:
		if os.path.exists(fpath_md5):
			with open(fpath_md5) as f:
				md5_value = f.readline().strip()
				if md5_value == 'd41d8cd98f00b204e9800998ecf8427e':
					print 'Ecology has been already initialized!'
		else:
			# 解压安装包
			if Unzip_file():
				Ecology_dir = os.path.join(local_base_path,'ecology')
				Resin_dir = os.path.join(local_base_path,'Resin4')
				JDK_dir = os.path.join(local_base_path,'jdk1.8.0_151')
				resin_conf = os.path.join(Resin_dir,'conf')
				if check_Resin_version(resin_conf):
					Init_setup_Resin4(Ecology_dir,Resin_dir,JDK_dir,new_install = True)
				else:
					Init_setup_Resin3(Ecology_dir,Resin_dir,JDK_dir,new_install = True)
				generate_file_md5sumFile(fpath)
			else:
				print 'There are no "Ecology,JDK,Resin" compressed packages in the current directory！\n'
	else:
		print 'The operating system needs to be set to zh_CN.gbk, or ZH_CN.utf8 !!!\n'
def get(msg,default):
	r=raw_input(msg).strip()
	if r=="":
		return default
	return r
#仅配置
def To_configure():
	print "[1]Please enter the relevant Ecology,Resin and JDK directory:(If you don't need to change it, just hit enter)"
	while True:
		Ecology_dir_default = os.path.join(local_base_path,'ecology')
		# Ecology_dir = raw_input('Please input the full path of "Ecology"(For example,/usr/weaver/ecology):').strip()
		msg = 'Please input the full path of "Ecology"(The default path:%s):'%Ecology_dir_default
		Ecology_dir = get(msg,Ecology_dir_default)
		if not os.path.exists(Ecology_dir):
			print 'The directory "%s" does not exist, please re-enter the correct directory!'%Ecology_dir
		else:
			break
	while True:
		Resin_dir_default = os.path.join(local_base_path,'Resin4')
		msg = 'Please input the full path of "Resin"(The default path:%s):'%Resin_dir_default
		Resin_dir = get(msg,Resin_dir_default)
		if not os.path.exists(Resin_dir):
			print 'The directory "%s" does not exist, please re-enter the correct directory!'%Resin_dir
		else:
			break
	while True:
		JDK_dir_default = os.path.join(local_base_path,'jdk1.8.0_151')
		msg = 'Please input the full path of "JDK"(The default path:%s):'%JDK_dir_default
		JDK_dir = get(msg,JDK_dir_default)
		if not os.path.exists(JDK_dir):
			print 'The directory "%s" does not exist, please re-enter the correct directory!'%JDK_dir
		else:
			break
	print '\n'
	try:
		character_info = Get_character_info()
		if character_info:
			resin_conf = os.path.join(Resin_dir,'conf')
			if check_Resin_version(resin_conf):
				Init_setup_Resin4(Ecology_dir,Resin_dir,JDK_dir,new_install = False)
			else:
				Init_setup_Resin3(Ecology_dir,Resin_dir,JDK_dir,new_install = False)
		else:
			print 'OS character set :gbk and utf8 are not installed !!!'
			print 'The current operating system character set must be zh_cn.utf-8'
	except KeyboardInterrupt:
		print os.linesep
		print 'You have forcibly stopped!'
		time.sleep(1)
		print os.linesep

def Read_Resin3_info(Resin_dir):
	resin_bin = os.path.join(Resin_dir,'bin')
	resin_conf = os.path.join(Resin_dir,'conf')
	# jdk_home = os.path.join(local_base_path,'jdk1.8.0_151')
	# ecology_dir = os.path.join(local_base_path,'ecology')

	httpd_f = os.path.join(resin_bin,'httpd.sh')
	startresin_f = os.path.join(resin_bin,'startresin.sh')
	stopresin_f = os.path.join(resin_bin,'stopresin.sh')
	resin_conf_f = os.path.join(resin_conf,'resin.conf')

	tips = {1:' httpd.sh',
			2:' startresin.sh',
			3:' stopresin.sh',
			4:' resin.conf\'s Xmx',
			5:' resin.conf\'s Xms',
			6:' resin.conf\'s #INSTALLDIR#ecology',
			7:' resin.conf\'s javac compiler directory',
			8:' resin.conf\'s http listening port',
			9:' resin.conf\'s hmux listening port',
			10:' resin.conf\'s watchdog-port'
	}

	print '[2]Reading related file configuration parameters:'
	if os.path.exists(httpd_f):
		print 'Reading configuration file:%s'%httpd_f
		with open(httpd_f) as f:
			strs01 = f.read()
			java_home_list = re.findall(r'JAVA_HOME=.+\w',strs01)
			if len(java_home_list)>0:
				s_str = java_home_list[0]
				print s_str
	if os.path.exists(startresin_f):
		print 'Reading configuration file:%s'%startresin_f
		with open(startresin_f) as f:
			lines = f.read()
			print lines
	if os.path.exists(stopresin_f):
		print 'Reading configuration file:%s'%stopresin_f
		with open(stopresin_f,) as f:
			lines = f.read()
			print lines
	if os.path.exists(resin_conf_f):
		print 'Reading configuration file:%s'%resin_conf_f
		with open(resin_conf_f) as f:
			strs1 = f.read()
			Installation_ecology_list = re.findall(r'web-app id="/" root-directory="(.+?)"',strs1)
			if len(Installation_ecology_list)>0:
				print 'web-app id="/" root-directory="%s"'%Installation_ecology_list[0]
		with open(resin_conf_f) as f:
			strs2 = f.read()
			Installation_jdk_list = re.findall(r'javac compiler="(.+?)"',strs2)
			if len(Installation_jdk_list)>0:
				print '<javac compiler="%s" args="-encoding UTF-8"/>'%Installation_jdk_list[0]

		with open(resin_conf_f) as f:
			strs4 = f.read()
			xmx_list = re.findall(r'-Xmx(.+?)m',strs4)
			if len(xmx_list)>0:
				xmx_num = xmx_list[0]
				print '<jvm-arg>-Xmx%sm</jvm-arg>'%xmx_num
		with open(resin_conf_f) as f:
			strs5 = f.read()
			xms_list = re.findall(r'-Xms(.+?)m',strs5)
			if len(xms_list)>0:
				xms_num = xms_list[0]
				print '<jvm-arg>-Xms%sm</jvm-arg>'%xms_num
		print 'Reading http addres port:'
		with open(resin_conf_f) as f:
			strs5 = f.read()
			app_http_list = re.findall(r'http address=.+\d"',strs5)
			#re.findall(r'javac compiler="(.+?)"',strs2)
			if len(app_http_list)>0:
				p = re.sub("\D","",app_http_list[0])
				print '<http address="*" port="%s"/>'%p
				http_port = p
		
		# 检查resin.conf中<server id="" address="127.0.0.1" port="6800"/>端口是否可用
		print 'Reading hmux listening port:'
		with open(resin_conf_f) as f:
			strs7 = f.read()
			app_servers_list = re.findall(r'server id="".+\d"',strs7)
			if len(app_servers_list)>0:
				p = re.sub("\D","",app_servers_list[0][app_servers_list[0].rfind("port")+1:])
				print '<server id="" address="127.0.0.1" port="%s"/>'%p

		# 检查resin.conf中 <watchdog-port>6600</watchdog-port>中端口是否可用
		print 'Reading watchdog-port:'
		with open(resin_conf_f) as f:
			strs6 = f.read()
			watchdog_list = re.findall(r'<watchdog-port>(\d+)</watchdog-port>',strs6)
			if len(watchdog_list)>0:
				p = watchdog_list[0]
				print '<watchdog-port>%s</watchdog-port>'%p
		print os.linesep
		print "[3]If the configuration is correct, after Resin service is successfully launched.Please input http://ip:%s in the browser to access OA system.\n"%http_port

def Read_Resin4_info(Resin_dir):
	resin_bin = os.path.join(Resin_dir,'bin')
	resin_conf = os.path.join(Resin_dir,'conf')
	# jdk_home = os.path.join(local_base_path,'jdk1.8.0_151')
	# ecology_dir = os.path.join(local_base_path,'ecology')

	httpd_f = os.path.join(resin_bin,'resin.sh')
	startresin_f = os.path.join(resin_bin,'startresin.sh')
	stopresin_f = os.path.join(resin_bin,'stopresin.sh')
	resin_xml = os.path.join(resin_conf,'resin.xml')
	resin_p = os.path.join(resin_conf,'resin.properties')

	tips = {1:' resin.sh',
			2:' startresin.sh',
			3:' stopresin.sh',
			4:' resin.properties\'s Xmx',
			5:' resin.properties\'s Xms',
			6:' resin.xml\'s #INSTALLDIR#ecology',
			7:' resin.xml\'s #INSTALLDIR#JDK',
			8:' resin.properties\'s app.http port',
			9:' resin.properties\'s app_servers port',
			10:' resin.xml\'s watchdog-port',
			11:' resinstart.bat'
	}

	print '[2]Reading related file configuration parameters:'
	# 修改startresin.sh,stopresin.sh,resin.sh
	# default_resin_path = r'/usr/weaver/resin/bin'
	# default_resin_path2 = r'/usr/weaver/Resin/bin'
	# default_jdk_home_path = r'/usr/weaver/jdk1.8.0_151'
	if os.path.exists(httpd_f):
		print 'Reading configuration file:%s'%httpd_f
		with open(httpd_f) as f:
			strs01 = f.read()
			java_home_list = re.findall(r'JAVA_HOME=.+\w',strs01)
			if len(java_home_list)>0:
				s_str = java_home_list[0]
				print s_str
	if os.path.exists(startresin_f):
		print 'Reading configuration file:%s'%startresin_f
		with open(startresin_f) as f:
			lines = f.read()
			print lines
	if os.path.exists(stopresin_f):
		print 'Reading configuration file:%s'%stopresin_f
		with open(stopresin_f,) as f:
			lines = f.read()
			print lines
	if os.path.exists(resin_xml):
		print 'Reading configuration file:%s'%resin_xml
		with open(resin_xml) as f:
			strs1 = f.read()
			Installation_ecology_list = re.findall(r'web-app id="/" root-directory="(.+?)"',strs1)
			if len(Installation_ecology_list)>0:
				print 'web-app id="/" root-directory="%s"'%Installation_ecology_list[0]
		with open(resin_xml) as f:
			strs2 = f.read()
			Installation_jdk_list = re.findall(r'javac compiler="(.+?)"',strs2)
			if len(Installation_jdk_list)>0:
				print '<javac compiler="%s" args="-encoding UTF-8"/>'%Installation_jdk_list[0]
	if os.path.exists(resin_p):
		print 'Reading configuration file:%s'%resin_p
		with open(resin_p) as f:
			strs4 = f.read()
			xmx_list = re.findall(r'-Xmx(.+?)m',strs4)
			if len(xmx_list)>0:
				xmx_num = xmx_list[0]
		with open(resin_p) as f:
			strs5 = f.read()
			xms_list = re.findall(r'-Xms(.+?)m',strs5)
			if len(xms_list)>0:
				xms_num = xms_list[0]
		print 'jvm_args  : -Xmx%sm -Xms%sm'%(xmx_num,xms_num)

		# 检查修改resin.properties中app.http          : 8888端口是否可用
		print 'Reading app.http port:'
		with open(resin_p) as f:
			strs5 = f.read()
			app_http_list = re.findall(r'app.http.+\d',strs5)
			if len(app_http_list)>0:
				for i in app_http_list:
					if i[:9] !='app.https':
						p = re.sub("\D","",i)
						s_str = 'app.http          : %s'%p
						print s_str
						http_port = p
		
		# 检查resin.properties中app_servers      : 127.0.0.1:6800 端口是否可用
		print 'Reading app_servers port:'
		with open(resin_p) as f:
			strs7 = f.read()
			app_servers_list = re.findall(r'app_servers.+\d',strs7)
			if len(app_servers_list)>0:
				p = app_servers_list[0][app_servers_list[0].rfind(":")+1:]
				s_str = 'app_servers      : 127.0.0.1:%s'%p
				# port_list_configuration.append(Modify_port(p,resin_p,s_str,tips[9])) # 此端口不用加到防火墙
				print s_str
	if os.path.exists(resin_xml):
		print 'Reading watchdog-port:'
		# 检查resin.xml中 <watchdog-port>6600</watchdog-port>中端口是否可用
		with open(resin_xml) as f:
			strs6 = f.read()
			watchdog_list = re.findall(r'<watchdog-port>(\d+)</watchdog-port>',strs6)
			if len(watchdog_list)>0:
				p = watchdog_list[0]
				s_str =  '<watchdog-port>%s</watchdog-port>'%p
				# port_list_configuration.append(Modify_port(p,resin_xml,s_str,tips[10])) # 此端口不用加到防火墙
				print s_str
		print os.linesep
		print "[3]If the configuration is correct, after Resin service is successfully launched.Please input http://ip:%s in the browser to access OA system.\n"%http_port

def Read_configure():
	print "[1]Please enter the relevant Resin\'s directory:(If you don't need to change it, just hit enter)"
	# while True:
	# 	Ecology_dir = raw_input('Please input the full path of "Ecology"(For example,/usr/weaver/ecology):').strip()
	# 	if not os.path.exists(Ecology_dir):
	# 		print 'The "ecology" directory you entered does not exist, please re-enter the correct directory!'
	# 	else:
	# 		break
	while True:
		Resin_dir_default = os.path.join(local_base_path,'Resin')
		msg = 'Please input the full path of "Resin"(The default path:%s):'%Resin_dir_default
		Resin_dir = get(msg,Resin_dir_default)
		if not os.path.exists(Resin_dir):
			print 'The directory "%s" does not exist, please re-enter the correct directory!'%Resin_dir
		else:
			break
	# while True:
	# 	JDK_dir = raw_input('Please input the full path of "JDK"(For example,/usr/weaver/jdk1.8.0_151):').strip()
	# 	if not os.path.exists(JDK_dir):
	# 		print 'The "JDK" directory you entered does not exist, please re-enter the correct directory!'
	# 	else:
	# 		break
	print '\n'
	try:
		# resin_lib_home = os.path.join(Resin_dir,'lib')
		# java_sh = os.path.join(JDK_dir,'bin/java')
		# r_version = check_Resin_version(resin_lib_home,java_sh)
		# if 'Resin-3.1.8' in r_version:
		# 	Read_Resin3_info(Resin_dir)
		# else:
		# 	Read_Resin4_info(Resin_dir)
		resin_conf = os.path.join(Resin_dir,'conf')
		if check_Resin_version(resin_conf):
			Read_Resin4_info(Resin_dir)
		else:
			Read_Resin3_info(Resin_dir)
	except KeyboardInterrupt:
		print os.linesep
		print 'You have forcibly stopped!'
		time.sleep(1)
		print os.linesep
def main():
	print 'Welcome to use Ecology Automatic Configuration tool'.center(60,'*')
	# user = os.popen('whoami').readline().strip()
	# now =datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
	# print 'Current User: %s'%user,'Date: %s'.ljust(80,' ')%now
	print os.linesep
	print 'Notice'.center(80,'=')
	print """
[1]This software is written in Python, and there is no infringement of third-party software.
[2]Function description:
1: Make sure the "unzip" and "tar" commands are available on the server.
2: The installation file has been extracted and can be configured according to the specified directory.
3: Means to view relevant configured parameters.
[3]Assume the responsibility for the downtime of OA or other software services caused by malicious cracking, decompression and modification of the software.
"""
	print os.linesep
	while True:
		menu = {1:'New installation',2:'Configuration parameters only',3:'Check the parameters',4:'Exit'}
		print 'Please select according to the number'.center(50,'*')
		for k,v in menu.items():
			print str(k)+':'+v
		try:
			choice = raw_input('Please input:').strip()
			if choice.isdigit():
				choice = int(choice)
				if choice in menu.keys():
					if choice ==1:
						m_choice = menu[choice]
						print  'You select the "%s"\n'%m_choice
						New_installation()
					elif choice ==2:
						m_choice = menu[choice]
						print  'You select the "%s"\n'%m_choice
						To_configure()
					elif choice ==3:
						m_choice = menu[choice]
						print  'You select the "%s"\n'%m_choice
						Read_configure()
					elif choice ==4:
						m_choice = menu[choice]
						# print  'You select the "%s"'%m_choice
						sys.exit(0)
				else:
					print "I'm sorry, but we don't have that option right now"
			else:
				print 'The input is incorrect. You must enter a number!'
		except Exception as e:
			print e
if __name__ == '__main__':
    main()