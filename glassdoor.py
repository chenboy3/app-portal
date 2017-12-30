import requests
import json
import config
from flask import request

req_url = 'http://api.glassdoor.com/api/api.htm?v='

def getCompanies(name):
    url = buildURL('1', 'json', config.id, config.key, 'employers', '75.104.65.154',
    request.user_agent.string,
    name)
    #print(url)
    return requests.get(url, headers = {"User-Agent": request.user_agent.string})

def buildURL(v, format, tp, tk, action, userip, useragent, searchterm):
    return (req_url + v + "&format=" + format + "&t.p=" + tp + "&t.k=" + tk +
         "&action=" + action + "&q=" + searchterm + "&userip=" + userip +
         "&useragent=" + useragent)

def getLogo(company):
    response = getCompanies(company).json()
    # Invalid search
    if len(response['response']['employers']) == 0:
        return None
    #print(response['response']['employers'][0])
    res = response['response']['employers'][0]
    return (res['squareLogo'], res['name'], res['website'], res['overallRating'], res['industry'])
    # name, website, overallRating, industry,
    #return "http://i.imgur.com/6E2694O.gifv"

# Change this to be more extensible
def getFiveCompanies(company):
    response = getCompanies(company).json()
    result = []
    for employer in response['response']['employers']:
        result.append(employer['name'])
        if len(result) == 5:
            break
    return result
