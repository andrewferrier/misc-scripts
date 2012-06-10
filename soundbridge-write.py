#!/usr/bin/python
#
# $Id$

"""
Write some text on a Roku soundbridge, using the telnet interface.
"""

import telnetlib
import syslog

from optparse import OptionParser

parser = OptionParser()

parser.add_option("-H", "--hostname", dest="hostname", default="soundbridge")
parser.add_option("-t", "--text", dest="text", default="use the --text option to set the text to display")

(options, args) = parser.parse_args()

port = 4444

syslog.openlog("soundbridge-write")

tn = telnetlib.Telnet(options.hostname, port)

tn.read_until("SoundBridge> ")
tn.write("sketch\n")
tn.read_until("sketch> ")
tn.write("font 10\n")
tn.read_until("sketch> ")
syslog.syslog("Writing '" + options.text + "' on the soundbridge at hostname '" + options.hostname + "'")
tn.write("text 0 0 \"" + options.text + "\"\n")
while 1 == 1:
    pass
tn.close()
