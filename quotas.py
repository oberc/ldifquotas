#! /usr/bin/python3

class User:
  def __init__(self, uid, uidnum, quota):
    self.uid = uid
    self.uidnum = uidnum
    self.quota = quota
    
  def getquota(self):
    return self.quota
    
    
def main(addr, passwd, binddn, base):
  print("Querying LDAP Server %s..." %addr)
  cmdline = ['ldapsearch',  '-x', '-LLL', '-D %s' % binddn, '-b %s' % base, '-H %s' %addr, '-w %s' % passwd]
  try: 
    rawldif = Popen(cmdline, shell=True, stdout=PIPE, stderr=STDOUT, executable='/bin/bash')
    out = rawldif.stdout.read()
    print(out)
  except TypeError as err:
    print("%s\nCould not query LDAP Server `%s`" % (err, addr))
  except:
    print("Unhandled exception %s\nCould not query LDAP Server `%s`" % (sys.exc_info(), addr))

if __name__ == '__main__':
  from subprocess import (PIPE, STDOUT, Popen, check_output)
  import sys
  
  readcfg = open('serverinfo.conf', 'r')
  server  = readcfg.readline().strip('\n')
  passwd  = readcfg.readline().strip('\n')
  binddn  = readcfg.readline().strip('\n')
  base    = readcfg.readline().strip('\n')
  readcfg.close()
  main(server, passwd, binddn, base)