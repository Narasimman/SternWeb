#!/usr/bin/python

import commands

print "Content-Type:text/html"
print
status, lsresults = commands.getstatusoutput('ls')
print lsresults
