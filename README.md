# aptly-convert.py

**Turkish:** Python ile yazılmış olan bu betik, bir dizinde ve alt dizinlerinde yer alan çok sayıdaki "*.deb" paketlerini modern bir paket deposu aracı olan "aptly"nin kullandığı dizin yapısına göre çok hızlı bir şekilde yeniden oluşturmanızı sağlar. Böylece örneğin Pardus, Debian, Ubuntu gibi ".DEB" uzantılı paketlerler çalışan Linux dağıtımlarında "apt-mirror" ile oluşturulmuş yerel depo yansılarını (varsayılan dizin "/var/spool/apt-mirror") GB'larca veriyi yeniden indirmek zorunda kalmadan saniyeler için aptly'nin kullanacağı şekilde yeniden organize edebilirsiniz. Betik zamandan ve disk alanından tasarruf etmek için paketlerin kopyasını oluşturmaz, bunun yerine sadece "hard link" oluşturur. Artık aski dizin yapısını kullanmayacaksanız işlem bittikten sonra eski dosyaları güvenle silebilirsiniz.

## Description

Automation script for hard-linking the DEB files in a directory into another directory using the aptly pool directory structure.

## Info

This script creates hard links for the DEB files into the aptly pool directory structure. You can use the script for any directory structure conatining DEB files (such as the default mirror directory "/var/spool/apt-mirror" for DEB files mirrored with apt-mirror). 

After executing this script the new directory structure of the files be comaptible with aptly.  So when you update your aptly mirror the DEB files will not be downloaded again. Hardlinks are used to save time and disk space. 

I you already have an aptly pool containing some files, it is recommended to use a temporary aptly pool folder and then merge the contents using rsync etc. manually. After checking everthing is ok, you can safely delete ("rm", "rm -rf") the old DEB files since they are already hard linked to new directory structure.

I have written this script to transfer my local apt-mirror repositories to aptly. It saved me a lot of time and bandwidth. Since it uses hardlinks, it doesn't require extra disk space. I hope it will be usefull for others.

## Usage

```
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
```
