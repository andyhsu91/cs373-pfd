#!/usr/bin/env python

# ------------------------------
# Copyright (C) 2011
# Glenn P. Downing
# -------------------------------

"""
To run the program
    % python RunPFD.py < RunPFD.in > RunPFD.out
    % chmod ugo+x RunPFD.py
    % RunPFD.py < RunPFD.in > RunPFD.out

To document the program
    % pydoc -w PFD
"""

# -------
# imports
# -------

import sys

from PFD import pfd_solve

# ----
# main
# ----

pfd_solve(sys.stdin, sys.stdout)
