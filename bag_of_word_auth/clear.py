#!/usr/bin/python
# -*- coding: utf8 -*-
from pyvi.pyvi import ViTokenizer, ViPosTagger
import re, itertools
import math,os
import pandas as pd
import json
from cassandra.io.libevreactor import LibevConnection
from cassandra.cluster import Cluster
from cassandra.query import dict_factory
cluster = Cluster()
cluster.connection_class = LibevConnection
session = cluster.connect('getfb')
query_clear = "TRUNCATE TABLE add_neg"
session.execute(query_clear)