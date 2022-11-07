import config
import shell
import wsl
# from shell import run_sudo, run_command
import Dependency
import ansible

repo_name = config.repo_name


repo_url = f"https://github.com/OpenWebBuilder/{repo_name}.git"

def cloneBaseRepo():
    shell.run_command(f"[ ! -d '{repo_name}' ] && git clone {repo_url}")
    shell.run_command(f"[ -d '{repo_name}' ] && cd {repo_name}; git pull")


def installWordpress():
    # print("Installing wordpress")
    Dependency.allDependencies()
    cloneBaseRepo()
    ansible.initInventory()

def makeSite():
    pass
    # run_sudo("mkdir -p ~/Wordpress/1PRbrands.com")
