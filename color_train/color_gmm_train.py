
import numpy as np
import argparse


#  read a file of lines 


def file2array(filename):
	pass


def calclogProb(x, mu, cov):
	logval = -np.log(((2*np.pi) ** (len(mu)/2)) * np.linalg.det(cov) **(1/2) )
	logval = logval - 0.5 * ((x-mu).T.dot( np.linalg.inv(cov).dot(x-mu)))

	# part1 = 1. / ( ((2* np.pi)**(len(mu)/2)) * (np.linalg.det(cov)**(1./2)) )
	# part2 = (-1./2) * ((x-mu).T.dot(np.linalg.inv(cov))).dot((x-mu))
	return logval




if __name__ == '__main__':

	ap = argparse.ArgumentParser()
	ap.add_argument('-f', '--filename')
	args = vars(ap.parse_args())

	d1 = np.loadtxt(args['filename'], dtype='float32')
	mean = np.mean(d1, axis = 0)
	cov = np.cov(d1, rowvar = 0)

	outname = args['filename'].split('.')[0]
	outfile = outname + '_mean' + '.txt'

	mean = mean[:, np.newaxis]
	mean = mean.T
	mean = np.array(mean)
	cov = np.array(cov)
	# print mean.shape
	finmat = np.concatenate((mean, cov), axis = 0)

	# print finmat
	np.savetxt(outfile, mean, fmt='%-5.2f')


	# print calclogProb(np.array([10, 100, 100]), mean, cov)




