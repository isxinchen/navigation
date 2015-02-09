#!/usr/bin/env python
# coding=utf-8

#This is a python script for my navigation

#spawn-fcgi -d /home/chenxin/work/git/navigation/ -f /home/chenxin/work/git/navigation/navigation.py -a 127.0.0.1 -p 9002


import web

groups = []
urls = ("/", "hello",
	"/api/addgroup(.+)", "addgroup",
	"/api/delgroup(.+)", "delgroup",
	"/api/editgroup(.+)", "editgroup",
	"/api/additem(.+)", "additem",
	"/api/delitem(.+)", "edititem",
	"/api/editgroup(.+)", "editgroup")
app = web.application(urls, globals())

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

class hello:
    def GET(self):
        return 'Hello, world!'
    
    if __name__ == "__main__":
        web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
        app.run()

class addgroup(object):
	"""docstring for ClassName"""
	# def __init__(self, arg):
		# super(ClassName, self).__init__()
		# self.arg = arg
	def GET(self):
		return "add group"

class delgroup(object):
	"""docstring for ClassName"""
	# def __init__(self, arg):
		# super(ClassName, self).__init__()
		# self.arg = arg
	def GET(self):
		return "del group"

class editgroup(object):
	"""docstring for ClassName"""
	# def __init__(self, arg):
		# super(ClassName, self).__init__()
		# self.arg = arg
	def GET(self):
		return "edit group"

class additem(object):
	"""docstring for ClassName"""
	# def __init__(self, arg):
		# super(ClassName, self).__init__()
		# self.arg = arg
	def GET(self):
		return "add item"

class delitem(object):
	"""docstring for ClassName"""
	# def __init__(self, arg):
		# super(ClassName, self).__init__()
		# self.arg = arg
	def GET(self):
		return "del item"

class edititem(object):
	"""docstring for ClassName"""
	# def __init__(self, arg):
		# super(ClassName, self).__init__()
		# self.arg = arg
	def GET(self):
		return "edit item"

def info():
	for group in groups:
		print group.g_id,group.g_name
		for item in group.items:
			print item.id,item.name,item.url

def parser():
	pass

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