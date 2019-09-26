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


	def sys_shortcut(self):
		bashrc = os.path.join(Path.home(),'.bashrc')
		f=open(bashrc,"a+")
		f.write('alias nvim=\''+self.app_path+'\'\n')
		f.close()


	def install_bin(self):
		super().install_bin()
		self.sys_shortcut()
