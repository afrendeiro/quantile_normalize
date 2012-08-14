quantile_normalize
==================

Quantile normalization of masked numpy arrays per [Bolstad et al](http://bmbolstad.com/misc/normalize/normalize.html).

NOTE: `quantile_norm` normalizes a matrix in place; it does not return a copy.

USE
---
    import quantile_normalize, numpy
    M = numpy.load("my_masked_matrix.npy")
    quantile_normalize.quantile_norm(M)
    