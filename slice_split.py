
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

def slice(n,fs,start,stop):

	# Function for coarse-graining input trajectory by slicing every nth frame

	i = 0
	with open(file, 'r') as inp:
		with open('trj_sliced.xyz', 'w') as out:
			while i*n < stop:
				next_n = list(islice(inp, n))
				if i*n < start:
					i += 1
					continue
				if not next_n:
					break
				it = int(i-start/n+1)
				print('Processing frame number %i' % it, end='\r')
				j = 0
				for line in next_n:
					if j < fs:
						out.write('%s' % line)
						j += 1
					else:
						break
				i += 1

			print('\nDone!')

def split(n,start,stop):

	# Function for splitting input trajectory into multiple subtrajectories

	i = 0
	with open(file, 'r') as inp:
		while i*n < stop:
			next_n = list(islice(inp, n))
			if i*n < start:
				i+=1
				continue
			if not next_n:
				break
			it = int(i-start/n+1)
			print('Processing chunk number %s' % it, end='\r')
			with open('trj_%s.xyz' % i, 'w') as out:
				for line in next_n:
					out.write('%s' % line)
			i += 1

		print('\nDone!')

def frame_size(file):

	# Function for calculating the number of lines per frame in input trajectory

	count = None
	with open(file) as f:
		for line in f:
			# Count number of lines between the 1st and 2nd occurence of 'time'
			if 'time' in line:
				if count is None:
					count = 1
				else:
					break
			elif count is not None:
				count += 1
	return count

def main():

	print('Initializing...')

	# Get number of lines per frame in given .xyz file (number of atoms + headers..)
	# File must contain in each frame one regularly occurring pattern to get number of lines!
	fs = frame_size(file)

	start = int(first*fs)
	stop = int(last*fs)

	if chunk is None:
		n = int(ts*fs)
		slice(n,fs,start,stop)
	else:
		n = int(chunk*fs)
		split(n,start,stop)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Split or coarse-grain MD trajectory')
	parser.add_argument('-i','--input',required=True,help='Input trajectory (.xyz)')
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('-n','--num',type=int,help='Number of frames in split subtrajectory')
	group.add_argument('-ts','--timestep',type=int,help='New stepsize in coarse-grained trajectory')
	parser.add_argument('-f','--first',default=0,type=int,help='First frame to include')
	parser.add_argument('-l','--last',default=1e32,type=int,help='Last frame to include')
	args = vars(parser.parse_args())
	file = args['input']
	chunk = args['num']
	ts = args['timestep']
	first = args['first']
	last = args['last']
	main()
