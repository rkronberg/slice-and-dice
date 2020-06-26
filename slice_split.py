
"""
Tool for splitting and coarse-graining
(slicing) .xyz MD trajectories. Possibly
useful for handling huge trajectory files.

TODO: Implement parallel I/O for even 
larger files

author: Rasmus Kronberg
rasmus.kronberg@aalto.fi
"""

from itertools import islice
import argparse

def slice(n,fs):

	i = 0
	with open(file, 'r') as inp:
		with open('trj_sliced.xyz' % i, 'w') as out:
			while True:
				next_f = list(islice(inp, n))
				if not next_f:
					break
				print('Processing chunk number %s' % (i+1))
					j = 0
					for line in next_f:
						if j < fs:
							out.write('%s' % line)
							j += 1
						else:
							break
				i += 1

def split(n):

	i = 0
	with open(file, 'r') as inp:
		while True:
			next_n = list(islice(inp, n))
			if not next_n:
				break
			print('Processing chunk number %s' % (i+1))
			with open('trj_%s.xyz' % i, 'w') as out:
				for line in next_n:
					out.write('%s' % line)
			i += 1

def frame_size(file):

	count = None
	with open(file) as f:
		for line in f:
			if 'time' in line:
				if count is None:
					count = 1
				else:
					break
			elif count is not None:
				count += 1
	return count

def main():

	print('Initializing...\n')
	fs = frame_size(file)
	n = int(chunk*fs)

	if SPLIT:
		split(n)
	elif SLICE:
		slice(n,fs)

			
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Split or slice MD trajectory')
	parser.add_argument('-i','--input',required=True,help='Input trajectory (.xyz)')
	parser.add_argument('-n','--num',required=True,type=int,
		help='Stepsize in sliced trajectory/Number of frames in split subtrajectory')
	parser.add_argument('-sp','--split',action='store_true',help='Split trajectory into subtrajectories')
	parser.add_argument('-sl','--slice',action='store_true',help='Coarse-grain (slice) trajectory')
	args = vars(parser.parse_args())
	file = args['input']
	chunk = args['num']
	SPLIT = args['split']
	SLICE = args['slice']
	main()