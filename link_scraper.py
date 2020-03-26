#!/usr/bin/python3

import bs4
import requests
import re
import dryscrape
import json
from bs4 import BeautifulSoup 

res = requests.get('https://ifttt.com/services')
soup = BeautifulSoup(res.text, 'lxml')
orig = "https://ifttt.com"
 
# file with links of services
filename = "links.txt"
fo = open(filename, "w")

# file with links of applets
filename2 = "links2.txt"
fo2 = open(filename2, "w")


links = []
links2 = []
list_of_services = []

supporto = []
for tag in soup.find_all('section'):
# just searching for particular services, remove if want to scrape all the services
  try:
    if "Blogging" == tag.h3.text:
      for link in tag.find_all('a', href = True):
        link_url = link.get('href')
        if ":" not in link_url:
          if "500px" not in link_url:
            if "source=" not in link_url:
              link_url = orig + link_url
              links.append(link_url)
              fo.write(link_url)
              fo.write('\n')  
    if "Cloud storage" == tag.h3.text:
      for link in tag.find_all('a', href = True):
        link_url = link.get('href')
        if ":" not in link_url:
          if "500px" not in link_url:
            if "source=" not in link_url:
              link_url = orig + link_url
              links.append(link_url)
              fo.write(link_url)
              fo.write('\n')
    if "Communication" == tag.h3.text:
      for link in tag.find_all('a', href = True):
        link_url = link.get('href')
        if ":" not in link_url:
          if "500px" not in link_url:
            if "source=" not in link_url:
              link_url = orig + link_url
              links.append(link_url)
              fo.write(link_url)
              fo.write('\n')
    if "Email" == tag.h3.text:
      for link in tag.find_all('a', href = True):
        link_url = link.get('href')
        if ":" not in link_url:
          if "500px" not in link_url:
            if "source=" not in link_url:
              link_url = orig + link_url
              links.append(link_url)
              fo.write(link_url)
              fo.write('\n') 
    if "Location" == tag.h3.text:
      for link in tag.find_all('a', href = True):
        link_url = link.get('href')
        if ":" not in link_url:
          if "500px" not in link_url:
            if "source=" not in link_url:
              link_url = orig + link_url
              links.append(link_url)
              fo.write(link_url)
              fo.write('\n')
    if "Notifications" == tag.h3.text:
      for link in tag.find_all('a', href = True):
        link_url = link.get('href')
        if ":" not in link_url:
          if "500px" not in link_url:
            if "source=" not in link_url:
              link_url = orig + link_url
              links.append(link_url)
              fo.write(link_url)
              fo.write('\n')              
    if "Photo & video" == tag.h3.text:
      for link in tag.find_all('a', href = True):
        link_url = link.get('href')
        if ":" not in link_url:
          if "500px" not in link_url:
            if "source=" not in link_url:
              link_url = orig + link_url
              links.append(link_url)
              fo.write(link_url)
              fo.write('\n')
    if "Social networks" == tag.h3.text:
      for link in tag.find_all('a', href = True):
        link_url = link.get('href')
        if ":" not in link_url:
          if "500px" not in link_url:
            if "source=" not in link_url:
              link_url = orig + link_url
              links.append(link_url)
              fo.write(link_url)
              fo.write('\n')
  except:
    continue

session = dryscrape.Session()

# for each link in links.txt
for j in range(len(links)): 
  session.visit(links[j])
  response = session.body()
  new_soup = BeautifulSoup(response,'lxml')
  for t in new_soup.find_all('section', {'class': 'service-header'}):
    if t is not None:
      service = t.h1.text
  # for each applet of that link
  for l in new_soup.find_all('a', href = True):
    href = l.get("href")
    if "/applets/" in href:
      link2 = orig + href
      links2.append(link2)
      supporto.append(service)
      fo2.write(link2)
      fo2.write("\n")

"""
# for only one link, for faster testing
session.visit(links[0])
response = session.body()
new_soup = BeautifulSoup(response,'lxml')
for t in new_soup.find_all('section', {'class': 'service-header'}):
  if t is not None:
    service = t.h1.text
for l in new_soup.find_all('a', href = True):
  href = l.get("href")
  if "/applets/" in href:
    link2 = orig + href
    links2.append(link2)
    supporto.append(service)
"""

fo2.close()      
fo.close()
