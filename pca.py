import pandas as pd

df = pd.read_csv(
    filepath_or_buffer='iristrain.data',
    header=None,
    sep=',')

df.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
df.dropna(how="all", inplace=True) # drops the empty line at file-end

df.tail()

X = df.ix[:,0:4].values
y = df.ix[:,4].values
 
from matplotlib import pyplot as plt
import numpy as np
import math

label_dict = {1: 'Iris-Setosa',
              2: 'Iris-Versicolor',
              3: 'Iris-Virgnica'}

feature_dict = {0: 'sepal length [cm]',
                1: 'sepal width [cm]',
                2: 'petal length [cm]',
                3: 'petal width [cm]'}
##
##with plt.style.context('seaborn-whitegrid'):
##    plt.figure(figsize=(8, 6))
##    for cnt in range(4):
##        plt.subplot(2, 2, cnt+1)
##        for lab in ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'):
##            plt.hist(X[y==lab, cnt],
##                     label=lab,
##                     bins=10,
##                     alpha=0.3,)
##        plt.xlabel(feature_dict[cnt])
##    plt.legend(loc='upper right', fancybox=True, fontsize=8)
##
##    plt.tight_layout()
##    plt.show()

##from sklearn.preprocessing import StandardScaler
##
X_std = X #= StandardScaler().fit_transform(X)


import numpy as np
mean_vec = np.mean(X_std, axis=0)
cov_mat = (X_std - mean_vec).T.dot((X_std - mean_vec)) / (X_std.shape[0]-1)

#print('Covariance matrix \n%s' %cov_mat)

auto_valor, auto_vetor = np.linalg.eig(cov_mat)

print('auto_valor \n%s' %auto_valor)
print('\auto_vetor \n%s' %auto_vetor)


for av in auto_vetor:
   print np.linalg.norm(av)
 
 

# Make a list of (eigenvalue, eigenvector) tuples
eig_pairs = [(np.abs(auto_valor[i]), auto_vetor[:,i]) for i in range(len(auto_valor))]

# Sort the (eigenvalue, eigenvector) tuples from high to low
eig_pairs.sort(key=lambda x: x[0], reverse=True)

# Visually confirm that the list is correctly sorted by decreasing eigenvalues
print('Eigenvalues in descending order:')
for i in eig_pairs:
    print(i)

##print eig_pairs


