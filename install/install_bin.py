from pip._internal import main
import urllib.request
from .var import var_neovim
from pathlib import Path
import zipfile
import os


def install_bin_neovim_linux(var):
    """
    Downlaod neovim binary in the binary path on linux
    """
    var.bin_dir_path.mkdir(0o744,True,True)
    urllib.request.urlretrieve(var.bin_url,var.bin_path)
    var.bin_path.chmod(0o744)


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
    main.main(['install','--user','neovim'])


def install_linux_syspath(bin_path):
    """
    Add alias to neovim binary in the bashrc
    """
    init_vim = Path.home() / '.bashrc'
    f=open(init_vim,'a+')
    f.write('alias nvim=\''+str(bin_path)+'\'\n')
    f.close()


def install_windows_syspath(bin_path):
    """
    Add bin path to PATH windows systeme variable
    """
    os.environ['Path'] += os.pathsep + str(bin_path)


def install_neovim_linux_bin(var):
    """
    Install neovim on Windows
    """
    install_bin_neovim_linux(var)
    install_py_module()
    install_linux_syspath(var.bin_path)


def install_neovim_windows_bin(var):
    """
    Install neovim on linux
    """
    install_bin_neovim_windows(var)
    install_py_module()
    install_windows_syspath(var.bin_path)
