import pip
import urllib.request
from .var import var_neovim
from pathlib import Path
import zipfile
import os
import shutil


def install_bin_neovim_linux(var):
    """
    Downlaod neovim binary in the binary path on linux
    """
    var.bin_dir_path.mkdir(0o744,True,True)
    print(var.bin_url)
    print(var.bin_path)
    with urllib.request.urlopen(var.bin_url) as nvim:
        var.bin_path.write_bytes(nvim.read())
    var.bin_path.chmod(0o744)
    print("salope")


def install_bin_neovim_windows(var):
    """
    Downlaod neovim binary in the binary path on windows
    """
    var.bin_dir_path.mkdir(0o744,True,True)
    urllib.request.urlretrieve(var.bin_url,var.zip)
    with zipfile.ZipFile(var.zip,'r') as zip_ref:
        zip_ref.extractall(var.bin_dir_path)


def install_py_module():
    """
    Downlaod neovim python module
    """
    pip.main(['install','--user','neovim'])

def install_linux_syspath(bin_path):
    """
    Add alias to neovim binary in the bashrc
    """
    init_vim = Path.home() / '.bashrc'
    init_vim.write_text('alias nvim=\''+str(bin_path)+'\'\n')


def install_windows_syspath(bin_path):
    """
    Add bin path to PATH windows systeme variable
    """
    os.environ['Path'] += os.pathsep + str(bin_path)


def install_neovim_linux_bin(var,is_32bits):
    """
    Install neovim on Windows
    """

    if(is_32bits):
        print('appimage not available on 32bits systeme, install neovim with yours package manager.'
            'The neovim version maybe outdated')
    else:
        install_bin_neovim_linux(var)
        install_linux_syspath(var.bin_path)
    install_py_module()

def install_neovim_windows_bin(var):
    """
    Install neovim on linux
    """
    install_bin_neovim_windows(var)
    install_py_module()
    install_windows_syspath(var.bin_path)
