#!/usr/bin/python3

import datetime
import whois
import pydig
import sys
import tldextract
import time
import threading
from colorama import Fore, Back, Style

#command line  tool for domain lookup, finds A,MX, Name servers, Registrar


start = time.time()

#function for whois lookup, finding registrar and nameservers

def whoislkup(domain):
  w = whois.whois(domain)
  print(Fore.BLUE+"REGISTRAR :::: "+Fore.WHITE+w.registrar)
  # print("Name servers :::: {}".format(w.name_servers))
  print(Fore.BLUE+"NAME SERVER"+Fore.WHITE)
  # print(w)
  try:
    for i in w.name_servers:
        print(i,end = " ")
  except Exception as e:
    print("Error")      
  


#function to find  records of the domain
def iplkup(domain,record):
  # IP of  domain 
  ip = pydig.query(domain, record)
  if record=="MX":
    print(Fore.BLUE+"--MAIL SERVER-- :: "+domain)
  else:
    print(Fore.BLUE+"--IP-- :: "+domain)
  for j in ip:
     print("{}".format(Fore.WHITE+j))
  print(Style.RESET_ALL)


#getting  arguments
domain =  str(sys.argv[1])



#parsing domain  from argument.
domain = tldextract.extract(domain)
subdomain =  domain[0]
domain = '.'.join(domain[-2:])
print("\nExtracted Root Domain Name ::  {}\n".format(Fore.RED+domain))




#creating  thread object
t_whoislkup = threading.Thread(target=whoislkup,args=(domain,))
t_iplkup = threading.Thread(target=iplkup,args=(domain,"A"))
t_mxlkup = threading.Thread(target=iplkup,args=(domain,"MX"))

#starting thread
t_whoislkup.start()
t_iplkup.start()
t_mxlkup.start()



#checking if the subdomain is www or not
if subdomain=="www" or not subdomain:
  subdomain="www."+domain
  t_Sub_iplkup = threading.Thread(target=iplkup,args=(subdomain,"A"))
  t_Sub_iplkup.start() 
else:
  
  subdomain= subdomain+"."+domain
  t_Sub_iplkup = threading.Thread(target=iplkup,args=(subdomain,"A"))
  t_Sub_iplkup.start() 


t_whoislkup.join()
t_Sub_iplkup.join()
t_mxlkup.join()
t_iplkup.join() 


end = time.time()
total = end -start
print('\nTotal  time: {}'.format(total))

