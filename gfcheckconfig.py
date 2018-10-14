import git.exc as GitError
import git.repo
import getpass
import configparser

try:
    config_file = "/home/{0}/.config/gitfire.conf".format(getpass.getuser())
    
    with open(config_file, 'r'):
        pass

    config = configparser.ConfigParser()
    config.read(config_file)

    if not config['DEFAULT']['GIT_FIRE_REPO']:
        raise configparser.NoOptionError
    
    with  git.Repo(config['DEFAULT']['GIT_FIRE_REPO']) as repo:
        print("{0}: Config file OK".format(config_file))

except FileNotFoundError:
    print("{0}: Not Found".format(config_file))

except (configparser.NoOptionError, KeyError):
    print("GIT_FIRE_REPO not defined in [DEFAULT] section")

except GitError.InvalidGitRepositoryError as e:
    print("{0}: Invalid git repo".format(str(e)))
