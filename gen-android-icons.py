__author__ = 'Maksim Dmitriev'

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', help='foo help', required=True)
    args = parser.parse_args()
