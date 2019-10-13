#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from shutil import copyfile

from .install_bin import install_neovim
from .install_conf import install_conf
from .install_pack import install_pack

def install(var):
    """
    Install neovim
    """
    install_neovim(var)
    install_conf(var)
    install_pack(var)
    copy_utility_file(var)


def copy_utility_file(var):
    """
    Copy utility script into the binary directory
    """
    copyfile(var.install_dir_src / 'var.py',var.bin_dir_path / 'var.py')
    for utility in var.utility_dir.iterdir():
        copyfile(utility,var.bin_dir_path / utility.name)
