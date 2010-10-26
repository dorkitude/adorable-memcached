#!/usr/bin/env python
# encoding: utf-8
"""
adorable_memcached
Created by dorkitude on 2010-10-25.
"""

import os
import python_memcached_fork.memcache as memcache

# this line forces python into adorable mode (referred to by some as 'interactive mode')
os.environ['PYTHONINSPECT'] = '1'

SETTINGS = {
    'host' : '127.0.0.1:11211'
}

    
def show_startup_text():
    f = open('STARTUP')
    print "".join(f.readlines())
    f.close() 

def get_client():
    return memcache.Client([ SETTINGS['host'] ], debug=0)

def help():
    f = open('USAGE')
    print "".join(f.readlines())
    f.close()
    
    
if __name__ == "__main__":
    show_startup_text()
    ac = get_client()
    
    