#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from install.install import install
from install.var import var_neovim

if __name__ == '__main__':
    global_var = var_neovim()
    install(global_var)

