#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import glob
import math
import sys
import os
import random

def print_numpy_version():
    print(np.version.version)


def make_plots():
    
    
    x_tilda = 3.0
    y_tilda = 4.0



    #plt.plot([1,2,3,4], [1,4,9,16], c='red')
    plt.xlim(-0.5, 6.5)
    plt.ylim(-0.5, 6.5)
    plt.gca().set_aspect('equal')
    
    
    # Observed data
    if True:
        plt.plot([x_tilda,], [y_tilda,], 'or')
    
    if True:
        num_true_points = 1500
        x_trues = np.random.normal(loc=x_tilda, scale=1.0, size=num_true_points)
        y_trues = np.random.normal(loc=y_tilda, scale=1.0, size=num_true_points)
        plt.plot(x_trues, y_trues, '.g', ms=1)
        
    
    
    plt.savefig('./figure_1.png', bbox_inches="tight")
    plt.show()


   

if __name__ == '__main__':

    #print_numpy_version()
    make_plots()
    pass
    
    
