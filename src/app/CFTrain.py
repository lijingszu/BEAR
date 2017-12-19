"""
CFTrain.py
BEAR

Created by Jing Li on Dec.18, 2017.
Copyright (c) 2017 jing.li@istb.unibe.ch. All rights reserved.
"""

"""
Goal: load parameters and trainer API
Step: 1. help_print
	  2. TrainGeneral()
	  3. save tree
"""

# from optparse import OptionParaser
from argparse import ArgumentParser
from ..detector.CF.MultiSourceCFTrainer.py import hello 

def print_usage():

	# print '[ train a classification forest with Haar features ]'
	# print 'python CFTrain.py --file iniFile\n'

	# print '[ create an example ini file ]'
	# print 'python CFTrain.py --example iniFile\n'

	# print '[ valid normalization type ]'
	# print 'NONE, UNIT_NORM, MAX_ONE, MIN_MAX, ZERO_MEAN_ONE_STD\n' 
	
	parser = ArgumentParser()

	parser.add_argument('-f', '--file', dest='iniFile', 
						help='ini file name for loading parameters') #, metavar='FILE'

	parser.add_argument('-e', '--example', dest='egIniFile',
						help='create an example ini file')

	args = parser.parse_args()

	if args.egIniFile:
		WriteDefaultIni(args.egIniFile)
		exit()

	TrainGeneral()

	hello()



def TrainGeneral():
	print "Hello, TrainGeneral!"

def WriteDefaultIni(path):
	print "Hello, WriteDefaultIni!"
	print 'path =',path


def main():
	print 'Hello, CFTrain'
	print_usage()

	# parser = ArgumentParser()

	# parser.add_argument('-f', '--file', dest='iniFile', 
	# 					help='ini file name for loading parameters') #, metavar='FILE'

	# parser.add_argument('-e', '--example', dest='iniFile',
	# 					help='create an example ini file')

	# args = parser.parse_args()


if __name__ == '__main__':
	main()