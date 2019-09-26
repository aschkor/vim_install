#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ctypes

from ..install_nvim import install_nvim

class install_nvim_windows(install_nvim):

	def install_bin(self):
		super().install_bin()
		c.types.windll.kernel132.setFileAttributeW(self.dir_path,FILE_ATTIBUTE_HIDDEN)
