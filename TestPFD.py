#!/usr/bin/env python

# -------------------------------
# Copyright (C) 2011
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestPFD.py > TestPFD.py.out
    % chmod ugo+x TestPFD.py
    % TestPFD.py > TestPFD.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from PFD import Vertex, pfd_process_rule, pfd_read, pfd_zero_pred, \
	pfd_sortbucket, pfd_update, pfd_print, pfd_eval, pfd_solve

# -------
# TestPFD
# -------

class TestPFD (unittest.TestCase) :

	# ------------
	# process_rule
	# ------------

	def test_process_rule_1 (self) :
		vertices = [Vertex() for _ in range(7)]
		l = ["3", "2", "1", "5"]
		pfd_process_rule(l, vertices)
		self.assert_(vertices[3].numPred == 2)
		self.assert_(vertices[3].listPred == [1, 5])
		self.assert_(vertices[1].listSuc == [3])
		self.assert_(vertices[5].listSuc == [3])
		
	def test_process_rule_2 (self) :
		vertices = [Vertex() for _ in range(7)]
		l = ["5", "1", "1"]
		pfd_process_rule(l, vertices)
		self.assert_(vertices[5].numPred == 1)
		self.assert_(vertices[5].listPred == [1])
		self.assert_(vertices[1].listSuc == [5])
		
	def test_process_rule_3 (self) :
		vertices = [Vertex() for _ in range(25)]
		l = ["3", "10", "1", "5", "6", "12", "2", "10", "8", "13", "16", "20"]
		pfd_process_rule(l, vertices)
		self.assert_(vertices[3].numPred == 10)
		self.assert_(vertices[3].listPred == [1, 5, 6, 12, 2, 10, 8, 13, 16, 20])
		self.assert_(vertices[1].listSuc == [3])
		self.assert_(vertices[5].listSuc == [3])
		self.assert_(vertices[6].listSuc == [3])
		self.assert_(vertices[12].listSuc == [3])
		self.assert_(vertices[2].listSuc == [3])
		self.assert_(vertices[10].listSuc == [3])
		self.assert_(vertices[8].listSuc == [3])
		self.assert_(vertices[13].listSuc == [3])
		self.assert_(vertices[16].listSuc == [3])
		self.assert_(vertices[20].listSuc == [3])

	# ----
	# read
	# ----

	def test_read_1 (self) :
		vertices = [Vertex() for _ in range(6)]
		vertices[3].numPred = 2
		vertices[3].listPred = [1, 5]
		vertices[2].numPred = 2
		vertices[2].listPred = [5, 3]
		vertices[1].listSuc = [3]
		vertices[3].listSuc = [2]
		vertices[5].listSuc = [3, 2]
		r = StringIO.StringIO("5 2\n3 2 1 5\n2 2 5 3\n")
		v = pfd_read(r)
		self.assert_(len(vertices) == len(v))
		self.assert_(vertices[3].numPred == v[3].numPred)
		self.assert_(vertices[3].listPred == v[3].listPred)
		self.assert_(vertices[2].numPred == v[2].numPred)
		self.assert_(vertices[2].listPred == v[2].listPred)
		self.assert_(vertices[1].listSuc == v[1].listSuc)
		self.assert_(vertices[1].listPred == v[1].listPred)
		self.assert_(vertices[3].listSuc == v[3].listSuc)
		self.assert_(vertices[5].listSuc == v[5].listSuc)
		

	# -------------
	# pfd_zero_pred
	# -------------
	
	def test_pfd_zero_pred_1 (self) :
		vertices = [Vertex() for _ in range(6)]
		vertices[3].numPred = 2
		vertices[2].numPred = 2
		v = pfd_zero_pred(vertices)
		result = [1, 4, 5]
		self.assert_(v == result)

	def test_pfd_zero_pred_2 (self) :
		vertices = [Vertex() for _ in range(6)]
		vertices[4].numPred = 1
		vertices[5].numPred = 1
		v = pfd_zero_pred(vertices)
		result = [1, 2, 3]
		self.assert_(v == result)

	def test_pfd_zero_pred_3 (self) :
		vertices = [Vertex() for _ in range(20)]
		vertices[1].numPred = 1
		vertices[2].numPred = 1
		vertices[3].numPred = 1
		vertices[4].numPred = 1
		vertices[6].numPred = 1
		vertices[8].numPred = 1
		vertices[10].numPred = 1
		vertices[12].numPred = 1
		vertices[13].numPred = 1
		vertices[15].numPred = 1
		vertices[17].numPred = 1
		vertices[18].numPred = 1
		v = pfd_zero_pred(vertices)
		result = [5, 7, 9, 11, 14, 16, 19]
		self.assert_(v == result)


	# --------------
	# pfd_sortbucket
	# --------------
	
	def test_pfd_sortbucket_1 (self) :
		result = pfd_sortbucket([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
		self.assert_(result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

	def test_pfd_sortbucket_2 (self) :
		result = pfd_sortbucket([3, 7, 1, 2, 10, 8, 5, 9, 4, 6])
		self.assert_(result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

	def test_pfd_sortbucket_3 (self) :
		result = pfd_sortbucket([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
		self.assert_(result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
	
	# ----------
	# pfd_update
	# ----------

	def test_pfd_update_1 (self) :
		vertices = [Vertex() for _ in range(7)]
		l = [1, 3, 5]
		vertices[2].numPred = 1
		vertices[4].numPred = 2
		vertices[6].numPred = 3
		vertices[1].listSuc = [2]
		vertices[3].listSuc = [4]
		vertices[5].listSuc = [6]
		pfd_update(l, vertices)
		self.assert_(vertices[2].numPred == 0)
		self.assert_(vertices[4].numPred == 1)
		self.assert_(vertices[6].numPred == 2)
	
	def test_pfd_update_2 (self) :
		vertices = [Vertex() for _ in range(7)]
		l = [1, 3, 5]
		vertices[2].numPred = 1
		vertices[4].numPred = 2
		vertices[6].numPred = 3
		vertices[1].listSuc = [2, 4, 6]
		vertices[3].listSuc = [4, 6]
		vertices[5].listSuc = [6]
		pfd_update(l, vertices)
		self.assert_(vertices[2].numPred == 0)
		self.assert_(vertices[4].numPred == 0)
		self.assert_(vertices[6].numPred == 0)

	def test_pfd_update_3 (self) :
		vertices = [Vertex() for _ in range(10)]
		l = [1, 3, 5, 7]
		vertices[2].numPred = 1
		vertices[4].numPred = 2
		vertices[6].numPred = 3
		vertices[8].numPred = 4
		vertices[9].numPred = 5
		vertices[1].listSuc = [2, 4, 6]
		vertices[3].listSuc = [4, 6]
		vertices[5].listSuc = [6, 9]
		vertices[7].listSuc = [8, 9]
		pfd_update(l, vertices)
		self.assert_(vertices[2].numPred == 0)
		self.assert_(vertices[4].numPred == 0)
		self.assert_(vertices[6].numPred == 0)
		self.assert_(vertices[8].numPred == 3)
		self.assert_(vertices[9].numPred == 3)

	# ----
	# eval
	# ----
    	
	def test_eval_1 (self) :
		vertices = [Vertex() for _ in range(6)]
		vertices[3].numPred = 2
		vertices[3].listPred = [1, 5]
		vertices[2].numPred = 2
		vertices[2].listPred = [5, 3]
		vertices[4].numPred = 1
		vertices[4].listPred = [3]
		vertices[5].numPred = 1
		vertices[5].listPred = [1]
		vertices[1].listSuc = [3, 5]
		vertices[3].listSuc = [2, 4]
		vertices[5].listSuc = [2, 3]
		result = pfd_eval(vertices)
		self.assert_(result == [1, 5, 3, 2, 4])
	
	def test_eval_3 (self) :
		vertices = [Vertex() for _ in range(7)]
		vertices[2].numPred = 2
		vertices[2].listPred = [1, 3]
		vertices[3].numPred = 1
		vertices[3].listPred = [1]
		vertices[4].numPred = 3
		vertices[4].listPred = [2, 5, 6]
		vertices[5].numPred = 1
		vertices[5].listPred = [3]
		vertices[6].numPred = 1
		vertices[6].listPred = [5]
		vertices[1].listSuc = [2, 3]
		vertices[2].listSuc = [4]
		vertices[3].listSuc = [2, 5]
		vertices[5].listSuc = [4, 6]
		vertices[6].listSuc = [4]
		result = pfd_eval(vertices)
		self.assert_(result == [1, 3, 2, 5, 6, 4])

	# -----
	# print
	# -----

	def test_print_1 (self) :
		w = StringIO.StringIO()
		pfd_print(w, [1, 2, 3, 4, 5])
		self.assert_(w.getvalue() == "1 2 3 4 5 \n")
	
	def test_print_2 (self) :
		w = StringIO.StringIO()
		pfd_print(w, [1])
		self.assert_(w.getvalue() == "1 \n")
	
	def test_print_3 (self) :
		w = StringIO.StringIO()
		pfd_print(w, [])
		self.assert_(w.getvalue() == "\n")

	# -----
	# solve
	# -----

	# def test_solve_1 (self) :

# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."



