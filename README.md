


# Domain Dig

A command line tool for checking domain information, written in python

* Finds A,MX records, Name server and Domain Registrar
* Can use URLs/E-mail IDs as input.
* Color scheme for readability

Install
------

```bash
git clone https://github.com/saviojoy20/ipk_ip-API.git
cd ipk_ip-API
pip3 install -r requirements.txt
```
copy the file "sig" to any of the locations in the "PATH" variable


Usage
-----
```
sig https://google.com/page1
```
```
sig google.com
```

Sample Output
---------

```console
-HP:~$ sig https://google.com/testpage

Extracted Root Domain Name ::  google.com

--IP-- :: www.google.com
142.250.195.164

--MAIL SERVER-- :: google.com
20 alt1.aspmx.l.google.com.
30 alt2.aspmx.l.google.com.
40 alt3.aspmx.l.google.com.
10 aspmx.l.google.com.
50 alt4.aspmx.l.google.com.

--IP-- :: google.com
142.250.182.110

REGISTRAR :::: MarkMonitor, Inc.
NAME SERVER
NS1.GOOGLE.COM NS2.GOOGLE.COM NS3.GOOGLE.COM NS4.GOOGLE.COM ns3.google.com ns4.google.com ns2.google.com ns1.google.com 
Total  time: 2.1054553985595703

```


Tool is in test phase.

The order in which threads are run is determined by the operating system and can be quite hard to predict. The order of the output may (and likely will) vary from run to run



