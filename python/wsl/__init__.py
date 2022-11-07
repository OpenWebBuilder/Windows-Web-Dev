from pathlib import Path
from pathlib import PurePosixPath
from shell import get_cmd_output


def _unc_path_from_cmd(unix_path):
    return Path(
        get_cmd_output(f"wslpath -w `realpath {unix_path}`").strip()
    )

def root_unc_path():
    """UNC path of the root."""
    return _unc_path_from_cmd("/")

def home_unc_path():
    """UNC path of the user home."""
    return _unc_path_from_cmd("~")

def home_path():
    """POSIX path of the user home."""
    return PurePosixPath(get_cmd_output("echo ~").strip())

def shell():
    """Default user shell path."""
    home = str(home_path)
    with open(root_unc_path / "etc" / "passwd") as passwd:
        line = next(itm for itm in passwd.readlines() if home in itm)
        return line.split(":")[-1].strip()


def copyTo():
    pass


def test():
    test1 = _unc_path_from_cmd("/home/me")
    print(test1)


# prime src: https://github.com/sanzoghenzo/wsl-tools
