import urllib2
import re
import json


def get_ins_username(pic_link):
	web_page = urllib2.urlopen(pic_link).read()
	return re.search('"owner": {"username": "(.*)", "is_unpublished"', web_page).groups()[0]


def get_locations(ins_name):
    web_page = urllib2.urlopen("https://www.instagram.com/%s/media/"%ins_name).read()
    jdata = json.loads(web_page)['items']
    locations = []
    for i in jdata:
        try:
            locations.append(i['location']['name'])
        except:
            pass
    return locations