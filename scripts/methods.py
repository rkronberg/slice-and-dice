from itertools import islice

def slice(inp, step, fsize, first, last):

	# Coarse-grain input trajectory by slicing every nth frame
	with open('trj_sliced.xyz', 'w') as out:
		for i, frame in enumerate(range(first, last, step)):
			next_n = list(islice(inp, step*fsize))
			if not next_n:
				break
			print('Processing frame number %i' % i, end='\r')
			for j, line in enumerate(next_n):
				if j < fsize:
					out.write('%s' % line)
				else:
					break

def split(inp, nframes, fsize, first, last):

	# Split input trajectory into multiple subtrajectories
	for i, frame in enumerate(range(first, last, nframes)):
		next_n = list(islice(inp, nframes*fsize))
		if not next_n:
			break
		print('Processing chunk number %i' % i, end='\r')
		with open('trj_%s.xyz' % i, 'w') as out:
			for line in next_n:
				out.write('%s' % line)

def frame_size(inp, regex):

	# Calculate the number of lines per frame in input trajectory
	count = None
	for line in inp:
		# Count number of lines between the 1st and 2nd occurence of regex
		if regex in line:
			if count is None:
				count = 1
			else:
				break
		elif count is not None:
			count += 1

	return count
