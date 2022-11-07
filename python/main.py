import config
config.distro = "Ubuntu-20.04"
config.user = "me"
config.sudopass = "u"
config.repo_name = "Wordpress-Dev"

import Wordpress
import wsl
import wsl.copy

if __name__ == '__main__':

    Wordpress.installWordpress()

    # wsl.test()