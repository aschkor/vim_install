#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

from install.install import install
from install.var import var_neovim


def parse():
    parser =argparse.ArgumentParser(description='Install vim or neovim with packages as user')
    parser.add_argument('soft', help = 'choose vim or neovim to install')
    return parser.parse_args()


if __name__ == '__main__':
    
    parser = parse()
    
    if parser.soft == 'neovim':
        global_var = var_neovim()
        install(global_var)
    elif parser.soft == 'vim':
        pass


