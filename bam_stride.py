# -*- coding: utf-8 -*-
# arg1 : bam file
# arg2 : filename output.bam
# arg3 : stride
# arg4 : shift

################################ IMPORT ################################################################################################
import os
import sys

scriptpath = "/home/mcardon/Mel/Code/sequana/sequana/"
sys.path.append(os.path.abspath(scriptpath))
import pacbio

################################ PARAMETERS ##############################################################################################

filename_BAM = str(sys.argv[1])
filename_output = str(sys.argv[2])
stride_nb = int(sys.argv[3])
shift = int(sys.argv[4])

################################ INPUT DATA ##############################################################################################

raw_BAM = pacbio.PacBioInputBAM(filename_BAM)


################################ EXECUTE ##############################################################################################

raw_BAM.stride(filename_output, stride=stride_nb, shift=shift)

name = "subreads_abscessus_v2_env"
#dict_shift = {1:"b", 2:"c"}
#dict_shift = {2:"c"}
dict_shift = {0:"a"}

"""
# batch moode
for div in [109,55,30,22,11,5]:
	filename_output = name + str(int(545/div)) + "X_" +".bam"
	raw_BAM.stride(filename_output, stride=div, shift=shift)
"""


"""
# batch moode
for div in [5,10,15,20,25,30,50]:
	for shift in dict_shift.keys():
		filename_output = name + str(int(500/div)) + "X_" + dict_shift[shift] +".bam"
		raw_BAM.stride(filename_output, stride=div, shift=shift)
"""

################################ PLOTS ##############################################################################################









