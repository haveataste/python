import requests
import json

key = '?key=6gkESaPpDgqIVFE74oAKT227NeUlcUKJ'

#Returns information about the Shodan account linked to this API key.
#shodan账号信息
def my_account():
    url = 'https://api.shodan.io/account/profile'+key
    d = requests.get(url).json()
    for i in d.items():
        print(i)

#Use this method to obtain a list of search queries that users have saved in Shodan.
#显示API查询记录
def query_history():
    url = 'https://api.shodan.io/shodan/query'+key+'&page=1'+'&order=asc'
    d = requests.get(url).json()
    print('total:',d['total'],'\n')
    for i in d['matches']:
        for j in i.items():
            print(j)
        print()

#Returns information about the API plan belonging to the given API key.
#API计划信息
def api_info():
    url = 'https://api.shodan.io/api-info'+key
    d = requests.get(url).json()
    for i in d.items():
        print(i)

#This method returns an object containing all the protocols that can be used when launching an Internet scan.
#all the protocols
def all_protocols():
    url = 'https://api.shodan.io/shodan/protocols'+key
    d = requests.get(url).json()
    s = json.dumps(d,indent=4,sort_keys=True)
    print(len(d),'\n',s)

#This method returns a list of port numbers that the crawlers are looking for.
#all ports
def all_ports():
    url = 'https://api.shodan.io/shodan/ports'+key
    l = requests.get(url).json()
    print(len(l),l)

#--useful--
   
#Returns all services that have been found on the given host IP.
#ip主机的所有服务
def search_host():
    url = 'https://api.shodan.io/shodan/host/'
    print('please input one ip:');ip = input()#94.142.241.111
    url = url+str(ip)+key
    #print(url)
    d = requests.get(url).json()
    for key in d:
        if not isinstance(d[key],list):
            print(key,d[key],sep=':')

#Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot).
#ip主机是否是蜜罐
def honeypot():
    url = 'https://api.shodan.io/labs/honeyscore/'
    print('please input one ip:');ip = input()#94.142.241.111
    url = url+ip+key
    r = requests.get(url).text
    print(r)

#Get your current IP address as seen from the Internet.
#我的ip
def myip():
    url = 'https://api.shodan.io/tools/myip'+key
    r = requests.get(url).text
    print(r)

#Look up the IP address for the provided list of hostnames.
#域名解析
def dns():
    url = 'https://api.shodan.io/dns/resolve'
    print('please input domains:');domain = input()
    url = url+key+'&hostnames='+domain
    r = requests.get(url).text
    print(r)

#Look up the hostnames that have been defined for the given list of IP addresses.
#域名逆解析
def reverse_dns():
    url = 'https://api.shodan.io/dns/reverse'
    print('please imput ips:');ips = input()
    url = url+key+'&ips='+ips
    r = requests.get(url).text
    print(r)

#Shows the HTTP headers that your client sends when connecting to a webserver.
#显示http报文头
def headers():
    url = 'https://api.shodan.io/tools/httpheaders'+key
    d = requests.get(url).json()
    s = json.dumps(d,indent=4,sort_keys=True)
    print(s)
   
if __name__ == '__main__':
    #my_account()
    #query_history()
    #api_info()
    myip()
