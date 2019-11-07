#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from install.install import install_neovim_linux
from install.install import install_neovim_windows
from install.var import var_neovim_linux
from install.var import var_neovim_windows
import sys


if __name__ == '__main__':
    if sys.platform.startswith('linux'):
        global_var = var_neovim_linux()
        install_neovim_linux(global_var)
    elif sys.platform.startswith('win32'):
        global_var = var_neovim_windows()
        install_neovim_windows(global_var)
    else:
        print('The platform '+ sys.platform() + 'is not suported')

    

