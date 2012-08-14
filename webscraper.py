#http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows

import urllib2
import os
from BeautifulSoup import BeautifulSoup
from xml.etree import ElementTree as ET

#Set output files
to_file = "listofimages.html"
out_file= open(to_file, 'w')

#Open and read URL
url = "http://www.bbc.co.uk/"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

#Find images
pictures = soup.findAll('img')

#Create HTML
root_element = ET.Element("body")

ul = ET.SubElement(root_element, "ul")

for eachpicture in pictures:
	picturesrc = eachpicture['src']
	li = ET.SubElement(root_element, "li")
	a = ET.SubElement (li, "a")
	img = ET.SubElement (a, "img")
	img.set("src",picturesrc)

#Save file
out_file.write(ET.tostring(root_element))
out_file.close()


"""
url="http://www.utexas.edu/world/univ/alpha/"

page=urllib2.urlopen(url)

soup = BeautifulSoup(page.read())

universities=soup.findAll('a',{'class':'institution'})

for eachuniversity in universities:
    print eachuniversity['href']+","+eachuniversity.string

 """