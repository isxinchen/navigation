#!/usr/bin/env python
# coding=utf-8

#This is a python script for my navigation

#spawn-fcgi -d /home/chenxin/work/git/navigation/ -f /home/chenxin/work/git/navigation/navigation.py -a 127.0.0.1 -p 9002


import web
import json
import db


groups = []
urls = ("/", "hello",
	"/api/getall", "hello",
	"/api/addgroup/", "addgroup",
	"/api/delgroup/", "delgroup",
	"/api/editgroup(.+)", "editgroup",
	"/api/additem(.+)", "additem",
	"/api/delitem(.+)", "edititem",
	"/api/editgroup(.+)", "editgroup",
	"/api/test", "test")
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
        # return 'Hello, world!'
        result = []
        groups = db.get_groups()
        
        for group in groups:
        	g = {}
        	items = db.get_items(group.g_id)

        	# item_result = []
        	# for item in items:
        	# 	i = {}
        	# 	i['i_id'] = item.i_id
        	# 	i['i_name'] = item.i_name
        	# 	i['i_url'] = item.i_url
        	# 	i['i_index'] = item.i_index
        	# 	item_result.append(i)
        	g['g_id'] = group.g_id
        	g['g_name'] = group.g_name
        	g['g_index'] = group.g_index
        	# g['items'] = item_result
        	g['items'] = items
        	result.append(g)
        web.header('content-type','application/json')
        web.header('charset','utf-8')
        web.header('Access-Control-Allow-Origin','*')
        # return json.dumps(result, ensure_ascii = False, indent = 2)
        return json.dumps(result)
    
    # if __name__ == "__main__":
    #     web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    #     app.run()

class addgroup:
	# """docstring for ClassName"""
	# def __init__(self, arg):
		# super(ClassName, self).__init__()
		# self.arg = arg
	# def GET(self, name):
	def GET(self):
		result = {}
		group = web.input()
		name = group.get('name')
		# return type(group)
		if not group:
			result['statuscode'] = -1
			result['msg'] = 'error, please check your parameter(s)'
			result['result'] = ''
			return json.dumps(result)
		# return name
		if name is None or not name:
		# if not group.__contains__('name'):
			result['statuscode'] = -2
			result['msg'] = "error, do not hava a  parameter named 'name' or 'name' is empty"
			result['result'] = ''
			return json.dumps(result)

		result['statuscode'] = 0
		result['msg'] = "success"
		result['result'] = ''
		return db.add_group(name, -1)
		return json.dumps(result) #+ " " + group.name

class delgroup(object):
	"""docstring for ClassName"""
	# def __init__(self, arg):
		# super(ClassName, self).__init__()
		# self.arg = arg
	def GET(self):
		data = web.input();
		# return "del group" + data.name
		return data

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

class test:
	# """docstring for ClassName"""
	# def __init__(self, arg):
		# super(ClassName, self).__init__()
		# self.arg = arg
	def GET(self):
		return "test"

def info():
	for group in groups:
		print group.g_id,group.g_name
		for item in group.items:
			print item.id,item.name,item.url

# if __name__ == '__main__':
# 	item1 = item(1, "qq", "http://www.qq.com")
# 	group1 = group(1, "test")
# 	group1.add_item(item1)
# 	group1.add_item(item1)
# 	group1.add_item(item1)
# 	group1.add_item(item1)
# 	group1.add_item(item1)
# 	groups.append(group1)
# 	info()