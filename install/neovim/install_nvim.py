#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import stat
import os
import shutil

from pip._internal import main
from pathlib import Path

from ..install import install

class install_nvim(install):

	def __init__(self, dir_path ,app_name):
		remove_path = os.path.join(dir_path,'remove.py')
		super().__init__(dir_path,app_name,remove_path)
	def init_dir(self):
		os.mkdir(self.dir_path);

	def install_bin(self):
		urllib.request.urlretrieve(self.url,self.app_path)
		os.chmod(self.app_path,stat.S_IRUSR | stat.S_IXUSR | stat.S_IWUSR| stat.S_IRGRP | stat.S_IROTH)

	def install_pymodul(self):
		main(["install","--user",self.pymodul_name])
