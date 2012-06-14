#!/usr/bin/env python

# ---------------------------
# Copyright (C) 2011
# Glenn P. Downing
# ---------------------------

class Vertex(object) :

	def __init__(self):
		self.numPred = -1
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
	for x in range(0, len(l)) :
		l[x] = int(l[x])
		
	vertices[l[0]].numPred = l[1]

	for x in range(2, l[1]+2) :
		vertices[l[0]].listPred += l[x]
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
	string = ""
	for x in range(0, len(v)) :
		string += str(v[x])
		string += " "	
	
	w.write(string + "\n")

# -------------
# pfd_zero_pred
# -------------

def pfd_zero_pred() :
	"""
	loop through all vertices and check for zero pred
	returns a bucket of zero pred and marks the numPred = -1
	"""

# --------------
# pfd_sortbucket
# --------------

def pfd_sortbucket(zeroPred) :
	"""
	given a list of zero predecessors, sort by vertex value
	zeroPred is an unsorted list of vertices with zero predecessors
	"""

# ----------
# pfd_update
# ----------

def pfd_update(listSuc) :
	"""
	updates the numPred for the global list of vertices by
	decrementing the value.
	listSuc is the list of vertices to be updated
	"""

# --------
# pfd_eval
# --------

def pfd_eval (vertices) :
	"""
	evaluates the list of vertices and returns another list ordered
	"""
	ordered = None
	zeroPred = None
	
	# Start to evaluate here
	
	# loop len(ordered) == len(vertices)-1
		# for each vertex, check no of pred
		# add all 0 zeropred to bucket
		# v = pfd_sortbucket(zeroPred)   sorts bucket by vertex value
		# once bucket is sort, append to ordered
		
		# ordered += v
		
		# pfd_update    updates all sucesssor
		
	
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
        
        
        
        
        
        
        
