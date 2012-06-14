#!/usr/bin/env python

"""
To run the program
    % python TestGenPFD.py [number of tests] > RunPFD.in 
    % chmod ugo+x TestGenPFD.py
    % TestGenPFD.py > RunPFD.in
"""

# -------
# imports
# -------

import sys
import random

# ----
# main
# ----


tasks = random.randrange(50, 101)
rules = random.randrange(50, tasks)

assert rules <= tasks

sys.stdout.write(str(tasks) + " " + str(rules) + "\n")
data1 = [i for i in range(1, tasks+1)]

while rules :
	rules -= 1
	strResult = ""
	index1 = random.randrange(0, tasks)

	while data1[index1] == -1 :
		index1 = random.randrange(0, tasks)

	elem1 = data1[index1]
	pred = random.randrange(1, tasks+1)
	predcnt = pred
	strResult += str(elem1) + " " + str(pred) + " "
	data2 = [j for j in range(1, tasks+1)]
	data2[index1] = -1
	while predcnt :
				
		predcnt -= 1
		index2 = random.randrange(0, tasks)
		
		while data2[index2] == -1 :
			index2 = random.randrange(0, tasks)

		elem2 = data2[index2]
		strResult += str(elem2) + " "
		data2[index2] = -1
	
	data1[index1] = -1
	
	sys.stdout.write(str(strResult) + "\n")


