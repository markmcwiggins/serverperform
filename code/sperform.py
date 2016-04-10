#!/usr/bin/env python

# sperform: track and report server performance

# author: Mark McWiggins <mark@pythonsoftwarewa.com>

import web
import datetime
import time
import json
from heapq import heappush, heappop
from collections import deque   # O(1) where normal python lists are O(n) on insertion

urls = ('/report/(.*)', "report",
        '/addserver', 'addserver')

app = web.application(urls, globals())

servers = {}



class Server(object):
    def __init__(self, name, cpu, ram, dt = int(time.time())):
        self.name = name
        self.cpu = cpu
        self.ram = ram
        if not servers.get(name):
            servers[name] = []
            
        heappush(servers[name],(dt, self))

def bucketize(bsize, timestamp):
    buckx = timestamp % bsize
    return timestamp - buckx

def add2bucket(last,bsize,timestamp,s):
    bucket = bucketize(bsize, timestamp)
    if not last.get(bucket):
        last[bucket] = []
    last[bucket].append((s[1].cpu, s[1].ram))


def subreport(last):
    records = []
    for k in sorted(last.keys()):
#        print 'k=%d' % k
        cputot = 0.0
        ramtot = 0.0
        lenlastdata = len(last[k])
        for b in last[k]:
            cputot += float(b[0])
            ramtot += float(b[1])
        cpuavg = cputot / lenlastdata
        ramavg = ramtot / lenlastdata
        timestr = str(datetime.datetime.fromtimestamp(k))
        print timestr, cpuavg, ramavg
        records.append((timestr,cpuavg,ramavg))

    return records

def do_report(servername):
    t = int(time.time())   # now!

    lastday = {}
    lasthour = {}
    for s in servers[servername]:
        timestamp = s[0]
        if t - 86400 < timestamp:
            add2bucket(lastday, 3600, timestamp, s)
        if t - 3600 < timestamp:
            add2bucket(lasthour, 60, timestamp, s)

    lh = subreport(lasthour)
    ld = subreport(lastday)
    return (lh, ld)

class report:
    def GET(self, servername):
        if servers.get(servername):
            (lasthour, lastday) = do_report(servername)
            r = {'servername' : servername, '1hourdata' : lasthour, '24hourdata' : lastday }
            dumper = json.dumps(r)
            print dumper
            return dumper
        else:
            print 'no such server!'
            return 'server not found'

class addserver:            
    def POST(self):
        data =  json.loads(web.data())
        #print data
        dt = int(data['dt'])
        s = Server(data['server'],float(data['cpu']),float(data['ram']),dt)
        #print 'got s: ', s.name
        return 'OK'

if __name__ == '__main__':
    app.run()
