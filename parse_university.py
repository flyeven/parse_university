# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 11:50:03 2016

@author: chero
"""

"""
parse university name on the site http://www.4icu.org/
"""


import re
import urllib.request
from  bs4 import BeautifulSoup 

page_name=['0001']+[str(i) for i in range(2,28)] 
'''
from '0001'(0-9),'2'(A),'3'(B) to '27'(Z)
'''
page_university=[]
page=page_name[0:28]
for item_page_name in page:
    url="http://www.4icu.org/reviews/index"+item_page_name+".htm"
    htmlpage = urllib.request.urlopen(url).read()
    htmlpage = htmlpage.decode('utf-8')
    soup = BeautifulSoup(htmlpage)
    body = soup.body
    list_university=body.find_all('table',{"width":"100%",'align':'center','cellspacing':'3'})[0]
    for link in list_university.find_all('a'):
        temp=link.get("href")
        page_university.append(temp)
        print(item_page_name,temp)

'''
item_page_university like '/reviews/5009.htm'
'''
university_name=[]
university_city=[]
university_region=[]
university_country=[]
error=[]
for item_page_university in page_university:
    try:
        url="http://www.4icu.org"+item_page_university
        htmlpage = urllib.request.urlopen(url).read()
        htmlpage = htmlpage.decode('utf-8')
        soup = BeautifulSoup(htmlpage)
        body = soup.body
        b=body.find_all('div',{"class":"section group"})
        #find name
        temp_name=b[2].find_all('b')
        print(temp_name)
        pat1=re.compile(r'<b>(.*?)</b>',re.IGNORECASE)
        university_name.append(pat1.findall(str(temp_name))[0])
        #find address
        temp_address=b[8].find_all('table',{"width":'100%',"cellpadding":'3'})[0]
        pat2=re.compile(r'<h5>(.*?)</h5>',re.IGNORECASE)
        address=pat2.findall(str(temp_address.tr))
        university_city.append(address[1])
        university_region.append(address[2])
        university_country.append(address[3])
    except:
        error.append(item_page_university)
        print(item_page_university,'not found!')
        

with open('university_info'+'.txt','wt')as f:
    for i in range(0,len(university_name)):
        row=university_name[i]+'\t'+university_city[i]+'\t'+university_region[i]+'\t'+university_country[i]
        f.write(row+'\n')
with opne('error.txt','wt') as f:
    for item in error:
        f.write(item+'\n')


    
        
    
