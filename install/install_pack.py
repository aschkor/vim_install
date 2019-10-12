import os
import git
from pathlib import Path

class pack:
    def __init__(self,url,options,pack_dir):
        self.url = 'https://github.com/'+url
        self.options = options
        self.pack_dir = self.format_path(pack_dir)

    def format_path (self,pack_dir):
        part = pack_dir.parts
        is_end_path = False
        res = Path() 
        
        for p in part:
            if is_end_path:
                res = res / p
            elif p == 'pack':
                is_end_path = True

        return res


def install_pack(var):
    packs_parameters = get_pack_parameters(var.descr_file_pack_path)
    if packs_parameters == None:
        return


    clone_packs(packs_parameters,var.pack_dir)
    write_packs_option(packs_parameters,var)


def get_pack_parameters(pack_file_dir):
    packs_parameters = []
    for pack_file_path in pack_file_dir.glob('**/*'):
        if pack_file_path.is_file():
            pack_parameters = pack_file_path.read_text().split('\n')
            packs_parameters.append(pack(pack_parameters[0],get_parameter_options(pack_parameters),pack_file_path.parent))

    if len(packs_parameters) > 0:
        return packs_parameters
    return None


def get_parameter_options(pack_file_content):
    if len(pack_file_content) < 1:
        return None

    option_pack = pack_file_content.copy()
    option_pack.pop(0)
    return option_pack

def clone_packs(packs_parameters,packs_dir):
    for pack_parameters in packs_parameters:
        pack_dir =packs_dir/pack_parameters.pack_dir 
        pack_dir.mkdir(0o777,True,True)
        git.Git(pack_dir).clone(pack_parameters.url)

def write_packs_option(packs_parameters,var):
    options = get_packs_options_content(packs_parameters)

    if len(options) > 0:
        pack_option_conf_file = var.conf_path / 'pack_option.vim'
        add_pack_option_file_to_conf_file(var.conf_file_path,pack_option_conf_file)
        write_packs_options_conf_file(options,pack_option_conf_file)



def add_pack_option_file_to_conf_file(main_conf_file_path,pack_options_file_path):
    f = main_conf_file_path.open('a')
    f.write('source '+str(pack_options_file_path) + '\n')
    f.close()


def get_packs_options_content(packs_parameters):
    options = "" 
    for pack_parameter in packs_parameters:
        if pack_parameter != None:
            for option in pack_parameter.options:
                options += option+'\n'
            options+='\n'
    return options


def write_packs_options_conf_file(options, file_path):
    file_path.write_text(options)
