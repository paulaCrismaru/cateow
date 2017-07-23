#!/usr/bin/env python
import click
import inspect
import os
import random

from cateow import cateow


@click.command()
@click.option('--meanie', default=None, help='What kitty will say')
def be_mean(meanie):
    file_path = os.path.dirname(
        os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = os.sep.join([file_path, 'kitties'])
    if meanie is None:
        meanies_path = os.sep.join([file_path, 'cateow', 'meanies'])
        meanie = random.choice(open(meanies_path).readlines())
    if os.path.isdir(path):
        file = random.choice(os.listdir(path))
        with open(os.sep.join([path, file]), 'rb') as f:
            kitty = f.read()

        cateow.cateow(meanie, kitty)


if __name__ == '__main__':
    be_mean()
