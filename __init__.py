#!/usr/bin/python
from __future__ import division
import numpy as np
from scipy import interpolate

# see: scoreatpercentile


def my_interpolate(pos, v):
  """Return interpolated value pos from v.
  Args:
    pos: 0 <= x <= 1 fractional position in v
    v: [num] vector
  Returns:
    num of interpolated v @ pos
  """
  n = len(v)-1
  low, high = int(np.floor(n*pos)), int(np.ceil(n*pos))
  if low==high:
    return v[low]
  else:
    frac = pos*n - low
    return v[low]*(1-frac) + v[high]*(frac)

  
def frac_intervals(n):
  x = 1/(n-1)
  return np.arange(0,1+x,x)

def quantile_norm(M):
  """Quantile normalize masked array M in place."""
  Q = M.argsort(0)
  m, n = np.size(M,0), np.size(M,1)
  counts = np.array([m - np.count_nonzero(M.mask[:,i]) for i in range(n)])

  # compute quantile vector
  quantiles = np.zeros(m)
  for i in xrange(n):
    # select first [# values] rows of argsorted column in Q
    r = counts[i] # number of non-missing values for this column
    v = M.data[:,i][Q[:r,i]]
    # create linear interpolator 
    f = interpolate.interp1d(np.arange(r)/(r-1), v)
    v_full = f(frac_intervals(m))
    quantiles += v_full
  quantiles = quantiles / n
  f_quantile = interpolate.interp1d(frac_intervals(m), quantiles)

  ranks = np.empty(m, int)
  for i in xrange(n):
    r = counts[i]
    ranks[Q[:,i]] = np.arange(m)
    # Get equivalence classes; unique values == 0
    dupes = np.zeros(m, dtype=np.int)
    for j in xrange(r-1):
      if M[Q[j,i]] == M[Q[j+1,i]]:
        dupes[j+1] = dupes[j]+1
    # zero-out ranks higher than the number of values (to prevent out of range errors)
    ranks[ranks>=r] = 0
    # Replace column with quantile ranks
    M.data[:,i] = f_quantile(ranks/(r-1))
    # Average together equivalence classes
    j = r-1
    while j >= 0:
      if dupes[j] == 0:
        j -= 1
      else:
        idxs = Q[j-dupes[j]:j+1,i]
        assert idxs[1:]-1 == idxs[:-1]
        M.data[idxs] = M.data[idxs].mean()
        j -= 1 + dupes[j]
    assert j == -1
  
