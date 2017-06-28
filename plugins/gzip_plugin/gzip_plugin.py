"""Pelican plugin that gzips all files."""

import gzip
import os
import re
import shutil

import pelican


def for_each_file(pelican, func, pattern=".*"):
    out_dir = pelican.settings["OUTPUT_PATH"]
    regex = re.compile(pattern)
    for dirpath, dirnames, filenames in os.walk(out_dir):
        for name in filenames:
            if (regex.match(name)):
                fullpath = os.path.join(dirpath, name)
                func(fullpath)


def gzip_files(pelican):
    def compress(path):
        with open(path, "rb") as in_file, \
                gzip.open(path + ".gz", "wb") as out_file:
            shutil.copyfileobj(in_file, out_file)

    for_each_file(pelican, compress, pattern=".*[^\.gz]$")


def register():
    pelican.signals.finalized.connect(gzip_files)
