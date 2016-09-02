import argparse
import logging
import os
import sys
import yaml
from os import path

here = os.path.dirname(os.path.realpath(__file__))

# Get version from the VERSION file
with open(path.join(here, 'VERSION'), encoding='utf-8') as f:
    script_version = f.readline().strip()


def parse_args(args):
    """parse cmdline args and return options to caller"""
    parser = argparse.ArgumentParser(
        description="Morelia - A Slack AI (Bot)")

    parser.add_argument('--version', action='version',
                        version='%(prog)s {}'.format(script_version))

    return parser.parse_args(args)


def main(args):
    args = parse_args(args)
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format="%(asctime)s (%(threadName)-10s) [%(levelname)8s] - %(message)s")
