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

#access the driectory of Paired-end data 
def get_PE_file(settings_dictionary):


    # set working directory
    work_dir = settings_dictionary["work_dir"]

    #set PE files from directory
    PE_data_dir = work_dir + settings_dictionary["PE_data_dir"]
    PE_data_dir_list = os.listdir(PE_data_dir)

    if '.DS_Store' in PE_data_dir_list:
        PE_data_dir_list.remove('.DS_Store')

    return PE_data_dir,PE_data_dir_list
    
#access to the two paired-end fastq files
def get_r1_r2(PE_data_dir,item):
    
    
    each_PE_dir = ''.join([PE_data_dir, item])
        
    each_dir_files = os.listdir(each_PE_dir)
    if '.DS_Store' in each_dir_files:
        each_dir_files.remove('.DS_Store')

    read1_file =  each_dir_files[0]
    read1_file = ''.join([each_PE_dir,"/", read1_file])
    read2_file =  each_dir_files[1]
    read2_file = ''.join([each_PE_dir,"/",read2_file])

    return read1_file, read2_file

#caculate the mean read length and add to the filename 
def caculate_read_length(read1, read2):
    
    num_line = 0
    base1 = []
    base2 = []
    
    file1_contents = open(read1, "r").read().strip().split("\n")
    file2_contents = open(read2, "r").read().strip().split("\n")
    
    num_lines = len(file1_contents)
    num_read = num_lines/2   
    
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
    average_read_length = ''.join(["_r" + str(average_read_length)])
    read1_new = ''.join([read1 + average_read_length])
    if average_read_length in read1:
        pass
    else:
        os.rename(read1,read1_new)
    read2_new = ''.join([read2 + average_read_length])
    if average_read_length in read2:
        pass
    else:
        os.rename(read2,read2_new)
    


if __name__ == '__main__':
    
    # parsing the parameters
    settings_file = sys.argv[1]
    settings_dictionary = settings_parser(settings_file)  
    PE_data_dir,PE_data_dir_list = get_PE_file(settings_dictionary)
    for item in PE_data_dir_list:
        read1_file, read2_file = get_r1_r2(PE_data_dir,item)
        caculate_read_length(read1_file, read2_file)
    
