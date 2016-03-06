#!/usr/bin/python
#
#  This is a cgi program (hw3.cgi) that can be used to list the contents of a users websys directory
#
#  It must be named hw3.cgi and have world read access in order to work.
# This is due o security restrictions on the Stern systems that
# will only allow execution of programs named .cgi
#
# the input is the netid of the user, provided by a form with a fieldname of userid
# The program then constructs the path to the users directory
# Stern student directories are located at:
# /homedir/grad/FCHAR/NETID/
# and their websys directories are located at:
# /homedir/grad/FCHAR/NETID/public_html/websys
# where FCHAR is the first character of the netid and NETID is the netid.
#
# import the cgi modules to be able to retrive the form parameters
import cgi, cgitb
#import the commands module to let us execute unix commands
# and retrieve the results

import commands


        

# print the html headers to standard output
print "Content-type:text/html"
print ""
print 
print '<head>'
print '<title>'
print 'Contents of a users websys directory'
print '</title>'
print '<link rel="stylesheet" href="css/bootstrap.min.css">'
print '</head>'
print '<body>'
print '<div style="margin:10% auto; width : 960px;">'

form=cgi.FieldStorage()

if "userid" not in form:
   print "<H1>Error</H1>"
   print "userid field not provided"
# retrieve the value of the userid field from the form
Userid =form["userid"].value
webSysPath = "/homedir/grad/" + Userid[0] + "/"  + Userid + "/public_html/websys"
print '<h2>List of user ' + Userid + "'s" + ' websys directory</h2>'

lscommand = 'ls ' + webSysPath


print '<table class="table table-striped">'
print '<th>Contents</th>'
status,lsresults = commands.getstatusoutput(lscommand)
arr = lsresults.split("\n")

if status == 0:
    for res in arr:
	filepath = "/~" + Userid + "/websys/" + res
        print "<tr><td><a href='" + filepath + "'>" + res + "</a></td></tr>"
else:
    print "Not a valid userid. Please enter a valid user id."

print '</table>'
print '</div>'
print '</body>'
print '</html>'

