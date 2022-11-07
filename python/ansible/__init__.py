import textwrap
import wsl
import config
import os

def getEnv():
    env = "dev"
    return env

def testEnvIP():
    return "8.8.8.8"

def ansibleCfg():
    this = f'''\
    [defaults]
    inventory = .this/inventory/{getEnv()}/hosts
    '''
    this = textwrap.dedent(this)
    return this

def ansibleHostsDev():
    this = f'''\
    [local]
    localhost
    
    [local:vars]
    ansible_connection=local
    ansible_user={config.user}
    ansible_become_password={config.sudopass}
    
    [test]
    {testEnvIP()}
    
    [test:vars]
    ansible_user={config.user}
    ansible_become_password={config.sudopass}
    
    [dev:children]
    local
    '''
    this = textwrap.dedent(this)
    return this

    # graph https://www.johndcook.com/blog/2021/01/30/python-triple-quote-regex/

def initInventory():
    ansible = f"{wsl.home_unc_path()}/{config.repo_name}/ansible"
    inventory = f"{ansible}/.this/inventory/dev"
    ansiblecfg = f"{ansible}/ansible.cfg"

    os.makedirs(inventory, exist_ok=True)

    with open(f"{inventory}/hosts", 'w') as f:
        f.write(ansibleHostsDev())

    with open(ansiblecfg, 'w') as f:
        f.write(ansibleCfg())
