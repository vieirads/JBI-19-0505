#!/home/dsvieira/anaconda3/bin/python

# author     : Denner Vieira (dennersvieira@gmail.com)
# created on : 09/01/2019 (dd/mm/yyyy)
# last update: 18/02/2019 (dd/mm/yyyy)

# import necessary packages
import numpy as np
import pandas as pd
import sys

# list with species pairs
sp_pairs = []

if len(sys.argv) != 3:
	print("The program needs two arguments:")
	print("n N")
	print("Where n is the number of species")
	print("and N is the number of links to create.")
	sys.exit(1)

# number of species
n = int(sys.argv[1])

# species to consider [1, n]
sp_arr = np.arange(1, n+1)

# number of pairs to consider
N = int(sys.argv[2])

# loop considering the number of pairs we want
for i in range(N): 
	# sort the first species
	sp1 = np.random.choice(sp_arr)
	sp2 = np.random.choice(sp_arr)

	# selecting a different species to make pair with sp1
	while sp2 == sp1:
		sp2 = np.random.choice(sp_arr)

	# random value (0, 1] for the sympatry of the pair sp1, sp2
	symp = np.random.uniform()

	# if the the species have overlapping area
	# we consider the species pair if they have
	# not been already sorted
	if (symp != 0) and ([sp1, sp2] not in sp_pairs):
			sp_pairs.append([sp1, sp2, symp])

# display the species pairs and their sympatry level as a pd.DataFrame	
sp_pairs_df = pd.DataFrame(sp_pairs, columns=['sp1', 'sp2', 'symp'])

print(sp_pairs_df)

# print(sp_pairs_df[sp_pairs_df['sp1'] == 30])