#!/usr/bin/env python
# encoding: utf-8
"""
interactive_memcached.py

Created by dorkitude on 2010-10-25.
"""

import sys, os
import getopt

help_message = '''
Use
'''

# this line forces python into adorable mode:
os.environ['PYTHONINSPECT'] = '1'

class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg


def main(argv=None):
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "ho:v", ["help", "output="])
		except getopt.error, msg:
			raise Usage(msg)
	
		# option processing
		for option, value in opts:
			if option == "-v":
				verbose = True
			if option in ("-h", "--help"):
				raise Usage(help_message)
			if option in ("-o", "--output"):
				output = value
	
	except Usage, err:
		print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
		print >> sys.stderr, "\t for help use --help"
		return 2
	
	


if __name__ == "__main__":
    print "hi"
    # sys.exit(main())
