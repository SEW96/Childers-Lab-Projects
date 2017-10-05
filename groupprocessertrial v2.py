#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:03:35 2017

@author: sarawhitlock
"""
import csv

FILE = 'data_processer_output'

with open ('{}.tsv'.format(FILE)) as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    
    """ 
    This block of code separates bacteria by number of fluorescent data points.
    Should work or up to five fluorescent data points. Not tested for six or
    more fluorescent data points. 
    
    """  
    a = one_entry = []
    b = two_entry = []
    c = three_entry = []
    d = four_entry = []
    e = five_entry = []
    for row in reader:
        for item in row:
            bacteria = row[0]
            rest = row[1]
            length = len(rest)
            #one entry fluorescence 
            if length <= 30: 
                bac_list1 = []
                for entry in one_entry:
                    bac1 = entry[0]
                    bac_list1.append(bac1)
                if bacteria not in bac_list1:
                    one_entry.append(row)
            #two entry fluorescence
            elif length <= 70:
                bac_list2 = []
                for entry in two_entry:
                    bac2 = entry[0]
                    bac_list2.append(bac2)
                if bacteria not in bac_list2:
                    two_entry.append(row)
            #three entry fluorescence
            elif length <=100:
                bac_list3 = []
                for entry in three_entry:
                    bac3 = entry[0]
                    bac_list3.append(bac3)
                if bacteria not in bac_list3:
                    three_entry.append(row)
            #four entry fluorescence
            elif length <= 120:
                bac_list4 = []
                for entry in four_entry:
                    bac4 = entry[0]
                    bac_list4.append(bac4)
                if bacteria not in bac_list4:
                    four_entry.append(row)
            #five entry fluorescence
            else:
                bac_list0 = []
                for entry in five_entry:
                    bac0 = entry[0]
                    bac_list0.append(bac0)
                if bacteria not in bac_list0:
                    five_entry.append(row)

with open('One Entry.tsv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerows(a)
with open('Two Entry.tsv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerows(b)
with open('Three Entry.tsv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerows(c)
with open('Four Entry.tsv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerows(d)
with open('Five Entry.tsv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerows(e)
print('Bacteria with one fluorescence data point are ', one_entry[:5])
print('Bacteria with two fluorescence data points are ', two_entry[:5])
print('Bacteria with three fluorescence data points are ', three_entry[:5])
print('Bacteria with four fluorescence data points are ', four_entry[:5])
print('Bacteria with five fluorescence data points are ', five_entry[:5])