#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from shutil import copyfile

class install:

	def __init__(self,dir_path,app_name,remove_script_path):
		self.dir_path = dir_path
		self.app_name = app_name
		self.url = 'https://github.com/neovim/neovim/releases/download/v0.4.2/nvim.appimage'
		self.extension = ".appimage"
		self.pymodul_name = 'neovim'
		self.remove_script_path = remove_script_path
		self.app_path = os.path.join(self.dir_path,self.app_name+self.extension)
		self.script_path = os.path.abspath(os.path.dirname(sys.argv[0]))
		self.conf_dir = os.path.join(self.script_path,'install','res')

	def init_dir(self):
		pass


	def install_bin(self):
		pass


	def install_pymodul(self):
		pass


	def add_del_script(self):
		pass


	def read_file(self,file_path):
		content = []
		fr = open(file_path,'r')

		while True:
				line=fr.readline()
				if len(line) == 0:
						break
				content.append(line)
		fr.close()

		return content


	def write_file(self,file_path,content):
			f = open(file_path,'w+')
			for line in content:
				f.write(line)


	def add_del_script(self):
			remove = os.path.join(self.script_path,'install','neovim','remove')
			remove_path =os.path.join(self.script_path,'install','neovim','linux','remove') 

			mark_function = '@remove_path'
			mark_dir_path = '@dir_path'
			mark_app_path = '@app_path'

			remove_path_dir = os.path.join(self.dir_path,'remove.py')
			remove_path_content = self.read_file(remove_path)
			remove_content = self.read_file(remove)
			file_content =[]

			for line in remove_content:
				if mark_function in line :
					for line_p in remove_path_content:
						file_content.append(line_p)
				elif mark_dir_path in line:
					file_content.append('	dir_path = \''+self.dir_path+'\'\n')
				elif mark_app_path in line:
					file_content.append('	app_path = \''+self.app_path+'\'\n')
				else:
					file_content.append(line)
			self.write_file(remove_path_dir,file_content)


	def copy_conf_file(self):
		files_list = os.listdir(self.conf_dir)
		for f in files_list:
			res_file =os.path.join(self.conf_dir,f) 
			conf_file =os.path.join(self.dir_path,f) 
			copyfile(res_file,conf_file)

	def get_init_content(self):
		files_list = os.listdir(self.conf_dir)
		content = []
		for f in files_list:
			content.append('source ')
			content.append(os.path.join(self.dir_path,f))
			content.append('\n')
		return content


