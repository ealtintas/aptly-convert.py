# aptly-convert.py

## Description

Automation script for hard-linking the DEB files in a directory into another directory using the aptly pool directory structure.

## Info

This script create hard links for the DEB files into the aptly pool directory structure. You can use the script for any directory structure conatining debs such as the mirrored with apt-mirror. The new directory structure of the file be comaptible with aptly.  So when you update your mirror the deb files will not be downloaded again. Hardlinks are used to save time and disk space. It is recommended to use a temproary aptly pool folder and then merge the contents using rsync etc. manually. After checking everthing is ok, you can safely delete ("rm", "rm -rf") the old DEB files since they are already hard linked to new directory structure.

## Usage

usage: aptly-convert.py [-h] [--verbosity VERBOSITY] [--src_path SRC_PATH]
                        [--dst_path DST_PATH]

optional arguments:
  -h, --help            show this help message and exit
  --verbosity VERBOSITY, -v VERBOSITY
                        increase output verbosity. 1: Prints info for every
                        file processed. 2: Prints extra info (HASH etc.) for
                        every file processed. 3: Prints directory traversal
                        info.
  --src_path SRC_PATH, -s SRC_PATH
                        Source directory containing the DEB files (defaults to
                        "/var/spool/apt-mirror")
  --dst_path DST_PATH, -d DST_PATH
                        Destination directory that will contain the DEB files
                        in aptly pool structure (defaults to
                        "/var/spool/aptly/pool")
