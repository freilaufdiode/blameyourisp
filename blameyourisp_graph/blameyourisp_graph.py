#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import warnings
import matplotlib
matplotlib.use('Agg')
try:
    import numpy as np
except:
    warnings.warn("numpy is not installed. some statistical values will not be computed")
    np = False
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import dateutil.parser
import os

try:
    from tzlocal import get_localzone
    tz = get_localzone()
except:
    try:
        import pytz
        warnings.warn("Cannot get local timezone, falling back to UTC")
        tz = pytz.utc
    except:
        warnings.warn("Neither tzlocal nor pytz installed, ignoring timezone")
        tz = None

FILE = os.path.join(os.path.expanduser("~"), ".blameyourisp", "blameyourisp.log")
LEGEND_FONTSIZE = 8
TITLE_FONTSIZE = 20

def stat( arr, label="" ):
    st = label
    _len = len(arr)
    if st != "":
        st += ": "
    st += "min: %.2f"%min(arr)
    st += ", max: %.2f"%max(arr)
    if _len > 0:
        st += ", avg: %.2f"%(sum(arr)/_len)
    if np != False:
        st += ", std: %.2f"%np.std(arr)
        st += ", var: %.2f"%np.var(arr)
    st += ", n: %d"%_len
    return st

def main():
    dates = []
    pings = []
    downs = []
    ups = []

    units = []

    isp = None
    isp_fail = False

    if not os.path.exists(FILE):
        raise Exception("File not found: %s"%FILE)

    with open(FILE, 'r') as f:
        while True:
            date = f.readline()
            if date in ("", "\n"): break

            _isp = f.readline().split(":")
            assert _isp[0] == "ISP"
            __isp = _isp[1].strip()
            if isp is None:
                if __isp not in ("", "\n"):
                    isp = __isp

            if isp is not None and __isp not in ("", "\n") and isp.split("(")[0].strip() != __isp.split("(")[0].strip():
                isp_fail = True
                warnings.warn("inconsistent ISP's detected '%s', '%s'"%(isp,__isp))

            ping = f.readline()
            _pings = ping.split(" ")

            dates.append(dateutil.parser.parse(date))
            if _pings[0] != 'Ping:':
                # some error
                downs.append(0)
                ups.append(0)
                pings.append(0)
            else:
                # test ok
                down = f.readline()
                _downs = down.split(" ")

                up = f.readline()
                _ups = up.split(" ")

                assert _downs[0] == 'Download:'
                assert _ups[0] == 'Upload:'

                if len(units) == 0:
                    units.append(_downs[2].strip())
                    units.append(_pings[2].strip())

                assert _downs[2].strip() == units[0]
                assert _ups[2].strip() == units[0]
                assert _pings[2].strip() == units[1]

                pings.append(float(_pings[1]))
                downs.append(float(_downs[1]))
                ups.append(float(_ups[1]))

    if len(dates) == 0:
        raise Exception("no data available")

    fig = plt.figure(1,figsize=(10,10),dpi=80)
    if isp_fail:
        isp = "Warning: inconsistent ISP's detected!"
    if isp is None:
        isp = "ISP not detected"
    fig.suptitle(isp, fontsize=TITLE_FONTSIZE, fontweight='bold')

    # Download + Upload
    g = fig.add_subplot(211)
    plt.ylim(0, 1.1*max(max(downs),max(ups)))
    g.plot(dates,downs,"b",label="down")
    g.plot(dates,ups,"r",label="up")
    g.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d, %H:%M', tz=tz))
    g.xaxis.grid()
    plt.ylabel("Speed [%s]"%units[0])
    plt.title("%s\n%s"%(stat(downs, "\n\ndown"), stat(ups, "up")))

    for tick in g.get_xticklabels():
        tick.set_rotation(15)

    g.legend(fontsize=LEGEND_FONTSIZE,loc=2,ncol=2)

    # Ping
    g = fig.add_subplot(212)
    plt.title(stat(pings, "ping"))
    plt.ylim(0, 1.1*max(pings))
    g.plot(dates,pings,"g",label="ping")
    g.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d, %H:%M', tz=tz))
    g.xaxis.grid()
    plt.ylabel("Latency [%s]"%units[1])

    for tick in g.get_xticklabels():
        tick.set_rotation(15)

    g.legend(fontsize=LEGEND_FONTSIZE,loc=2)

    plt.tight_layout()

    plt.savefig( os.path.join(os.path.expanduser("~"), 'blameyourisp.png'))
    plt.close()

if __name__ == "__main__":
    main()

