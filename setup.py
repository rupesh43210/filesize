import os
import sys
import inspect

def check_sudo():
    if os.geteuid() != 0:
        print("This script requires root privileges. Please run as sudo.")
        sys.exit(1)

def install_dependencies():
    try:
        os.system("which pip3 || sudo apt-get install python3-pip -y")
        os.system("pip3 install tabulate")
        os.system("pip3 install termcolor")
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

def update_bashrc_for_all_users():
    try:
        file_size_path = os.path.abspath(inspect.getfile(inspect.currentframe()))
        file_size_path = os.path.join(os.path.dirname(file_size_path), "file_size.py")
        with open("/etc/profile.d/filesize.sh", "w") as f:
            f.write(f"path={file_size_path}\n")
            f.write("if [ -f \"$path\" ]\n")
            f.write("then\n")
            f.write("    echo \"alias filesize='sudo python3 $path'\" >> /etc/bash.bashrc\n")
            f.write("fi\n")
        os.system("sudo chmod +x /etc/profile.d/filesize.sh")
        print("\n/etc/bash.bashrc updated for all users.")
    except Exception as e:
        print(f"Error updating /etc/bash.bashrc for all users: {e}")
        sys.exit(1)

if __name__ == "__main__":
    check_sudo()
    install_dependencies()
    create_alias()
    if 'bash' in os.environ['SHELL']:
        os.system("sudo bash -c 'source ~/.bashrc'")
    elif 'zsh' in os.environ['SHELL']:
os.system("sudo zsh -c 'source ~/.zshrc'")
update_bashrc_for_all_users()
