#!/usr/bin/python
from __future__ import division
import unittest
from StringIO import StringIO
import numpy as np
from __init__ import *

VALUES = [2,4,6,8]
#M = np.genfromtxt("test2.tab", delimiter="\t", usemask=True)

MATRIX = """1	2	5	1
9		1	0
8	4	9	0
		8	
6	23	1	0"""

MATRIX_QNORMED = """1	1	4	10.5000000000000
10.5000000000000		1.59375000000000	2.79166666666667
6.33333333333333	4	10.5000000000000	2.79166666666667
		7.50000000000000	
2.79166666666667	10.5000000000000	1.59375000000000	2.79166666666667"""

MATRIX = """1	2	5	1
9		1	0
8	4	9	0
		8	
6	23	1	0"""

class TestFractionalIntervals(unittest.TestCase):
  def test_range1(self):
    M = 22283
    q = frac_intervals(M)
    self.assertEqual(np.size(q), M)
  def test_range2(self):
    M = 4
    q = frac_intervals(M)
    self.assertEqual(np.size(q), M)
  def test_range2(self):
    M = 22280
    q = frac_intervals(M)
    self.assertEqual(np.size(q), M)    

class TestInterpolate(unittest.TestCase):
  def test_interpolate1(self):
    v = [2,8]
    self.assertEqual(my_interpolate(0,v), 2)
    self.assertEqual(my_interpolate(1/3,v), 4)
    self.assertEqual(my_interpolate(2/3,v), 6)
    self.assertEqual(my_interpolate(3/3,v), 8)

  def test_interpolate2(self):
    v = [2,8,30]
    self.assertEqual(my_interpolate(0,v), 2)
    self.assertEqual(my_interpolate(1/2,v), 8)
    self.assertEqual(my_interpolate(1/3,v), 1/3*2 + 2/3*8)
    self.assertEqual(my_interpolate(2/3,v), 2/3*8 + 1/3*30)
    self.assertEqual(my_interpolate(3/3,v), 30)

class TestQuantileNorm(unittest.TestCase):
  def test_norm(self):
    M = np.genfromtxt(StringIO(MATRIX), delimiter="\t", usemask=True)
    self.assertEqual(M[0,0], 1)
    self.assertEqual(M.mask[0,0], False)
    self.assertEqual(M.mask[3,0], True)
    quantile_norm(M)
    print M
    # verify results
    Q = np.genfromtxt(StringIO(MATRIX_QNORMED), delimiter="\t", usemask=True)
    self.assertTrue(np.mean(M-Q) < 0.00000000001 )
    
if __name__ == "__main__":
  unittest.main()
