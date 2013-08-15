# Boilerplate script for creating a new Tornado web app project.
# Will create results in new directory from calling directory.
# Author: Suharsh Sivakumar
# Date: August 13, 2013

import argparse
import sys
import subprocess


parser = argparse.ArgumentParser(prog='mypyserver.py')
parser.add_argument('--name', nargs='?', default='',
                    help='Name of project and virtual env.')
parser.add_argument('--modules', nargs='*', default=[],
                    help='Modules to be installed by pip.')
parser.add_argument('--git_url', nargs='?', default='',
                    help='Url to initial git repository.')
parser.add_argument(
    '--venv_base_dir', nargs='?', default='',
    help='The base directory where venvs on your system are stored. ' +
         'If not provided, no virtualenv will be created.')
args = parser.parse_args(sys.argv[1:])

# Required modules.
required_modules = ['tornado']

if not args.name:
  raise Exception('You must name you project.')

# Create the folders.
subprocess.call(['mkdir', args.name])
subprocess.call(['mkdir', args.name + '/handlers'])
subprocess.call(['mkdir', args.name + '/static'])
subprocess.call(['mkdir', args.name + '/templates'])
subprocess.call(['mkdir', args.name + '/static/css'])
subprocess.call(['mkdir', args.name + '/static/img'])
subprocess.call(['mkdir', args.name + '/static/js'])

if args.venv_base_dir:
  # Create the virtual environment with the user define modules.
  venv_commands = ('source /usr/local/bin/virtualenvwrapper.sh &&' +
                   ' mkvirtualenv {0}'.format(args.name))
  for module in (args.modules + required_modules):
    venv_commands = (venv_commands +
                     ' && /usr/local/bin/pip install -E {0}/{1} {2}'
                     .format(args.venv_base_dir, args.name, module))
  # Create the requirements.txt from the installed modules.
  venv_commands = (venv_commands +
                   ' && /usr/local/bin/pip freeze -E' +
                   ' {0}/{1}'.format(args.venv_base_dir, args.name) +
                   ' > {0}/requirements.txt'.format(args.name))
  subprocess.call(venv_commands, shell=True)
  print ('Virtualenv {0} created. Execute \'workon {0}\''.format(args.name) +
         ' before running you application.')


# Add gitignore
# Initialize with git

# Do the first commit
