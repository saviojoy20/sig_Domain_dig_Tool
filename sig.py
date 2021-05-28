#!/usr/bin/python3
import socket
import ssl
import datetime
import whois
import pydig
import sys
import tldextract
import time
import threading


start = time.time()

#function for whois lookup, finding registrar and nameservers
def whoislk(domain):
  w = whois.whois(domain)
  print("\nREGISTRAR :::: {} ".format(w.registrar))
  # print("Name servers :::: {}".format(w.name_servers))
  print("\nNAME SERVER")
  # print(w)
  try:
    for i in w.name_servers:
        print(i,end = " ")
  except Exception as e:
    print("Error")      
  


#function to find  A record of domain
def iplk(domain):
  # IP of  domain 
  ip = pydig.query(domain, 'A')
  print("\n--IP--  {}".format(domain))
  for j in ip:
     print("{}".format(j))


#function to find  A record  subdomain
def iplks(domain):
  # IP of  domain 
  ip = pydig.query(domain, 'A')
  print("\n--IP--  {}".format(domain))
  for j in ip:
     print("{}".format(j))

#function  to find the MX record of the domain
def mxlk(domain):
# mx records 
 mxadd= pydig.query(domain, 'MX')
 print("\nMAIL SERVER")
 for l in mxadd:
    print(l)


#function to find SSL and it exp date
def ssl_expiry_datetime(hostname):
    try:  
        ssl_dateformat = r'%b %d %H:%M:%S %Y %Z'

        context = ssl.create_default_context()
        context.check_hostname = False

        conn = context.wrap_socket(
            socket.socket(socket.AF_INET),
            server_hostname=hostname,
        )
        # 5 second timeout
        conn.settimeout(5.0)

        conn.connect((hostname, 443))
        ssl_info = conn.getpeercert()
        # Python datetime object
        # return datetime.datetime.strptime(ssl_info['notAfter'], ssl_dateformat,ssl_info['subjectAltName'])
        
        #parsing SSL infomrations
        
        # common=ssl_info['subject']

        # common=common[0][0]
        # c,d =common
        # print("Common Name: {}".format(d))
        

        # #printing SAN
        # print("\n------SAN-----")
        # for i in ssl_info['subjectAltName']:
        #     a,b = i
        #     print(b)
        # print("--------------")

        #finds the remaining expiration days
        now = datetime.datetime.now()
        expire = datetime.datetime.strptime(ssl_info['notAfter'], ssl_dateformat)
        diff = expire - now
        print ("\nDomain name: {} \tSSL Expiry Date: {} \tSSL Expiry Day: {}".format(hostname,expire.strftime("%Y-%m-%d"),diff.days))
    except Exception as e:
        print (e)
 

 

#getting function from arguments
domain =  str(sys.argv[1])



#parsing domain and subdomain from argument.
domain = tldextract.extract(domain)
subdomain =  domain[0]
domain = '.'.join(domain[-2:])


t_whoislk = threading.Thread(target=whoislk,args=(domain,))
t_iplk = threading.Thread(target=iplk,args=(domain,))
t_mxlk= threading.Thread(target=mxlk,args=(domain,))
# t_ssl_expiry_datetime= threading.Thread(target=ssl_expiry_datetime,args=(domain,))

if subdomain=="www" or not subdomain:
  subdomain="www."+domain
  t_iplksub = threading.Thread(target=iplks,args=(subdomain,))
  t_iplksub.start() 
else:
  
  subdomain= subdomain+"."+domain
  t_iplksub = threading.Thread(target=iplks,args=(subdomain,))
  t_iplksub.start() 




t_whoislk.start()
t_iplk.start()
t_mxlk.start()
# t_ssl_expiry_datetime.start()

t_whoislk.join()
t_iplk.join()
t_mxlk.join()
t_iplksub.join() 
# t_ssl_expiry_datetime.join()



end = time.time()
total = end -start
print('\nTotal  time: {}'.format(total))

