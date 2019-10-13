from pip._internal import main
import urllib.request
from .var import var_neovim
from pathlib import Path

def install_bin(var):
    """
    Downlaod neovim binary in the binary path
    """
    var.bin_dir_path.mkdir(0o744,True,True)
    urllib.request.urlretrieve(var.bin_url,var.bin_path)
    var.bin_path.chmod(0o744)

def install_py_module():
    """
    Downlaod neovim python module
    """
    main(['install','--user','neovim'])


def install_linux_syspath(bin_path):
    """
    Add alias to neovim binary in the bashrc
    """
    init_vim = Path.home()/'.bashrc'
    f=open(init_vim,'a+')
    f.write('alias nvim=\''+str(bin_path)+'\'\n')
    f.close()

def install_neovim(var):
    """
    Install neovim
    """
    install_bin(var)
    install_py_module()
    install_linux_syspath(var.bin_path)
