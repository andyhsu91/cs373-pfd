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

from PFD import pfd_vertices_init, pfd_process_rule, pfd_read, pfd_print /
	pfd_eval, pfd_solve

# -------
# TestPFD
# -------

class TestPFD (unittest.TestCase) :
    # -------------
    # vertices_init
    # -------------

	def test_vertices_init_1 (self) :		

	# ------------
	# process_rule
	# ------------

	def test_process_rule_1 (self) :	

	# ----
	# read
	# ----

	def test_read_1 (self) :

    # ----
    # eval
    # ----

	def test_eval_1 (self) :

    # -----
    # print
    # -----

	def test_print_1 (self) :

    # -----
    # solve
    # -----

	def test_solve_1 (self) :

# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."



