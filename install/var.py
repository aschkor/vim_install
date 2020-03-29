from pathlib import Path
from appdirs import *
import tempfile


class var:
    """
    Global variables
    """
    def __init__(self,app_name):
        """
        Initialize global variables
        """
        script_path = Path(os.path.dirname(sys.argv[0]))
        res_dir = script_path / 'install'/'res'
        self.descr_file_pack_path = res_dir / 'pack'
        self.files_conf_dir = res_dir / 'conf'
        self.utility_dir = res_dir / 'utility_script'
        self.install_dir_src = script_path / 'install'


class var_neovim(var):
    """
    Global variable for neovim
    """
    def __init__(self):
        """
        Initiallize global variables for neovim
        """
        app_name = 'nvim'
        super().__init__(app_name)
        self.user_data_dir = Path(user_data_dir(app_name,''))
        self.conf_path = Path(user_config_dir(app_name,''))
        self.conf_file_path = self.conf_path / 'init.vim'


class var_neovim_linux(var_neovim):
    """
    Global variable for neovim on linux
    """
    def __init__(self):
        """
        Initiallize global variables for neovim on linux
        """
        super().__init__()
        self.bin_dir_path = Path.home() / '.local' / 'bin' / 'nvim'
        self.bin_url = 'https://github.com/neovim/neovim/releases/download/nightly/nvim.appimage'
        self.bin_path = self.bin_dir_path / 'nvim.appimage'
        self.pack_dir = self.user_data_dir / 'site' / 'pack'
        self.utility_file_dir = self.bin_dir_path


class var_neovim_windows(var_neovim):
    """
    Global variable for neovim on windows
    """
    def __init__(self):
        """
        Initiallize global variables for neovim on windows
        """
        super().__init__()
        self.bin_dir_path = Path.home() / 'AppData' / 'Local' / 'Programs'
        self.bin_url = 'https://github.com/neovim/neovim/releases/download/v0.4.2/nvim-win64.zip'
        self.zip = Path(tempfile.gettempdir()) / 'neovim.zip'
        self.bin_path = self.bin_dir_path / 'Neovim' / 'bin' / 'nvim.exe'
        self.pack_dir = Path.home() / 'AppData' / 'Local' / 'nvim-data' / 'site' / 'pack'
        self.utility_file_dir = self.bin_dir_path / 'Neovim'
