# Boilerplate script for creating a new Tornado web app project.
# Will create results in new directory from calling directory.
# Author: Suharsh Sivakumar

import argparse
import sys
import subprocess


parser = argparse.ArgumentParser(prog='mypyserver.py')
parser.add_argument('--name', nargs='?', default='', help='Name of project and virtual env.')
parser.add_argument('--modules', nargs='*', help='Modules to be installed by pip.')
parser.add_argument('--venv', nargs='?', default=True, type=bool, help='Whether or not to create a virtual env')
args = parser.parse_args(sys.argv[1:])

if not args.name:
  raise Exception('You must name you project.')

# Required modules.
required_modules = ['tornado']

# Create the virtual environment with the user define modules.
subprocess.call(['mkvirtualenv', args.name], shell=True)
for module in (args.modules + required_modules):
  subprocess.call(['pip install', module], shell=True)


