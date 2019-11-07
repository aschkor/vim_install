#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from shutil import copyfile

from .install_bin import install_neovim_linux_bin
from .install_bin import install_neovim_windows_bin
from .install_conf import install_conf
from .install_pack import install_pack


def install_neovim_linux(var):
    """
    Install neovim on linux
    """
    install_neovim_linux_bin(var)
    install_conf(var)
    install_pack(var)
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
    copyfile(var.install_dir_src / 'var.py', var.utility_file_dir / 'var.py')
    for utility in var.utility_dir.iterdir():
        copyfile(utility,var.utility_file_dir / utility.name)
