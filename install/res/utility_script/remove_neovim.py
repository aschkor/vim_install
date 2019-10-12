import shutil
from var import var_neovim
from pathlib import Path
from pip._internal import main

def remove_conf(config_path):
    """
    Remove configuration files
    """
    if config_path.exists():
        shutil.rmtree(config_path)


def remove_data(data_dir):
    """
    Remove all data
    """
    if data_dir.exists():
        shutil.rmtree(data_dir)


def remove_bin(bin_dir):
    """
    Remove binary
    """
    if bin_dir.exists():
        shutil.rmtree(bin_dir)


def remove_nvim_alias(content,app_path):
    """
    Remove alias nvim
    """
    alias = 'alias nvim=\''+str(app_path)+'\''
    res_content = '' 
    for line in content:
        if line != alias:
            res_content+=line+'\n'
    return res_content


def remove_path(app_path):
    """
    Remove alias nvim in the bashcr file
    """
    bashrc_path = Path.home()/'.bashrc'
    bashrc_content = remove_nvim_alias(bashrc_path.read_text().split('\n'),app_path)
    bashrc_path.write_text(bashrc_content)


def remove_py_module():
    main(["uninstall","--yes","neovim"])


def remove_neovim(var):
    """
    Remove neovim and its files
    """
    remove_conf(var.conf_path)
    remove_data(var.user_data_dir)
    remove_py_module()
    remove_path(var.bin_path)
    remove_bin(var.bin_dir_path)


if __name__ == "__main__":
    var = var_neovim()
    remove_neovim(var)
