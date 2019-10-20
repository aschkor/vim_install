
import pip

def install_module(mod):
    pip.main(["install","--user",mod])

if __name__ == "__main__":
    install_module("appdirs")
    install_module("gitpython")
