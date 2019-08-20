"""
TCP-Pot.

TCP open port honeypot logger

Usage:
  tcp-pot [config_filepath]

Options:
  [config_filepath]     Path to config options .ini file
  -h --help     Show this screen.
"""

from docopt import docopt

args = docopt(__doc__)

print("Config file: %s", args['[config_filepath]'])