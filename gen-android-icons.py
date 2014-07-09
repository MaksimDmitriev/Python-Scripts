__author__ = 'Maksim Dmitriev'

import argparse
import os

from PIL import Image

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

    im = Image.open(source_image, 'r').resize((args.baseline, args.baseline))
    im.save(os.path.join(dpi_dirs[mdpi], 'lorem'), 'PNG')



