__author__ = 'Maksim Dmitriev'

import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', help='the icon to be resized', required=True)
    parser.add_argument('-d', '--dest', help='the directory where resized icons are saved')
    parser.add_argument('-f', '--outfile', help='the output file names')

    args = parser.parse_args()
    source_image = args.source
    dest_dir = args.dest
    if dest_dir is None:
        dest_dir = os.path.join(os.path.dirname(os.path.realpath(source_image)), 'out')
        os.makedirs(dest_dir, exist_ok=True)

    dpi_dirs = ['drawable-mdpi', 'drawable-hdpi', 'drawable-xhdpi', 'drawable-xxhdpi']
    for dpi_dir in dpi_dirs:
        os.makedirs(os.path.join(dest_dir, dpi_dir), exist_ok=True)

