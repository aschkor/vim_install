from pathlib import Path
from appdirs import *
class var:
    """
    Global variables
    """
    def __init__(self,app_name):
        """
        Initialize global variables
        """
        script_path = Path(os.path.dirname(sys.argv[0]))
        self.user_data_dir = Path(user_data_dir(app_name))
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
        self.bin_dir_path = Path.home() / '.local'/ 'bin' / app_name
        self.conf_path = Path(user_config_dir(app_name))
        self.conf_file_path = self.conf_path / 'init.vim'
        self.pack_dir = self.user_data_dir / 'site' / 'pack'
        self.bin_url = 'https://github.com/neovim/neovim/releases/download/v0.4.2/nvim.appimage'
        self.bin_path = self.bin_dir_path / 'nvim.appimage'
