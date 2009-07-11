import libxml2
import pycurl
import sys
import os

def parse_xml(code):
  doc = libxml2.parseDoc(code)
  ctxt = doc.xpathNewContext()
  ctxt.xpathRegisterNs('x', "http://www.w3.org/1999/xhtml")
  for found in ctxt.xpathEval("//x:div[@class='linkinfo']/x:a"):
    print found.getContent()

def drop_file(file):
  c = pycurl.Curl()
  c.setopt(c.HTTPPOST, [('drop', (c.FORM_FILE, file))])
  c.setopt(c.URL, "http://fdrop.it")
  c.setopt(c.FOLLOWLOCATION, 1)
  c.setopt(c.WRITEFUNCTION, parse_xml)
  c.perform()
  c.close()

if __name__ == '__main__':
  if len(sys.argv) >= 2:
    f = sys.argv[1]
    if os.path.isfile(f):
      drop_file(f)
    else:
      print sys.argv[0] + ": " + f + ": No such file"
  else:
    print "usage: " + sys.argv[0] + " name"
