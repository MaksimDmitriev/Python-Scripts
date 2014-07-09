__author__ = 'Maksim Dmitriev'

from enum import Enum
import argparse
import os

from PIL import Image


class Density(Enum):
    MDPI = ('drawable-mdpi', 1)
    HDPI = ('drawable-hdpi', 1.5)
    XHDPI = ('drawable-xhdpi', 2)
    XXHDPI = ('drawable-xxhdpi', 3)

    def __init__(self, folder, factor):
        self.folder = folder
        self.factor = factor

    def get_dim(self, base_dim):
        return int(base_dim * self.factor)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', help='the icon to be resized', required=True)
    parser.add_argument('-d', '--dest', help='the directory where resized icons are saved')
    parser.add_argument('-W', '--width', help='the width for medium-density (MDPI) screens (px)', type=int,
                        required=True)
    parser.add_argument('-H', '--height', help='the height for medium-density (MDPI) screens (px)', type=int,
                        required=True)
    parser.add_argument('-f', '--outfile', help='the output file names')

    args = parser.parse_args()
    if not os.path.isfile(args.source):
        raise FileNotFoundError('No such file or directory: ' + args.source)

    dest_dir = args.dest
    if dest_dir is None:
        dest_dir = os.path.join(os.path.dirname(os.path.realpath(args.source)), 'res')
    os.makedirs(dest_dir, exist_ok=True)

    '''
    They say os.path.basename will not work in all cases.
    http://stackoverflow.com/a/8384788/1065835
    But it's highly unlikely that somebody will use weird names for Android icons.
    '''
    out_filename = args.outfile if args.outfile is not None else os.path.basename(args.source)

    for density in Density:
        os.makedirs(os.path.join(dest_dir, density.folder), exist_ok=True)
        Image.open(args.source).resize((density.get_dim(args.height), density.get_dim(args.width))).save(
            os.path.join(dest_dir, density.folder, out_filename), 'PNG')