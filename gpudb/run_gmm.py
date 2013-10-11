#!/usr/bin/python
import os

for file in os.listdir("/home/kai/projects/gpudb/test/ssb_test/"):
	if file[-3:] == 'sql':
		os.chdir("/home/kai/projects/gpudb/")
		cmd = r'/home/kai/projects/gpudb/translate.py' + r' /home/kai/projects/gpudb/test/ssb_test/' + file + r' /home/kai/projects/gpudb/test/ssb_test/ssb.schema'
		os.system(cmd)
		#os.system('/home/kai/projects/gpudb/translate file /home/kai/projects/gpudb/test/ssb_test/ssb.schema')
		os.chdir("/home/kai/projects/gpudb/src/cuda")
		os.system('make gpudb')
		output = file[0:-3] + 'solo'
		#! New GMM add
		os.chdir("/home/kai/projects/gpudb-explore/src")
		cmd = r'LD_PRELOAD=/home/kai/projects/gpudb-explore/src/libgmm.so /home/kai/projects/gpudb/src/cuda/GPUDATABASE --datadir /home/kai/projects/gpudb/data' + r' > ' + r'/home/kai/projects/trace/file/' + output
		#! OLD libicept test
		#cmd = r'LD_PRELOAD=/home/kai/projects/lib-intercept/libicept.so /home/kai/projects/gpudb/src/cuda/GPUDATABASE --datadir /home/kai/projects/gpudb/data' + r' > ' + r'/home/kai/projects/trace/file/' + output
		os.system(cmd)
