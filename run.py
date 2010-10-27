#!/usr/bin/env python
# encoding: utf-8
"""
adorable_memcached
Created by dorkitude on 2010-10-25.
"""

import os
from python_memcached_fork import memcache
import binascii # used for php_mode
import pickle
from PHPSerialize_Scott_Hurring.PHPSerialize import PHPSerialize
from PHPSerialize_Scott_Hurring.PHPUnserialize import PHPUnserialize

# this line forces python into adorable mode (referred to by some as 'interactive mode')
os.environ['PYTHONINSPECT'] = '1'

SETTINGS = {
    'hosts' : [ 'localhost:11211' ], # a list of servers:port strings
    'php_mode' : False, # if true, adorable will hash keys and use php-style serialization/deserialization on values.
}



# if we're in php_mode, make sure the keys get hashed in php style    
if SETTINGS['php_mode']:
    print ""
    print ""
    print ""
    print "php mode: TRUE"
    print ""
    print ""
    print ""
    def php_hash(key):
        return (binascii.crc32(key) >> 16) & 0x7fff # borrowed from http://groups.google.com/group/memcached/msg/7bb75a026c44ec43
    memcache.serverHashFunction = php_hash
    
    
def raw(input):
    print "Tryme"
    return input

class AdorableClient(memcache.Client):
    """docstring for AdorableMemcache"""
    def __init__(self, settings):

        if settings['php_mode']:
            pickler = AdorablePicklerPHP
            unpickler = AdorableUnpicklerPHP
        else:
            pickler = pickle.Pickler
            unpickler = pickle.Unpickler
        
        super(AdorableClient, self).__init__(servers=settings['hosts'], pickler=pickler, unpickler=unpickler)

class AdorablePicklerPHP(pickle.Pickler):
    """docstring for AdorablePicklerPHP"""
    def dump(self, obj):
        self.write(PHPSerialize().serialize(obj))

class AdorableUnpicklerPHP(object):
    """docstring for AdorableUnpicklerPHP"""
    def __init__(self, arg):
        super(AdorableUnpicklerPHP, self).__init__()
        # print type(arg)
        # print arg.getvalue()
        self.inputString = arg.getvalue()

    def load(self):
        print "unserializing: %s" % self.inputString
        return PHPUnserialize().unserialize(self.inputString)

def show_startup_text():
    f = open('STARTUP')
    print "".join(f.readlines())
    f.close() 

def get_client(settings):
    return AdorableClient(settings)

def help():
    f = open('USAGE')
    print "".join(f.readlines())
    f.close()
    
    
if __name__ == "__main__":
    show_startup_text()
    ac = get_client(SETTINGS)
    # 
    # 
    # print "---"
    # 
    # ac.set('dicto', {'key' : 'value'})
    # ac.set('listo', [1,2,3,4,5,'why'])
    # 
    # print "what i get back for dicto is %s" % ac.get('dicto')
    # print "what i get back for listo is %s" % ac.get('listo')
    # 