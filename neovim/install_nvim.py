#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import stat
import os
import shutil
from pip._internal import main
from pathlib import Path
is_linux = os.name == 'posix'
is_windows = os.name == 'nt'


def init_directory():
	print('init directory')

	dir_name = "neovim"
	if is_linux:
		dir_name = '.'+dir_name

	dir_path =  os.path.join(Path.home(),dir_name)
	os.mkdir(dir_path)
	if is_windows:
		import ctypes
		c.types.windll.kernel132.setFileAttributeW(dir_path,FILE_ATTIBUTE_HIDDEN)
	return dir_path


def install_python(dir_path):
	
	print ('dowlaod and install neovim')
	url ='https://github.com/neovim/neovim/releases/download/nightly/nvim.appimage'
	app_extention = '.appimage'
	app_name = 'neovim'
	app_path = os.path.join(dir_path,app_name+app_extention)

	urllib.request.urlretrieve(url,app_path)

	os.chmod(app_path,stat.S_IRUSR | stat.S_IXUSR | stat.S_IWUSR| stat.S_IRGRP | stat.S_IROTH)

	main(["install","--user",app_name])
	return app_path

def config_sys_path(app_path):
	print('configure systeme path')
	
	if is_linux:
		bashrc = os.path.join(Path.home(),'.bashrc')
		f=open(bashrc,"a+")
		f.write('alias nvim=\''+app_path+'\'\n')
		f.close()

def remove_install(dir_path,app_name):
	if is_linux:
		shutil.rmtree(dir_path)
	main(["uninstall",'--yes',app_name])

def remove_sys_path(app_path):
	if is_linux:
		bashrc = os.path.join(Path.home(),'.bashrc')
		file_content = []
		fr =open(bashrc,'r')
		
		while True:
			line=fr.readline()
			if len(line) == 0:
				break
			alias = 'alias nvim=\''+app_path+'\'\n'
			if line != alias:
				file_content.append(line)

		fr.close
		os.remove(bashrc)
		
		fw =open(bashrc,'a')

		for line in file_content:
			fw.write(line)
		fw.close


def remove_nvim():

	print('removing nvim')
	app_name = 'neovim.appimage'
	dir_path = os.path.join(Path.home(),'.neovim')
	app_path = os.path.join(dir_path,'neovim.appimage')
	
	remove_install(dir_path,'neovim')
	remove_sys_path(app_path)
	
remove_nvim()
#path = init_directory()
#path = install_python(path)
#config_sys_path(path)
