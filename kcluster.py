# ---------------------------------------------------------------------------#
#                                 kCluster                                   #
# ---------------------------------------------------------------------------#
#                                                                            #
# This file provides the framework for running the kCluster training         #
# algorithm on a specified dataset. When running the kCluster algorithm, the #
# user may additionally specify the types of data (Copy Number, RPPA, mRNA,  #
# miRNA, and/or methylation) provided in the input dataset. The user may     #
# also specify the type of cancer from the TCGA (The Cancer Genome Atlas)    #
# database.                                                                  #
#                                                                            #
# Licensed under the Apache License, Version 2.0 (the "License"); you may    #
# not use this file except in compliance with the License. You may obtain a  #
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.         #
# Unless required by applicable law or agreed to in writing, software        #
# distributed under the License is distributed on an "AS IS" BASIS,          #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   #
# See the License for the specific language governing permissions and        #
# limitations under the License.                                             #
# ---------------------------------------------------------------------------#

# IMPORTS
import numpy as np
import scipy as sp
import random
from kmeans import kmeans
from kmeans import kmeanssample

# Kernels
from sklearn.metrics.pairwise import additive_chi2_kernel
from sklearn.metrics.pairwise import chi2_kernel
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import polynomial_kernel
from sklearn.metrics.pairwise import rbf_kernel
from sklearn.metrics.pairwise import laplacian_kernel
from sklearn.metrics.pairwise import sigmoid_kernel

################################
#       GLOBAL VARIABLES       #
################################
# theta: the kernel parameter vector, specifiying kernel parameters and weights
    # Theta Variable Layout:
    # Each type of kernel has three copies of the following (contiously):
    # 
    # Additive Chi2 Kernel: weight 
    # Chi2 Kernel: weight, gamma
    # Cosine Similarity: weight
    # Linear Kernel: weight
    # Polynomial Kernel: weight, degree, gamma, coef0
    # RBF Kernel: weight, gamma
    # Laplacian Kernel: weight, gamma
    # Sigmoid Kernel: weight
    # Number of Clusters: integer
    #
    # Kernel Documentation: http://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics.pairwise 
    #
    # The theta vector should be size 46 in length according to the specs given
    # above.

theta = 0

# Function: calculateMultipleKernel
# Calculates the value of the linear combintation of kernels given the kernel
# input vector and the input vectors x and y.
# 
# Inputs:
# @x: the first input array-like of shape (n_samples_X = 1, n_features)
# @y: the second input array-like of shape (n_samples_Y = 1, n_features)

def calculateMultipleKernel(x, y):
    theta = random.sample(range(1,47),46) # given a random theta for now

    # Convert our 2d arrays to numpy arrays
    x = np.array(x)
    y = np.array(y)
    
    # Reshape the array-like input vectors since we only have one sample
    x = x.reshape(1,-1)
    y = y.reshape(1,-1)
    
    # Variables to aggregate the kernel result
    kernelResult = 0;
    index = 0; 
    
    for i in range(0,3):
        kernelResult += theta[index] * additive_chi2_kernel(x,y)
        index += 1
        
    for i in range(0,3):
        kernelResult += theta[index] * chi2_kernel(x,y,theta[index+1])
        index += 2
    
    for i in range(0,3):
        kernelResult += theta[index] * cosine_similarity(x,y)
        index += 1
    
    for i in range(0,3):
        kernelResult += theta[index] * linear_kernel(x,y)
        index += 1
    
    for i in range(0,3):
        kernelResult += theta[index] * polynomial_kernel(
            x,y,theta[index+1],theta[index+2], theta[index+3])
        index += 4
        
    for i in range(0,3):
        kernelResult += theta[index] * rbf_kernel(x,y,theta[index+1])
        index += 2
        
    for i in range(0,3):
        kernelResult += theta[index] * laplacian_kernel(x,y,theta[index+1])
        index += 2
    
    for i in range(0,3):
        kernelResult += theta[index] * sigmoid_kernel(x,y,theta[index+1])
        index += 2
        
    return kernelResult
    
# sample input X Array; each row is a different sample, each column is a feature
x = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
     [7, 2, 0, 2, 3, 7, 10, 3, 2, 3]]

# randomly generated theta of length 46
theta = random.sample(range(1,47),46) # given a random theta for now

# perform kMeansClustering and return the clusters
if __name__ == "__main__":
    import random
    import sys
    from time import time

    N = 10000
    dim = 10
    ncluster = 10
    kmsample = 100  # 0: random centres, > 0: kmeanssample
    kmdelta = .001
    kmiter = 10
    metric = calculateMultipleKernel  # "chebyshev" = max, "cityblock" L1,  Lqmetric
    seed = 1

    np.random.seed(seed)
    random.seed(seed)

    print "N %d  dim %d  ncluster %d  kmsample %d  metric %s" % (
        N, dim, ncluster, kmsample, metric)
    X = np.random.exponential( size=(N,dim) )
        # cf scikits-learn datasets/
    t0 = time()
    if kmsample > 0:
        centres, xtoc, dist = kmeanssample( X, ncluster, nsample=kmsample,
            delta=kmdelta, maxiter=kmiter, metric=metric, verbose=2 )
    else:
        randomcentres = randomsample( X, ncluster )
        centres, xtoc, dist = kmeans( X, randomcentres,
            delta=kmdelta, maxiter=kmiter, metric=metric, verbose=2 )
    print "%.0f msec" % ((time() - t0) * 1000)

    # also ~/py/np/kmeans/test-kmeans.py