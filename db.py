#!/usr/bin/env python
# coding=utf-8

import web
import sqlite3 # 导入sqlite模块

print "In db.py"

group_sql = "create table if not exists groups(" \
	"g_id integer primary key autoincrement not null," \
	"g_name varchar(255), g_index int)"

item_sql = "create table if not exists items(" \
	"i_id integer primary key autoincrement not null," \
	"i_name varchar(255)," \
	"i_url varchar(255)," \
	"i_index int)"

relation_sql =  "create table if not exists relations(" \
	"r_id integer primary key autoincrement not null," \
	"g_id integer," \
	"i_id integer)"

db = web.database(dbn='sqlite', db='navigation.db')
con = sqlite3.connect("navigation.db") # 连接到数据库文件,
cur = con.cursor() # 创建一个指针
cur.execute(group_sql) # 创建表
cur.execute(item_sql)
cur.execute(relation_sql)
con.commit() # 执行操作
# cur.close() # 关闭指针
# con.close() # 关闭数据库连接

def get_groups():
	# for g in db.select('groups', order='g_index'):
		# return g.g_name
	return db.select('groups', order = 'g_index')

def add_group(g_name, g_index):
	return db.insert('groups', g_name = g_name, g_index = g_index)	

def del_group(g_id):
	db.delete('groups', where="g_id = $g_id");

def get_items(g_id):
	try:
		results = db.query("SELECT items.i_id, items.i_name, items.i_url, items.i_index FROM items,relations \
			WHERE relations.g_id = $g_id and relations.i_id = items.i_id ", vars = {'g_id' : g_id})
		rets = []
		for row in results:
			ret = {}
			ret['i_id'] = row.i_id
			ret['i_name'] = row.i_name
			ret['i_url'] = row.i_url
			ret['i_index'] = row.i_index
			rets.append(ret)
		return rets
	except:
		print "Error: unable to fecth data"

def add_item(g_id, i_item, i_name, i_url, i_index):
	return db.insert('items', i_name = i_name, i_url = i_url, i_index = i_index)

def del_item(i_id):
	db.delete('items', i_id = i_id)

def insert_test_data():
	g_id = db.insert('groups', g_name = 'aaa', g_index = 12)
	i_id = db.insert('items', i_name = 'csdn', i_url = 'http://www.csdn.net', i_index = '22')
	db.insert('relations', g_id = g_id, i_id = i_id)
	i_id = db.insert('items', i_name = 'baidu', i_url = 'http://www.baidu.com', i_index = '0')
	db.insert('relations', g_id = g_id, i_id = i_id)
	i_id = db.insert('items', i_name = 'google', i_url = 'http://www.google.com', i_index = '1')
	db.insert('relations', g_id = g_id, i_id = i_id)
	i_id = db.insert('items', i_name = 'qq', i_url = 'http://www.qq.com', i_index = '2')
	db.insert('relations', g_id = g_id, i_id = i_id)

	g_id = db.insert('groups', g_name = 'bbb', g_index = 13)
	i_id = db.insert('items', i_name = '360', i_url = 'http://www.360.com', i_index = '2')
	db.insert('relations', g_id = g_id, i_id = i_id)
	i_id = db.insert('items', i_name = 'duokan', i_url = 'http://www.duokan.com', i_index = '1')
	db.insert('relations', g_id = g_id, i_id = i_id)
	i_id = db.insert('items', i_name = 'jd', i_url = 'http://www.jd.com', i_index = '5')
	db.insert('relations', g_id = g_id, i_id = i_id)

	g_id = db.insert('groups', g_name = 'ccc', g_index = 14)
	i_id = db.insert('items', i_name = 'dangdang', i_url = 'http://www.dangdang.com', i_index = '2')
	db.insert('relations', g_id = g_id, i_id = i_id)
	i_id = db.insert('items', i_name = 'zhihu', i_url = 'http://www.zhihu.com', i_index = '5')
	db.insert('relations', g_id = g_id, i_id = i_id)
	i_id = db.insert('items', i_name = 'douban', i_url = 'http://www.douban.com', i_index = '7')
	db.insert('relations', g_id = g_id, i_id = i_id)
	i_id = db.insert('items', i_name = 'renren', i_url = 'http://www.renren.com', i_index = '23')
	db.insert('relations', g_id = g_id, i_id = i_id)
	i_id = db.insert('items', i_name = 'amazon', i_url = 'http://www.amazon.com', i_index = '12')
	db.insert('relations', g_id = g_id, i_id = i_id)
	i_id = db.insert('items', i_name = 'yhd', i_url = 'http://www.yhd.com', i_index = '30')
	db.insert('relations', g_id = g_id, i_id = i_id)

# insert_test_data()
print "Out db.py"