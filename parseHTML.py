from bs4 import BeautifulSoup
import re

def getIndex(index):
    return visible_text.index(reqList[index][0]+" "+reqList[index][1])

soup = BeautifulSoup(open('degree.htm'), 'html.parser')

categories = soup.find_all("font")
requirements = dict()
reqList = list()
#Looking for things like 1) CSE REQ or maybe > 2) Statistics - Reqd
valid = re.compile(r".*([1-9]+\))\s([^-]+).*$")
for req in categories:
    if req.string is not None:
        regexResult = valid.match(req.string)
        if regexResult is not None:
            reqList.append(regexResult.groups())

[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
visible_text = soup.getText()
index = 0

takenCourses = re.compile(r"((?:FA|SP|WI)(?:15|16|17))\s([A-Z]{3,4}\s+[0-9]{1,3}[A-Z]*)")
missingReq = re.compile(r"\nNeeds:\s+([1-9]+)\sCourses\n")
for index in range(1,len(reqList)):
    #Going to have the requirements be (takenCourses, missingCourses)
    requirements[reqList[index-1][1]] = [[],0]
    stringSegment = visible_text[getIndex(index-1):getIndex(index)]
    regexResult = takenCourses.findall(stringSegment)
    for result in regexResult:
        #Add to the taken courses
        requirements[reqList[index-1][1]][0].append(result[0] + " " + result[1])
    regexResult = missingReq.search(stringSegment)
    if regexResult is not None:
        requirements[reqList[index-1][1]][1] = int(regexResult.groups()[0])
