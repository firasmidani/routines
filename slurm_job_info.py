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
# check the status of all jobs in the array
# output list of jobs that are PENDING due to Job_requeued_in_held_state

# NOTES: this can be broken up into sub-functions
# 1) get job information into dictionary form for an array
# 2) given information in a pickle file, read and check for held jobs
# 3) given held jobs, release them   

# CREATES
#  txt file for job_array_info (default path)
#  txt file for held jobs (default path) 

# DESTROYS
#  none

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

