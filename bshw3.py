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

import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString
import re
import urllib

url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(url)
f = open('bshw3.html', "w")

soup = BeautifulSoup(r.text, "html.parser")
#f.write(soup.encode("ascii", "ignore").decode("utf-8"))
#for line in soup.find_all("a"):
for line in soup.find_all("a"): #href=re.compile("student")):
	if "student" in line.text:
		#l = line.p.string
		fixed = "***************"#line.text.replace("student", "AMAZING student")
		line.replace_with(fixed)
		print (line.text)
	# print (line.text)
	# print (line.text.encode("ascii", "ignore").decode("utf-8"))

	# f.write(lines.text.replace("student", "AMAZING student").strip().\
 #              encode("ascii", "ignore").decode("utf-8"))
	# print (str(student).encode("ascii", "ignore").decode("utf-8"))

f.close()