import subprocess
from shell import run_sudo, run_command, get_cmd_output

def installAnsible():
    try:
        if ( (get_cmd_output("which ansible").strip()) == "/usr/bin/ansible"):
            print("installed = True")
    except subprocess.CalledProcessError:
        run_sudo("apt update")
        run_sudo("apt install ansible git -y")

def allDependencies():
    installAnsible()

# graph.guide: https://geekrewind.com/how-to-install-wordpress-on-windows-wsl/