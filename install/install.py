#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import platform

from .install_bin import install_neovim_linux_bin
from .install_bin import install_neovim_windows_bin
from .install_conf import install_conf
from .install_pack import install_pack


def install_neovim_linux(var):
    """
    Install neovim on linux
    """
    is_32bit_system = platform.architecture()[0] == '32bit'

    install_neovim_linux_bin(var,is_32bit_system)
    install_conf(var)
    install_pack(var)

    if(not is_32bit_system):
        copy_utility_file(var)


def install_neovim_windows(var):
    """
    Install neovim on windows
    """
    install_neovim_windows_bin(var)
    install_conf(var)
    install_pack(var)
    copy_utility_file(var)


def copy_utility_file(var):
    """
    Copy utility script into the binary directory
    """
    print(var.install_dir_src / 'var.py')
    print(var.utility_file_dir / 'var.py')
    (var.utility_file_dir / 'var.py').write_text((var.install_dir_src / 'var.py').read_text())
    for utility in var.utility_dir.iterdir():
        (var.utility_file_dir / utility.name).write_text(utility.read_text())
