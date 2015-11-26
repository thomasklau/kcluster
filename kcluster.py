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

# Kernels
from sklearn.metrics.pairwise import additive_chi2_kernel
from sklearn.metrics.pairwise import chi2_kernel
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import polynomial_kernel
from sklearn.metrics.pairwise import rbf_kernel
from sklearn.metrics.pairwise import laplacian_kernel
from sklearn.metrics.pairwise import sigmoid_kernel

# Function: kcluster
#
# Inputs:
# @theta: the kernel parameter vector, specifiying kernel parameters and weights
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
    # The theta vector should be size 43 in length according to the specs given
    # above.
# @x: the first input array-like of shape (n_samples_X = 1, n_features)
# @y: the second input array-like of shape (n_samples_Y = 1, n_features)

def kcluster(theta, x, y):
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
        
    print kernelResult
    #TODO: Run K-Means Clustering on the clusters that are specified
    
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [3, 4, 5, 2, 3, 5, 7, 9, 3, 2]
t = random.sample(range(1,100),60)
kcluster(t,x,y)