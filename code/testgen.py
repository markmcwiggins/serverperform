#!/usr/bin/env python

# testgen: generate data for storage/reporting by sperform.py

# author: Mark McWiggins <mark@pythonsoftwarewa.com>

import requests
import json
import random
import gevent
import sys
import time


# usage: testgen.py ngreen ndp 
#
# ngreen == number of 'greenlets' (see gevent docs -- a substitute for threads)
# ndp == number of data points, one each for a different server (per greenlet)

try:
    ngreen = int(sys.argv[1])     
except:
    ngreen = 200

try:
    ndp = int(sys.argv[2])
except:
    ndp = 20

now = int(time.time())           # current number of seconds since the epoch
onedayago = now - 86400          # yesterday this same time


url = 'http://127.0.0.1:8080/addserver'        # by default

def dogreen(greenno):   # one 'greenlet' of gevent
    for i in range(ndp):      # one data point per server
        s = 'server%03d' % i
        cpu = greenno * 0.01 * i    # fixed data for ease in testing
        ram = greenno * 0.05 * i    
        dt = random.randint(onedayago,now)   # distribute data randomly in time over the last day
        data = json.dumps({'server' : s, 'cpu' : cpu, 'ram' : ram, 'dt' : dt})
    #print data
        r = requests.post(url,data=data)
        assert(r.status_code == 200)

glist = []
for i in range(ngreen):
    glist.append(gevent.spawn(dogreen(i)))    # multiple 'greenlets' run simultaneously (really in a cooperative multitasking setup)


# just grab one server's report

r2 = requests.get("http://127.0.0.1:8080/report/server005")
assert(r2.status_code == 200)
print r2.json()

print 'PASSED'
