from __future__ import absolute_import, print_function

import sys
import argparse

import where


def main():
    parser = argparse.ArgumentParser(description=
        "Find the locations of a file in the environment's paths")

    parser.add_argument('filename', type=str, help='The filename to be found')

    args = parser.parse_args()

    for result in where.iwhere(args.filename):
        print(result)
