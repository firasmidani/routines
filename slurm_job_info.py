#!/usr/env/bin python

#title         :releaseHeldJobs.py 
#description   :checks status of slurm job array and releases pending held jobs
#author        :Firas Said Midani
#date          :2015.04.24
#version       :1.0
#usage         :python releaseHeldJobs.py 
#arguments     :text file with job array number

# given a job_array_main_id 
# grab information about all jobs in the array from slurm

##INPUT 
# job id
# desired attribute (any attribute that "scontrol show job" would return about a job)

##OUTPUT
# information of desired attribute

import pandas as pd, \
       sys, \
       os

import subprocess

job_array_main_id = sys.argv[1]
job_arg_out       = sys.argv[2]

proc         = subprocess.Popen(["scontrol","show","job",job_array_main_id],stdout=subprocess.PIPE,shell=False)
(output,err) = proc.communicate()

output = output.split('\n\n')[:-1];

#for each job, create a dictionary with job features and their settings
job_info={}
for job in range(len(output)):
	single_job = " ".join(output[job].split('\n   ')).split(' ')
	job_dict={}
	for value in single_job:
		job_dict[value.split('=')[0]]=value.split('=')[1]
	job_info[job_dict['JobId']]=job_dict;

print job_info[job_array_main_id][job_arg_out] 

