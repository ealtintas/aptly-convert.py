#!/usr/bin/python
#
# script: aptly-convert.py
#
# This script creates hard links for the DEB files into the aptly pool directory structure.
# You can use the script for any directory structure conatining DEB files (such as the default 
# mirror directory "/var/spool/apt-mirror" for DEB files mirrored with apt-mirror).
# After executing this script the new directory structure of the files will be comaptible with aptly. 

import os
import sys
import apt
import hashlib
import argparse

def main(argv):
	
	parser = argparse.ArgumentParser(description='Automation script for hard-linking the DEB files in a directory into another directory using the aptly pool directory structure.')
	parser.add_argument("--verbosity", "-v", help="increase output verbosity. 1: Prints info for every file processed. 2: Prints extra info (HASH etc.) for every file processed. 3: Prints directory traversal info.")
	parser.add_argument("--src_path", "-s", action="store", help='Source directory containing the DEB files (defaults to "/var/spool/apt-mirror")')
	parser.add_argument("--dst_path", "-d", action="store", help='Destination directory that will contain the DEB files in aptly pool structure (defaults to "/var/spool/aptly/pool")')
	args = parser.parse_args()

	if args.verbosity:
		print("Verbosity turned on. I will print about every file processed.")
		
	dst_path = args.dst_path
	if dst_path == None:
		dst_path="/var/spool/aptly"
	print "Aptly pool structure will be created in the destination path: " + dst_path
	
	src_path = args.src_path
	if src_path == None:
		src_path="/var/spool/apt-mirror"

	print("Traversing files in the source path: " + src_path)
	for (path, dirs, files) in os.walk(src_path):
		if args.verbosity == "3":
			print "Path:", path
			print "Dirs:", dirs
			print "Files:", files
			print "-----"

		for f in files:
			current_file = os.path.join(path,f)
				
			H = hashlib.md5()

			with open(current_file) as FIN:
				H.update(FIN.read())

			current_md5 = H.hexdigest()
			current_dst_path =  dst_path + '/' + current_md5[:2] + '/' + current_md5[2:4] + '/' 

			if args.verbosity == "2":
				print "File:\t" + current_file + "\tMD5SUM:\t" + current_md5 + "\tDest. Path:\t" + current_dst_path 
		
			try:
				os.makedirs(current_dst_path)
			except OSError:
				pass
					
			current_dst = os.path.abspath (current_dst_path + os.path.basename(current_file))

			if args.verbosity:
				print current_file + "\t=>\t" + current_dst
			try:
				os.link(current_file, current_dst)
			except OSError as e:
				print "Error:", e.errno, e.filename, e.strerror
				pass
			#print "Created hard link successfully!!"
		
		if args.verbosity == "3":
			print "-----"

	print("Completed.")

if __name__ == "__main__":
	main(sys.argv[1:])
