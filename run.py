#!/usr/bin/env python
# encoding: utf-8
"""
interactive_memcached.py

Created by dorkitude on 2010-10-25.
"""

import sys, os
import getopt
import python_memcached_fork.memcache as memcache


help_message = '''
Use
'''

# this line forces python into adorable mode:
os.environ['PYTHONINSPECT'] = '1'

    
def show_startup_text():
    f = open('STARTUP')
    print "".join(f.readlines())
    f.close() 

def get_client():
    return memcache.Client(['127.0.0.1:11211'], debug=0)

def help():
    f = open('USAGE')
    print "".join(f.readlines())
    f.close()
    
    
if __name__ == "__main__":
    show_startup_text()
    ac = get_client()
    
    