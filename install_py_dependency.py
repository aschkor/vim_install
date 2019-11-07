from pip._internal import main

def install_module(mod):
    main.main(["install","--user",mod])

if __name__ == "__main__":
    install_module("appdirs")
    install_module("gitpython")
