#!/usr/bin/python

import subprocess, shlex, sys, getopt, os
import whois
from datetime import datetime
from sys import argv,exit

def main(argv):
   os.system('clear')
   global domain
   domain = ''

   # Gather args
   try:
      opts, args = getopt.getopt(argv,"hd:",["ifile="])
   except getopt.GetoptError:
      print 'zonecheck.py -d <domain.com>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'zonecheck.py -d <domain.com> -h'
         sys.exit()
      elif opt in ("-d", "--domain"):
         domain = arg
   
   # Run lookups
   #checkzone(domain)
   print 'Checking records on zone : ' + domain
   print '--------------------------------------'
   checkdig('a','',domain)
   checkdig('a','www',domain)
   checkdig('a','backup',domain)
   checkdig('ns','',domain)
   checkdig('txt','',domain)
   checkdig('mx','',domain)
   checkexpiry(domain)
   
def checkdig (digtype,digprefix,domain):
   if digprefix:
      cmd='dig ' + digtype + ' ' + digprefix + '.' + domain + ' +short'
   else:
      cmd='dig ' + digtype + ' ' + domain + ' +short'
   print (cmd)
   proc=subprocess.Popen(shlex.split(cmd),stdout=subprocess.PIPE)
   out,err=proc.communicate()
   print (out)

def checkexpiry (d):
   # Code in this function borrowed from https://github.com/averi/python-scripts/blob/master/check-domain-expiration.py
   now = datetime.now()
   try:
       w = whois.whois(d)
   except whois.parser.PywhoisError as e:
       print e
       exit(1)

   if type(w.expiration_date) == list:
       w.expiration_date = w.expiration_date[0]
   else:
       w.expiration_date = w.expiration_date

   domain_expiration_date = str(w.expiration_date.day) + '/' + str(w.expiration_date.month) + '/' + str(w.expiration_date.year)
   timedelta = w.expiration_date - now
   days_to_expire = timedelta.days


# Main Program Function
if __name__ == "__main__":
   # Send all args to main function
   main(sys.argv[1:])


