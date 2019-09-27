#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from install.neovim.linux.install_nvim_linux import install_nvim_linux
from install.neovim.windows.install_nvim_windows import install_nvim_windows

import os

if __name__ == "__main__":
	is_linux = os.name == 'posix'
	is_windows = os.name == 'nt'

	install = None

	if is_linux:
		install = install_nvim_linux()
	elif is_windows:
		install = install_nvim_windows()

	install.init_dir()
	install.install_bin()
	install.install_pymodul()
	install.add_del_script()
	install.copy_conf_file()
	install.write_init_file()
