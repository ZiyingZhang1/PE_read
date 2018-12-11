#!/usr/bin/env python

from sys import argv
from decimal import getcontext, Decimal
import os
import re
import sys

# parsing the parameters --Setting.txt
def settings_parser(settings_file):
    
    settings_dictionary = {}
    with open(settings_file) as f:
        for line in f:
            if not line.startswith("#"):
                line = line.strip()
                line = line.split("    ")
                settings_dictionary[line[0]] = line[1]
    return settings_dictionary

def get_PE_file(directory):
    
    
    filesname = os.listdir(directory)
    
    return filesname
    
    
def caculate_read_length(read1, read2):
    
    num_line = 0
    base1 = []
    base2 = []
    
    file1_contents = open(read1, "r").read().strip().split("\n")
    #print("1-",file1_contents)
    #file1_contents = ' '.join(file1_contents).split()
    #print("2-",file1_contents)
    file2_contents = open(read2, "r").read().strip().split("\n")
    
    #file2_contents = ' '.join(file2_contents).split()
    #print(file2_contents)
    num_lines = len(file1_contents)
    num_read = num_lines/2   
    print("read num",num_read)
    
    for i in range(num_lines):
        if file1_contents[i].startswith("@"):
            base1.append(file1_contents[i+1].strip())
    
    
    for i in range(num_lines):
        if file2_contents[i].startswith("@"):
            base2.append(file2_contents[i+1].strip())
               
    total_base = base1 + base2
    total_base = ''.join(total_base)
    average_read_length = len(total_base)/num_read
    average_read_length = Decimal(average_read_length).quantize(Decimal('0.0'))
    return (average_read_length)
    


    
    
    


if __name__ == '__main__':
    
    # parsing the parameters
    settings_file = sys.argv[1]
    settings_dictionary = settings_parser(settings_file)
    print(settings_dictionary)
    
    # set working directory
    work_dir = settings_dictionary["work_dir"]
    
    
    #set PE files from directory
    PE_data_dir = settings_dictionary["PE_data_dir"]
    
    filesname = get_PE_file(PE_data_dir)
    print(filesname)
    for i in range(len(filesname)):
        if i%2 == 0:
            read1_file = "test data/" + filesname[i]
            #print(type(read1_file))
           # print("the first file",read1_file)
            read2_file = "test data/" + filesname[i+1]
            #print("the second file",read2_file)
            average_read_length = caculate_read_length(read1_file, read2_file)
            print(average_read_length)

