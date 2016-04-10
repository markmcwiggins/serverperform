#!/usr/bin/env python

import requests
import json
import random
import gevent
import sys
import time

try:
    ngreen = int(sys.argv[1])
except:
    ngreen = 10

try:
    ndp = int(sys.argv[2])
except:
    ndp = 100

now = int(time.time())
onedayago = now - 86400


url = 'http://127.0.0.1:8080/addserver'

def dogreen(greenno):   # one 'greenlet' of gevent
    for i in range(ndp):
        s = 'server%03d' % i
        cpu = greenno * 0.01 * i # random.random()
        ram = greenno * 0.05 * i
        dt = random.randint(onedayago,now)
        data = json.dumps({'server' : s, 'cpu' : cpu, 'ram' : ram, 'dt' : dt})
    #print data
        r = requests.post(url,data=data)
        assert(r.status_code == 200)

glist = []
for i in range(ngreen):
    glist.append(gevent.spawn(dogreen(i)))


r2 = requests.get("http://127.0.0.1:8080/report/server005")
assert(r2.status_code == 200)

