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
    
if __name__ == "__main__":
  unittest.main()
