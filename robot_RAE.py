#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from srae import get_html


OUTPUT = 'output'
LEMARIO = 'lemario.txt'


def generate_html(word):
	return None
	

def get_all_html(lemario):
	"""Create html documents at OUTPUT directory"""
	f = open(lemario, 'r')
	if f != None:
		for line in f: # Read random best!
			print line
	else: 
		print 'Error file: %s' % lemario 


if __name__ == '__main__':
	print 'Exec!'
	args = sys.argv
	if len(args) > 1:
		get_all_html(args[1])
	else:
		get_all_html(LEMARIO)