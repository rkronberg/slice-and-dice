"""
Tool for splitting and coarse-graining (slicing) .xyz MD trajectories.
Possibly useful for handling huge trajectory files.

author: Rasmus Kronberg
rasmus.kronberg@aalto.fi

"""

from argparse import ArgumentParser
import methods

def parse():

	# Parse command line arguments

	p = ArgumentParser(description='Split or coarse-grain MD trajectory')
	p.add_argument('-i', '--input', required=True, help='Input trajectory (.xyz)')
	p.add_argument('-f', '--first', default=0, type=int, help='First frame to include')
	p.add_argument('-l', '--last', default=int(1e16), type=int, help='Last frame to include')
	g1 = p.add_mutually_exclusive_group(required=True)
	g2 = p.add_mutually_exclusive_group(required=True)
	g1.add_argument('-n', '--nframes', type=int, help='Number of frames in split subtrajectory')
	g1.add_argument('-ts', '--step', type=int, help='New stepsize in coarse-grained trajectory')
	g2.add_argument('-r', '--regex', type=str, help='Regular expression to get frame size')
	g2.add_argument('-fs', '--fsize', type=int, help='Number of lines per frame')

	return vars(p.parse_args())

def main():

	print('Initializing...')

	args = parse()
	file = args['input']
	regex = args['regex']
	fsize = args['fsize']
	nframes = args['nframes']
	step = args['step']
	first = args['first']
	last = args['last']

	with open(file, 'r') as inp:
		# If fsize is not specified, tries to get number of lines per frame (number 
		# of atoms + headers) based on given expression that repeats regularly every 
		# frame (in .xyz files this may be 'time' or 'frame' etc..)
		if regex is not None:
			fsize = methods.frame_size(inp, regex)
			if fsize is None:
				print('Regex not found. Check your input or set frame size by hand.')
				quit()

		# Rewind file to specified start and slice or split trajectory 
		inp.seek(first*fsize)
		if step is not None:
			methods.slice(inp, step, fsize, first, last)
		else:
			methods.split(inp, nframes, fsize, first, last)

	print('\nDone!')

if __name__ == '__main__':
	main()
