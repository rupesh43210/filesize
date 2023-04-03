import os
import sys
import inspect

def install_dependencies():
    try:
        os.system("which pip3 || sudo apt-get install python3-pip")
        os.system("pip3 install tabulate termcolor")
        print("\nPackages installed successfully.")
    except Exception as e:
        print(f"Error installing packages: {e}")
        sys.exit(1)

def create_alias():
    try:
        shell = os.environ['SHELL']
        if 'bash' in shell:
            config_file = os.path.expanduser('~/.bashrc')
        elif 'zsh' in shell:
            config_file = os.path.expanduser('~/.zshrc')
        else:
            print("Unsupported shell. Please add the alias manually.")
            return

        path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        file_size_path = os.path.join(path, 'file_size.py')

        with open(config_file, 'a') as f:
            f.write(f'\nalias filesize="sudo python3 {file_size_path}"\n')

        print("\nAlias 'filesize' created successfully.")
    except Exception as e:
        print(f"Error creating alias: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_dependencies()
    create_alias()
