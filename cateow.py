#!/usr/bin/env python
import click
import inspect
import os
import random

from cateow import cateow


@click.command()
def be_mean():
    file_path = os.path.dirname(
        os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = os.sep.join([file_path, 'kitties'])
    meanies = os.sep.join([file_path, 'cateow', 'meanies'])
    if os.path.isdir(path):
        file = random.choice(os.listdir(path))
        with open(os.sep.join([path, file]), 'rb') as f:
            content = f.read()
        text = random.choice(open(meanies).readlines())

        cateow.cateow(text, content)


if __name__ == '__main__':
    be_mean()
