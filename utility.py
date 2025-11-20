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
    
    np.random.seed(0)
    
    
    x_tilda = 3.0
    y_tilda = 4.0
    
    lower_limit = -0.5
    upper_limit = 6.5



    plt.xlim(lower_limit, upper_limit)
    plt.ylim(lower_limit, upper_limit)
    plt.gca().set_aspect('equal')
    
    
    # Observed data
    if True:
        plt.plot([x_tilda,], [y_tilda,], 'or')
        plt.xlabel(r'$x$')
        plt.ylabel(r'$y$')
        plt.savefig('./figure_1.png', bbox_inches="tight")
    
    if True:
        num_true_points = 1500
        x_trues = np.random.normal(loc=x_tilda, scale=1.0, size=num_true_points)
        y_trues = np.random.normal(loc=y_tilda, scale=1.0, size=num_true_points)
        plt.plot(x_trues, y_trues, '.g', ms=1)
        plt.savefig('./figure_2.png', bbox_inches="tight")
        
    if True:
        plt.plot([lower_limit, upper_limit], [0.75 * y for y in [lower_limit, upper_limit]], 'k-')
        plt.text(6.2, 4.3, r'$b$')
        plt.plot([lower_limit, upper_limit], [0.80 * y for y in [lower_limit, upper_limit]], 'k-')
        plt.text(5.3, 5, r'$b+db$')
        plt.savefig('./figure_3.png', bbox_inches="tight")
    plt.show()
    
    
    
    
    if False:
        
        plt.clf
    
        plt.xlim(lower_limit, upper_limit)
        plt.ylim(lower_limit, upper_limit)
        plt.gca().set_aspect('equal')
       
        b_prior_low = 0.0
        b_prior_high = 10.0
        x_prior_low = -10.0
        x_prior_high = 30.0

        num_data_points = 60000
        plt.plot([x_tilda,], [y_tilda,], 'or')
        b_trues = np.random.uniform(b_prior_low, b_prior_high, num_data_points)
        x_trues = np.random.uniform(x_prior_low, x_prior_high, num_data_points)
        y_trues = b_trues * x_trues
        x_data = x_trues + np.random.normal(loc=0.0, scale=1.0, size=num_data_points)
        y_data = y_trues + np.random.normal(loc=0.0, scale=1.0, size=num_data_points)
        res = plt.scatter(x_data, y_data, s=2, c=b_trues, cmap='magma') #'viridis'
        plt.colorbar(res, label=r'True $b$')
        
        plt.savefig('./figure_4.png', bbox_inches="tight")
        plt.show()
        
    




   

if __name__ == '__main__':

    #print_numpy_version()
    make_plots()
    pass
    
    
