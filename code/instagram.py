import urllib2
import re


def get_ins_username(pic_link):
	web_page = urllib2.urlopen(pic_link).read()
	return re.search('"owner": {"username": "(.*)", "is_unpublished"', web_page).groups()[0]