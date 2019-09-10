# -*- coding: utf-8 -*-

import numpy as np
def ptmilieu(f,n,a,b):
    "quadrature de \int_a^b f(x)dx par la méthode du pt milieu decoupé en n ss-intervalle"
    h = (b-a)/n
    xm  = a + (0.5 + np.arange(n))*h
    Q = np.sum(f(xm))*h
    return Q
