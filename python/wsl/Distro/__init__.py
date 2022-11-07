import config
import subprocess

distro = config.distro

def runWSL(cmd):
    run = subprocess.run(f"wsl {cmd}", check=True, stdout=subprocess.PIPE, text=True,)
    return run.stdout


def listAvailableDistro():
    runWSL("--list --online")

def installDistro(distro):
    runWSL(f"wsl --install -d {distro}")


# graph.doc: https://learn.microsoft.com/en-us/windows/wsl/install