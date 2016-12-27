# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import re

'''
1. Read all the 
'''
outfile = open('test\\test_out\\outfile.txt', 'r+')

def extract(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        #for d in dirs:      
            #print os.path.join(d)        
        for file in files:
            #print os.path.join(filename)
            if re.search('target',file):
                target_file = os.path.join(root, file)
                #print os.path.join(root, filename)
                target = open(target_file)
                lines = target.readlines()
                for line in lines:
                    if re.search('one',line):
                        print(file+':\t'+line)
                        #outfile.read()
                        outfile.write(file+':\t'+line)
                target.close()

extract('test\\test_in')

outfile.close()