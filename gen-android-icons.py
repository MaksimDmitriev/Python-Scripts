import PIL

__author__ = 'Maksim Dmitriev'

import argparse
import os

from PIL import Image
from enum import Enum

# class Density(Enum):
#     mdpi = 1
# TODO: implement if possible

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', help='the icon to be resized', required=True)
    parser.add_argument('-d', '--dest', help='the directory where resized icons are saved')
    parser.add_argument('-b', '--baseline', help='the baseline (MDPI) asset (px)', type=int, required=True)
    parser.add_argument('-f', '--outfile', help='the output file names')

    args = parser.parse_args()
    source_image = args.source
    if not os.path.isfile(source_image):
        raise FileNotFoundError('No such file or directory: ' + source_image)

    dest_dir = args.dest
    if dest_dir is None:
        dest_dir = os.path.join(os.path.dirname(os.path.realpath(source_image)), 'out')
        os.makedirs(dest_dir, exist_ok=True)

    mdpi = 'mdpi'
    hdpi = 'hdpi'
    xhdpi = 'xhdpi'
    xxhdpi = 'xxhdpi'

    dpi_dirs = {mdpi: os.path.join(dest_dir, 'drawable-mdpi'),
                hdpi: os.path.join(dest_dir, 'drawable-hdpi'),
                xhdpi: os.path.join(dest_dir, 'drawable-xhdpi'),
                xxhdpi: os.path.join(dest_dir, 'drawable-xxhdpi')}

    for k, v in dpi_dirs.items():
        os.makedirs(v, exist_ok=True)

    # a if test else b
    outfile = args.outfile if args.outfile is not None else 'dolor'
    Image.open(source_image, 'r').resize((args.baseline, args.baseline)).save(os.path.join(dpi_dirs[mdpi], outfile),
                                                                              'PNG')
    # TODO: convert float to integer
    # Image.open(source_image, 'r').resize((args.baseline * 1.5, args.baseline * 1.5)).save(
    #     os.path.join(dpi_dirs[hdpi], outfile), 'PNG')
    Image.open(source_image, 'r').resize((args.baseline * 2, args.baseline * 2)).save(
        os.path.join(dpi_dirs[xhdpi], outfile), 'PNG')
    Image.open(source_image, 'r').resize((args.baseline * 3, args.baseline * 3)).save(
        os.path.join(dpi_dirs[xxhdpi], outfile), 'PNG')



