from bs4 import BeautifulSoup
import re

#Try to sort them by quarter taken
def getSchedule():
    classes = getClasses()
    schedule = dict()
    for requirement in classes.keys():
        for class1 in classes[requirement][0]:
            quarter = class1[0:4]
            #this is honestly the greatest line of code ever

            #Tries to append to the specific quarter list of classes
            try:
                schedule[quarter].append(class1[5:])
            #If the list of classes hasn't been initialized, initialize it
            except:
                schedule[quarter] = [class1[5:]]
    return schedule;


def getClasses():
    def getIndex(index):
        return visible_text.index(reqList[index][0]+" "+reqList[index][1])
    soup = BeautifulSoup(open('UCSD Degree Audit Report.html'), 'html.parser')

    categories = soup.find_all("font")
    requirements = dict()
    reqList = list()
    #Looking for things like 1) CSE REQ or maybe > 2) Statistics - Reqd
    # FIX THIS
    valid = re.compile(r".*([1-9]+\))\s([^-]+).*$")
    for req in categories:
        if req.string is not None:
            regexResult = valid.match(req.string)
            if regexResult is not None:
                reqList.append(regexResult.groups())
    #print reqList

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

    return requirements

# [Name, PID, College, UC GPA, Total Units Completed, UC Graded Units, Major]
def getHeaderInfo():
    soup = BeautifulSoup(open('UCSD Degree Audit Report.html'), 'html.parser')
    header = (soup.find_all("tbody"))[0]
    headerList = []

    #abusing BeautifulSoup dom capabilities
    name = header.find_all(string=re.compile("Name"))
    namestring = unicode(name[0].parent.next_sibling.contents[0]).strip()
    commaIndex = namestring.find(',')
    formattedName = namestring[commaIndex + 2:] + ' ' + namestring[:commaIndex]
    headerList.append(formattedName)
    pid = header.find_all(string=re.compile("PID"))
    headerList.append(pid[0].parent.next_sibling.contents[0])
    college = header.find_all(string=re.compile("College"))
    headerList.append(college[0].parent.next_sibling.contents[0])
    ucgpa = header.find_all(string=re.compile("UC GPA"))
    headerList.append(ucgpa[0].parent.next_sibling.contents[0])
    tunits = header.find_all(string=re.compile("Total Units"))
    headerList.append(tunits[0].parent.parent.next_sibling.contents[0].contents[0])
    ucunits = header.find_all(string=re.compile("UC Graded Units"))
    headerList.append(ucunits[0].parent.next_sibling.contents[0])
    major = header.find_all(string=re.compile("Major"))
    headerList.append(major[0].parent.next_sibling.contents[0])

    return headerList
