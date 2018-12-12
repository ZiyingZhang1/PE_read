
## The objective

Caculate the mean read length of Paired end fastq files



## Getting started

To get started on using the scripts, the overarching directory PE_read, which contains all the needed files, scripts and directories. 
User need to change the path(work_dir) in Setting.txt. And run the command below on server or in terminal. 

##
```python
python3.7 readlength.py Setting.txt
```
## Lay-out of directories and files. 
users need to store data in the layout shown as below. (See test data)

   * readlength.py
   
   * Setting.txt
   
   * testdata
   
      * Paired_end_fastq_files1
	  
	     * Read_1_fastq
		 
		 * Read_2_fastq
		 
	  * Paired_end_fastq_files2
	  
	     * Read_1_fastq
		 
		 * Read_2_fastq
	  
	   

