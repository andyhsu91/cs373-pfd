#!/usr/bin/env python

# ------------------------------
# Copyright (C) 2011
# Glenn P. Downing
# -------------------------------

"""
To run the program
    % python SpherePFD.py < RunPFD.in > SpherePFD.out
    % chmod ugo+x SpherePFD.py
    % SpherePFD.py < RunPFD.in > SpherePFD.out

To document the program
    % pydoc -w PFD
"""

# -------
# imports
# -------

import sys
import heapq

class Vertex(object) :
	"""
	object storing number of predecessors,
	list of predecessors, and list of sucessors
	"""
	def __init__(self):
		self.numPred = 0
		self.listPred = []
		self.listSuc = []

# ----------------
# pfd_process_rule
# ----------------

def pfd_process_rule (l, vertices) :
	"""
	processes rules to the corresponding vertex
	l is a list of strings of ints
	"""
	assert vertices != []
	assert l != []
	for x in range(0, len(l)) :
		l[x] = int(l[x])
		
	vertices[l[0]].numPred = l[1]

	if l[1] != 0 :
		for x in range(2, l[1]+2) :
			vertices[l[0]].listPred += [l[x]]
			vertices[l[x]].listSuc += [l[0]]

# ---------
# pfd_read
# --------

def pfd_read (r) :
	"""
	reads the file and creates a list to store vertices
	r is a  reader
	"""
	s = r.readline()
	if s == "" :
		return None
	l = s.split()
	if len(l) < 2 :
		return None
		
	numVertices = int(l[0])
	numRules = int(l[1])
	
	assert numVertices > 0
	assert numRules > 0
	assert numVertices > numRules
	
	vertices = [Vertex() for _ in range(numVertices + 1)]

	for x in range(0, numRules) :
		s = r.readline()
		if s == "" :
			return None
		l = s.split()
		if len(l) < 2 :
			return None
			
		pfd_process_rule(l, vertices)

	return vertices

# ---------
# pfd_print
# ---------

def pfd_print (w, v) :
	"""
	prints the sorted tasks by dependecies
	w is a writer
	v is a list of ordered ints
	"""
	assert v != None
	assert v != []
	string = ""
	for x in range(0, len(v)-1) :
		string += str(v[x])
		string += " "	
	string += str(v[len(v)-1])
	w.write(string)

# -------------
# pfd_zero_pred
# -------------

def pfd_zero_pred(vertices) :
	"""
	loop through all vertices and check for zero pred, adds them
	to a bucket of zero pred, takes the smallest vertex and marks 
	the numPred = -1 of that vertex	also decrements the number pred 
	for the sucessors
	vertices is the created object structure holding all the info
	"""
	assert vertices != []
	result = []
	# Find all zero preds
	for x in range(1, len(vertices)) :
		if (vertices[x].numPred == 0) :
			heapq.heappush(result, x)					# <------------ HEAP
	
	# Take smallest zero pred, mark and update
	assert result != []
	val = heapq.heappop(result)	
	
	tempSuc = vertices[val].listSuc
	for x in range(len(tempSuc)) :
		vertices[tempSuc[x]].numPred -= 1		
	vertices[val].numPred = -1
	return val

# --------
# pfd_eval
# --------

def pfd_eval (vertices) :
	"""
	evaluates the list of vertices and returns another list ordered
	"""
	assert vertices != []
	ordered = []
	
	# Start to evaluate here
	
	while len(ordered) != len(vertices)-1 :
		zeroPred = pfd_zero_pred(vertices)
		ordered += [zeroPred]
	assert ordered != []
	return ordered

# ---------
# pfd_solve
# ---------

def pfd_solve (r, w) :
	"""
	read, eval, print loop
	r is a reader
	w is a writer
	"""
	l = pfd_read(r)
	if l != None :
		v = pfd_eval(l)
	pfd_print(w, v)
	
# ----
# main
# ----

pfd_solve(sys.stdin, sys.stdout)

