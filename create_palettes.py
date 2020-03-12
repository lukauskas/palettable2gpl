#!/usr/bin/env python3
from tqdm import tqdm
import click
import os

from available_palettes import PALETTES

def write_palette_header(file_handle, name):
    # Inspired by https://github.com/tcyb/cbrewer2gpl/blob/master/cbrewer_convert.ipynb
    file_handle.write('GIMP Palette\n')
    file_handle.write(f'Name: {name}\n')
    file_handle.write(f'Columns: 4\n')
    file_handle.write('#\n')


def write_palette_colors(file_handle, name, colors):
    for i, color in enumerate(colors, start=1):
        r, g, b = color
        color_name = f'{name}.{i}'
        file_handle.write(f'{r:4} {g:4} {b:4} {color_name}\n')

def write_separator(file_handle):
    r = g = b = 0
    color_name = 'SEPARATOR'
    file_handle.write(f'{r:4} {g:4} {b:4} {color_name}\n')

def make_palette_gpl(filename, palette_name, member_palettes):
    first = True
    with open(filename, 'w') as file_:
        write_palette_header(file_, palette_name)
        for member_palette in member_palettes:
            if not first:
                write_separator(file_)

            first = False
            member_name = member_palette.name.partition('_')[0]
            write_palette_colors(file_, member_name, member_palette.colors)


@click.command()
@click.option('--outdir',
              help="Output directory",
              type=click.Path(file_okay=False, writable=True),
              default="palettes")
def main(outdir):

    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    for palette_group, member_palettes in tqdm(PALETTES.items()):
        filename = os.path.join(outdir, f'{palette_group}.gpl')
        make_palette_gpl(filename, palette_group, member_palettes)

if __name__ == '__main__':
    main()
