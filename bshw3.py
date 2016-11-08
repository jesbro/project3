# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

'''
References: 
http://stackoverflow.com/questions/28516928/how-do-you-replace-specific-characters-in-beautifulsoup?rq=1
'''

import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString
import re
import urllib

url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(url)
f = open('bshw3.html', "w")

soup = BeautifulSoup(r.text, "html.parser")

#to change students to AMAZING students
for line in soup.find_all("a"):
	if "student" in line.text:
		line.string = re.sub(r'student', r'AMAZING student', line.string)

for line2 in soup.find_all("p"):
	if "student" in line2.text:
		line2.string = re.sub(r'student', r'AMAZING student', line2.text)

#replaces main pic with one of my own
for img in soup.find_all("img"):
	if img.get('alt') == None:
		img['src'] = open("loco.jpg")
		print (img)




f.write(soup.encode("ascii", "ignore").decode("utf-8"))
f.close()