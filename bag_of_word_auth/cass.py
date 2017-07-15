#!/usr/bin/python
# -*- coding: utf8 -*-
from cassandra.io.libevreactor import LibevConnection
from cassandra.cluster import Cluster
from cassandra.query import dict_factory
from cassandra import ReadTimeout
from pyvi.pyvi import ViTokenizer, ViPosTagger
import re, itertools
import math,os
import pandas as pd
import json
cluster = Cluster()
cluster.connection_class = LibevConnection
session = cluster.connect('test')
rows = session.execute('SELECT * FROM tmp')

data = {}

a = []
for row in rows:
    a.append(row.comment.encode('utf8'))

print a
print data

x = 'a'
print type(x)
z = x
session.execute("INSERT INTO add_neg (negative_comment) VALUES (%s)", z)
session.execute(query)
