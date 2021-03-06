#!/usr/bin/env python3
import os
from setuptools import setup
import shutil


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


if not os.path.exists('build'):
    os.mkdir('build')
scripts = (
    'main.py',
    'decode.py',
    'dump_dev.py',
    'hist_eq.py',
    'hist_eq_dir.py',
    'img2bin.py',
    'mask.py',
    'cal.py',
    'fire.py',
    'raw.py',
    'process.py',
    #'prog_eeprom.py',
    #'restore_dev.py',
)
scripts_dist = []
for script in scripts:
    # Make script names more executable like
    dst = 'build/gxs700-' + script.replace('.py', '').replace('_', '-')
    shutil.copy(script, dst)
    scripts_dist.append(dst)

setup(
    name="gxs700",
    version="2.0.0",
    author="John McMaster",
    author_email='JohnDMcMaster@gmail.com',
    description=("Gendex GXS700 / Dexis Platinum USB x-ray sensor driver."),
    license="BSD",
    keywords="gxs700 gendex dexis x-ray",
    url='https://github.com/JohnDMcMaster/gxs700',
    packages=['gxs700'],
    scripts=scripts_dist,
    install_requires=[
        'libusb1',
    ],
    long_description="gxs700 x-ray go vroom",
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
)
