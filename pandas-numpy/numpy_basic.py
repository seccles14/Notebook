'''
Basic Operations Exercise in Matrix Operations
'''

import numpy as np


gene_list = np.array([['a2m', 'fos', 'brca2', 'cpox']])
times_list = np.array(['4h','12h','24h','48h'])

values0 = np.array([[.12,0.08,0.06,0.02]])
values1 = np.array([[0.01,0.07,0.11,0.09]])
values2 = np.array([[0.03,0.04,0.04,0.02]])
values3 = np.array([[0.05,0.09,0.11,0.14]])

x = np.vstack([values0, values1, values2, values3])
print(x)








########################################################
## which gene has the maximum mean expression value?
########################################################

#print("\nQuestion 4")
#gene_means = X.mean(axis=1)
#gene_mean_ind = np.argmax(gene_means)
#print("gene with max mean expression value: %s (%s)"%(row_names[gene_mean_ind],gene_means[gene_mean_ind]))

########################################################
## sort the gene names by the max expression value
########################################################

#gene_names = row_names
#print("sorted gene names: %s"%(gene_names[np.argsort(np.max(X,axis=1))]))
