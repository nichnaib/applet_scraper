#!/usr/bin/python3


import bs4
import requests
import re
import json
import dryscrape
from bs4 import BeautifulSoup 


session = dryscrape.Session()

json_filename = "../data.json"
f = open(json_filename, "w")

ids = []
with open("../links2.txt") as fr:  
  for line in fr:
    session.visit(line)
    response = session.body()
    soup = BeautifulSoup(response,'lxml')
    for i in soup.find_all("div",{"data-react-class":"App.Comps.ConnectionCard.AuthorInfo"}):
      j = i.get("data-react-props")
      d = json.loads(j)
      f.write(json.dumps(d,indent=2))
f.close()
