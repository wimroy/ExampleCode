'''
From: http://stackoverflow.com/a/2026849/1840563
'''

import random
import time

class Base:
	name = 'Base'
	def __init__(self):
		self.name = name

class A (Base):
	pass

class B (Base):
	name = 'BBB'

class C (Base):
	name = 'CCC'


class X (random.choice([A,B,C])):
    def __init__(self):
			print self.name


for i in range(5): x = X()
