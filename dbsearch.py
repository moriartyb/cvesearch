#!/usr/bin/python
import xml.sax
import gzip
import urllib2
import os
GZIP_CVE ="http://cve.mitre.org/data/downloads/allitems.xml.gz"
localCVE = None
def getCVE():
	if not os.path.isfile('cves.xml'):
		localCVE = open('cves.xml','wb')
		gzFile = urllib2.urlopen(urllib2.Request(GZIP_CVE)).read()
		localGZ = open('cves.gz','wb')
		localGZ.write(gzFile)
		localGZ.close()
		cveg = gzip.open('cves.gz','rb')
		cve = cveg.read()
		localCVE.write(cve)
		return cve

def cleanup():
	if localCVE:
		localCVE.close()



print "Getting CVE..."
cveXML = getCVE()

cleanup()
