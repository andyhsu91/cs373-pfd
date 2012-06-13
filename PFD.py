#!/usr/bin/env python

# ---------------------------
# Copyright (C) 2011
# Glenn P. Downing
# ---------------------------

class Vertex(object) :

	def __init__(self):
		self.numPred = None
		self.listPred = None
		self.listSuc = None

vertices = None			# Type list of Vertex objects
numVertices = 0			# Type int

# -----------------
# pfd_vertices_init
# -----------------

def pfd_vertices_init () :
	"""
	initializes a list of vertices at the given global size
	read in
	"""
	global vertices
	vertices = [Vertex() for _ in range(numVertices)]

# ----------------
# pfd_process_rule
# ----------------

def pfd_read (l) :
	"""
	processes rules to the corresponding vertex
	l is a list of ints
	"""
	global vertices
	vertices[l[0]].numPred = l[1]
	
	for x in range(2, l[1]+2) :
		vertices[l[0]].listPred += [l[x]]	

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
		return False
	l = s.split()
	if len(l) < 2 :
		return False
	global numVertices
	numVertices = int(l[0])
	numRules = int(l[1])
	
	assert numVertices > 0
	
	pfd_vertices_init()

	for x in range(0, numRules) :
		s = r.readline()
		if s == "" :
			return False
		l = s.split()
		if len(l) < 2 :
			return False
			
		v =  v and pfd_process_rule(l)

	return v

# ---------
# pfd_print
# ---------

def pfd_print (w, v) :
	"""
	prints the sorted tasks by dependecies
	w is a writer
	v is a list of ordered ints
	"""
	string = ""
	for x in range(0,numVertices) :
		string += str(v[x])
		string += " "	
	
	w.write(string)

# --------
# pfd_eval
# --------

def pfd_eval () :
	"""
	evaluates the list of vertices and returns another list ordered
	"""
	ordered = None
	zeroPred = None
	
	# Start to evaluate here
	
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
	if pfd_read(r) :
		v = pfd_eval()
	pfd_print(w, v)
        
        
        
        
        
        
        
