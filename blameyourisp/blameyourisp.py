#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import print_function
import os, sys, traceback

try:
    import requests
except:
    requests = False

import json
import datetime
import time
import subprocess
from subprocess import CalledProcessError

path = os.path.join( os.path.expanduser("~"), ".blameyourisp" )

if not os.path.exists( path ):
    os.makedirs( path )

logfile = os.path.join( path, "blameyourisp.log" )
SLEEP=15 # minutes
isp_url="http://ip-api.com/json"

def isp():
    if requests != False:
        r = requests.get( isp_url ).json()
        return "ISP: %s (%s/%s, %s)"%(r['isp'], r['country'], r['city'], r['zip'])
    return "ISP: cannot determine ISP"

def main():
    while True:
        try:
            error = False

            date = datetime.datetime.utcnow().isoformat()
            _isp = isp()

            try:
                out = str( subprocess.check_output( ("speedtest-cli", "--simple"), universal_newlines=True ) )
            except CalledProcessError:
                traceback.print_exc( file=sys.stdout )
                error = True

            if not error:
                with open( logfile, "a") as f:
                    f.write( "%s\n%s\n%s"%(date, _isp, out) )
                print( "%s\n%s\n%s"%(date, _isp, out) )
                subprocess.call( "blameyourisp-graph" )
        except:
            traceback.print_exc( file=sys.stdout )

        time.sleep( 60 * SLEEP )

if __name__ == '__main__':
    main()

