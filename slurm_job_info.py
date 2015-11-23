#!/usr/env/bin python

#title         :slurm_job_info.py 
#description   :checks attributes of cluster job using slurm scontrol
#author        :Firas Said Midani
#3-mai         :firas.midani@duke.edu
#date          :2015.11.23
#version       :1.0
#usage         :python slurm_job_info.py [job id] [job attribute] 

# given a job_array_main_id 
# grab information about all jobs in the array from slurm

##ARGUMENTS
# job id
# desired attribute (any attribute that "scontrol show job" would return about a job)

##OUTPUT
# information of desired attribute

import \
pandas as pd, \
subprocess,   \
sys, \
os

## process arguments
job_array_main_id = sys.argv[1]
job_arg_out       = sys.argv[2]

## necessary for importing shell output into python 
proc         = subprocess.Popen(["scontrol","show","job",job_array_main_id],stdout=subprocess.PIPE,shell=False)
(output,err) = proc.communicate()
output       = output.split('\n\n')[:-1];

#for each job, create a dictionary with job features and their settings
job_info={}
for job in range(len(output)):
	job_dict={}
	single_job = " ".join(output[job].split('\n   ')).split(' ')
	for value in single_job:
		job_dict[value.split('=')[0]]=value.split('=')[1]
	job_info[job_dict['JobId']]=job_dict;

print job_info[job_array_main_id][job_arg_out] 

