#!/usr/bin/python

#This is a python script for my navigation

groups = []

class group:
	g_id = -1
	g_name = ""
	items = []

	def __init__(self, id, name):
		self.g_id = id
		self.g_name = name

	def add_item(self, item):
		self.items.append(item)
		print "add"

	def del_item(self,item):
		self.items.remove(item)

	def clear():
		print "Clear items"

class item:
	id = -1
	name = ""
	url = ""
	def __init__(self, id, name, url):
		self.id = id
		self.name = name
		self.url = url
		print "init"

	def set_name(self, name):
		self.name = name

def info():
	for group in groups:
		print group.g_id,group.g_name
		for item in group.items:
			print item.id,item.name,item.url

if __name__ == '__main__':
	item1 = item(1, "qq", "http://www.qq.com")
	group1 = group(1, "test")
	group1.add_item(item1)
	group1.add_item(item1)
	group1.add_item(item1)
	group1.add_item(item1)
	group1.add_item(item1)
	groups.append(group1)
	info()