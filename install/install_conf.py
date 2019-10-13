from shutil import copyfile
from pathlib import Path

def install_conf(var):
    var.conf_path.mkdir(0o744,True,True)
    write_main_conf_file(get_init_content(var),var.conf_file_path)
    copy_conf_files(var)


def get_init_content(var):
    content = '' 
    for conf_file in var.files_conf_dir.iterdir():
        content+='source '
        content+=str(var.conf_path/conf_file.name)
        content+='\n'
    return content


def write_main_conf_file(content,main_conf_path):
    main_conf_path.write_text(content)


def copy_conf_files(var):
    for conf_file_path in var.files_conf_dir.iterdir():
        copyfile(conf_file_path, var.conf_path / conf_file_path.name)

