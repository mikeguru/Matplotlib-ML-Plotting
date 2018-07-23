# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Michael (Wen) Jiang"

# matplotlib 	2.1.1
# scipy		    1.0.0

import matplotlib.pyplot as plt
import numpy as np
import scipy.special as ss


def pmf ( n , p , t , x ):
    return -(1 - (1 - p) ** (n - x) * p ** x * ss.binom ( n , x ) * ss.hyp2f1 ( 1 , -n + x , 1 + x ,
                                                                                p / (p - 1) )) ** t + (
                   1 - (1 - p) ** (-1 + n - x) * p ** (1 + x) * ss.binom ( n , 1 + x ) * ss.hyp2f1 ( 1 , 1 - n + x ,
                                                                                                     2 + x , p / (
                                                                                                             p - 1) )) ** t

def mean ( n , p , t ):
    s = 0
    for x in range ( 0 , n + 1 ):
        s += x * pmf ( n , p , t , x )
    return s

print ( mean ( 1000 , 1 / 9 , 9 ) )

plt.hist ( np.random.multinomial ( 1000 , [ 1 / 9 ] * 9 , 99999 ) )
plt.axvline ( np.random.multinomial ( 1000 , [ 1 / 9 ] * 9 , 99999 ).mean ( ) , color='b' , linestyle='solid' ,
              linewidth=2 )
plt.title ( 'multinomial' )

plt.show ( )

maxx = [ max ( x ) for x in np.random.multinomial ( 1000 , [ 1 / 9 ] * 9 , 99999 ) ]

print ( np.mean ( maxx ) )
