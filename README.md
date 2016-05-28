# Blame you ISP
blameyourisp is a simple tool which makes a speedtest every 15 minutes and plots a graph to visualize your ISP's performance, helpful to spot deviations of your internet speed based on certain daytimes.

![Screenshot](https://github.com/freilaufdiode/blameyourisp/blob/master/screenshot.png)

## Software Dependencies
* [speedtest-cli](https://github.com/sivel/speedtest-cli)
* python (>=2.7 or 3.x)
* python-matplotlib
* python-dateutil
* python-setuptools

### optional Dependencies
* python-requests (for isp detection via [ip-api.com](http://ip-api.com))
* python-numpy (for some statistical values)
* python-pytz or python-tzlocal (for timezone detection)

## Hardware Dependencies
A unix or windows machine with appropriate uptime, connected via cable to your router/modem.

## Setup
most dependencies should be met by your distributions package management system, others can be installed with pip.

Download the sourcecode and run `python setup.py install` as root.

### Unix
blameyourisp does not ship with an init-script, but you could start it manually in the background:  
`nohup blameyourisp > /dev/null 2>&1 &`  
or put it in your /etc/rc.local (systemd users see [here](http://superuser.com/questions/278396/systemd-does-not-run-etc-rc-local)):  
`su - USER -c blameyourisp &`  
(replace USER by your own username)  
or, additionally to above suggestions, launch it inside screen or tmux  

### Windows
You could add a link to your Autostart-Folder, eg. from c:\PythonXX\Scripts\blameyourisp.exe  
Dont close the terminal window or the tool will stop (please let me know if you have a better solution!).  
The first test may fail if your network connection is not yet up - just ignore the ConnectionError.

## Usage
Once set up correctly, results from speedtests will be recorded in ~/.blameyourisp/blameyourisp.log. After each test, a new plot will be saved to ~/blameyourisp.png (probably /home/USER/ or c:\Users\USER)

## Bugs
blameyourisp is beta software and has not yet been tested exhaustively. If you experience any issues, or have any suggestions/ideas/questions/whatever, do not hesitate to contact me!

* if a test fails for any reason (may it be you aren't connected to internet, or your ISP is gone at all), that fact is currently not considered in the plots. Future versions might take this into concern.
* if there is only one testresult available, no lines will be plotted in the graph. You still will be able to see the values in the title of each plot.

## Notes
* Speedtests are influenced by active traffic (downloads, streams, etc). Traffic generated by flatmates also impacts speedtest results!
* Use a LAN-cable instead of a wireless connection for accurate results.
* Dont run multiple instances of blameyourisp in the same network.
* When using on mobile computers, stop the tool when you leave your home.
* See [github.com/sivel/speedtest-cli#inconsistency](https://github.com/sivel/speedtest-cli#inconsistency)

