#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from shutil import copyfile

from .install_bin import install_neovim
from .install_conf import install_conf
from .install_pack import install_pack

def install(var):
    install_neovim(var)
    install_conf(var)
    install_pack(var)
    copy_utility_file(var)


def copy_utility_file(var):

    copyfile(var.install_dir_src / 'var.py',var.bin_dir_path / 'var.py')
    for utility in var.utility_dir.iterdir():
        copyfile(utility,var.bin_dir_path / utility.name)
    

#def install_bin(neovim_var):
#
#    class install:
#
#        def __init__(self,dir_path,app_name,remove_script_path,init_vim_dir,pack_dir):
#            self.dir_path = dir_path
#                self.app_name = app_name
#                self.url = 'https://github.com/neovim/neovim/releases/download/v0.4.2/nvim.appimage'
#                self.extension = ".appimage"
#                self.pymodul_name = 'neovim'
#                self.remove_script_path = remove_script_path
#                self.app_path = os.path.join(self.dir_path,self.app_name+self.extension)
#                self.script_path = Path(os.path.dirname(sys.argv[0]))
#                self.conf_dir = os.path.join(self.script_path,'install','res')
#                self.init_vim_dir = init_vim_dir
#                self.pack_dir = pack.dir
#
#        def init_dir(self):
#            pass
#
#
#        def install_bin(self):
#            pass
#
#
#        def install_pymodul(self):
#            pass
#
#
#        def add_del_script(self):
#            pass
#
#
#        def read_file(self,file_path):
#            content = []
#                fr = open(file_path,'r')
#
#                while True:
#                    line=fr.readline()
#                        if len(line) == 0:
#                            break
#                        content.append(line)
#                fr.close()
#
#                return content
#
#
#
#
#        def add_del_script(self):
#            remove = os.path.join(self.script_path,'install','neovim','remove')
#                remove_path =os.path.join(self.script_path,'install','neovim','linux','remove') 
#
#                mark_function = '@remove_path'
#                mark_dir_path = '@dir_path'
#                mark_app_path = '@app_path'
#                mark_conf_path = '@conf_path'
#
#                remove_path_dir = os.path.join(self.dir_path,'remove.py')
#                remove_path_content = self.read_file(remove_path)
#                remove_content = self.read_file(remove)
#                file_content =[]
#
#                for line in remove_content:
#                    if mark_function in line :
#                        for line_p in remove_path_content:
#                            file_content.append(line_p)
#                        elif mark_dir_path in line:
#                            file_content.append('	dir_path = \''+self.dir_path+'\'\n')
#                        elif mark_app_path in line:
#                            file_content.append('	app_path = \''+self.app_path+'\'\n')
#                        elif mark_conf_path in line:
#                            file_content.append('	conf_path = \''+self.init_vim_dir+'\'\n')
#                        else:
#                            file_content.append(line)
#                self.write_file(remove_path_dir,file_content)
#
#
#
#
