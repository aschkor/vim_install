import os
import git
from pathlib import Path

class pack:
    """
    Represente information over a vim plugin
    """
    def __init__(self,author,repo,options,pack_dir):
        """
        Initialze information ovec a pack
        """
        self.url = 'https://github.com/'+author+'/'+repo
        self.name = repo
        self.options = options
        self.pack_dir = self.format_path(pack_dir)

    def format_path (self,pack_dir):
        """
        Isolate the plugin description path to respecte
        the directory hierarchy of plugins in the pack directory
        """
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
    """
    Install all packs
    """
    packs_parameters = get_pack_parameters(var.descr_file_pack_path)
    if packs_parameters == None:
        return

    for pack_parameters in packs_parameters:
        pack_dir = var.pack_dir/pack_parameters.pack_dir
        repo_dir = pack_dir/pack_parameters.name
        print (pack_dir)
        print (repo_dir)
        if(not repo_dir.exists()):
            """update_pack(git.Remote(repo_dir))"""
            pack_dir.mkdir(0o740,True,True)
            clone_pack(pack_parameters.url,git.Git(pack_dir),repo_dir)

    write_packs_option(packs_parameters,var)


def get_pack_parameters(pack_file_dir):
    """
    Read a description pach file and return structured information on him
    """
    packs_parameters = []
    for pack_file_path in pack_file_dir.glob('**/*'):
        if pack_file_path.is_file():
            pack_parameters = pack_file_path.read_text().split('\n')
            url = pack_parameters[0].split('/')
            packs_parameters.append(pack(url[0],url[1],get_parameter_options(pack_parameters),pack_file_path.parent))

    if(len(packs_parameters) > 0):
        return packs_parameters
    return None


def get_parameter_options(pack_file_content):
    """
    Read facultatif option in a desccription pack file
    """
    if len(pack_file_content) < 1:
        return None

    option_pack = pack_file_content.copy()
    option_pack.pop(0)
    return option_pack


def update_pack(repo):
    """
    Update the pack
    """
    repo.pull()


def clone_pack(url,repo,repo_dir):
    """
    Downlaod pack with a git client
    """
    repo.clone(url,repo_dir)


def write_packs_option(packs_parameters,var):
    """
    Write packs option in configuration file
    """
    options = get_packs_options_content(packs_parameters)

    if len(options) > 0:
        pack_option_conf_file = var.conf_path / 'pack_option.vim'
        add_pack_option_file_to_conf_file(var.conf_file_path,pack_option_conf_file)
        write_packs_options_conf_file(options,pack_option_conf_file)


def add_pack_option_file_to_conf_file(main_conf_file_path,pack_options_file_path):
    """
    Add the path to the pack configuration file on the main configuration file
    """
    f = main_conf_file_path.open('a')
    f.write('source '+str(pack_options_file_path) + '\n')
    f.close()


def get_packs_options_content(packs_parameters):
    """
    Generate content of pack configuration file
    """
    options = ""
    for pack_parameter in packs_parameters:
        if pack_parameter != None:
            for option in pack_parameter.options:
                options += option+'\n'
            options+='\n'
    return options


def write_packs_options_conf_file(options, file_path):
    """
    Write the packs configuration file
    """
    file_path.write_text(options)
