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

from sklearn.metrics.pairwise import additive_chi2_kernel

# Function: kcluster
#
# Inputs:
# @theta: the kernel parameter vector, specifiying kernel parameters and weights
# @x: the first input vector
# @y: the second input vector

# TODO: Shoudl the kernel still work if (x,y) are a different size? For example,
# if a particular cancer doesn't have miRNA data and x/y are size 60 instead of
# 80 it should still be cool right? -> Therefore, we don't have to specify in
# this function what features we're looking at right?

def kcluster(theta, x, y):
    
    ###############################
    #    Global Data Structures   #
    ###############################
    
    # Kernel Parameter Vector (Theta):
    # Each type of kernel has three copies of the following (contiously):
    # 
    # Regular Kernel Documentation: http://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics.pairwise 
    #
    # This is just for regular kernels (use some of these)?:
    # Cosine Similarity: weight 
    # Linear Kernel: weight
    # Polynomial Kernel: weight, degree, gamma
    # Manhattan Kernel: weight
    # Pairwise Kernel: weight
    # RBF Kernel: weight, gamma
    # Laplacian Kernel: weight, gamma
    # Chi2 Kernel: weight, gamma
    # Chi2 Additive Kernel: weight 
    # Number of Clusters (integer)
    #
    # Or should the kernel approximations be enough?
    # 
    # Approximate Kernels Documetation: http://scikit-learn.org/stable/modules/classes.html#module-sklearn.kernel_approximation
    # AdditiveChi2: weight, sample_steps
    # Nystroem: weight, gamma, (random_state = 1)
    # RBFSampler: weight, gamma, (random_state = 1)
    # SkewedChi2: weight, skewedness, n_components, (random_state = 1)
    #
    # The theta vector should be size 43 in length according to the specs given
    # above. (if using just regular kernels)
    
    # Inputting 

    
    print additive_chi2_kernel(x,y)
    #TODO: Run K-Means Clustering on the clusters that are specified
    
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y= [3, 4, 6, 8, 6, 4, 3, 2, 4, 3]
t = [0]
kcluster(t,x,y)