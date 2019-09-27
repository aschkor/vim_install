#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
from pathlib import Path

from ..install_nvim import install_nvim

class install_nvim_linux(install_nvim):


	def __init__(self,app_name = 'neovim',dir_name = 'neovim' ,dir_path = str(Path.home())):
		hidden_dir_path = os.path.join(dir_path,'.'+dir_name)
		super().__init__(hidden_dir_path,app_name)
		self.init_vim_dir = os.path.join(Path.home(),'.config','nvim') 


	def sys_shortcut(self):
		bashrc = os.path.join(Path.home(),'.bashrc')
		f=open(bashrc,"a+")
		f.write('alias nvim=\''+self.app_path+'\'\n')
		f.close()


	def install_bin(self):
		super().install_bin()
		self.sys_shortcut()


	def init_dir(self):
		super().init_dir()
		if not os.path.exists(self.init_vim_dir):
			os.mkdir(self.init_vim_dir)


	def write_init_file(self):
		content = self.get_init_content()
		self.write_file(os.path.join(self.init_vim_dir,'init.vim'),content)



