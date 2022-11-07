import subprocess
import config

name = config.distro
WSL_EXE = "wsl.exe"
load_profile = False

def _cmd_base() -> str:
    """Base command for launching programs in the WSL distro."""
    return f"{WSL_EXE} ~ -d {name}"

def run_command( command, load_profile = False, **kwargs ):
    """
    Run a bash command in the distro.
    Args:
        command: command to run in the WSL distro.
        load_profile: load .profile before running the command.
        kwargs: arguments to pass to the subprocess function.
    Returns:
        The result of the subprocess call.
    """
    login = "l" if load_profile else ""
    command = f"sh -c{login} '{command}'"
    return subprocess.run(f"{_cmd_base()} {command}", **kwargs)

def get_cmd_output(cmd, **kwargs):
    """
    Run a command in the distro and return the stdout output as text.
    Args:
        cmd: commmand to run in the WSL distro.
        kwargs: arguments to pass to subprocess.Popen
    Returns:
        command output.
    """
    run = run_command(
        cmd,
        check=True,
        stdout=subprocess.PIPE,
        text=True,
        **kwargs,
    )
    return run.stdout

def get_output(cmd, **kwargs):
    """
    *my. modification that doesn't use `check=True,` so works even if non-zero return code!
    """
    run = run_command(
        cmd,
        stdout=subprocess.PIPE,
        text=True,
        **kwargs,
    )
    return run.stdout

def run_sudo(command):
    sudo_password = "u"
    """Run the commmand with sudo."""
    run_command(f"echo '{sudo_password}' | sudo -H -S {command}")


# prime src: https://github.com/sanzoghenzo/wsl-tools