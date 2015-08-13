#! /usr/bin/env python 

import sys
print sys.version
print sys.executable
print sys.path

from tasks import add
for x in range(0,20):
    print "Sending: %d" % (x)
    result = add.delay(1,x)
    value = result.get(timeout=2)
    print "Result: %d" % (value)
    print "--------------"


