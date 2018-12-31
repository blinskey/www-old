"""Pelican plugin that gzips all files."""

import gzip
import os
import re
import shutil

import pelican


def compress(path):
    with open(path, "rb") as in_file:
        with gzip.open(path + ".gz", "wb") as out_file:
            shutil.copyfileobj(in_file, out_file)


def gzip_files(pelican):
    pattern = ".*[^.gz]$"
    regex = re.compile(pattern)

    out_dir = pelican.settings["OUTPUT_PATH"]
    for dirpath, dirnames, filenames in os.walk(out_dir):
        for name in filenames:
            if regex.match(name):
                fullpath = os.path.join(dirpath, name)
                compress(fullpath)


def register():
    pelican.signals.finalized.connect(gzip_files)
