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

import sklearn

def kcluster(theta):
    
    ###############################
    #    Global Data Structures   #
    ###############################
    
    # Kernel Parameter Vector (Theta):
    # Each type of kernel has three copies of the following (contiously):
    # 
    # Kernel Documentation: http://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics.pairwise 
    #
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
    # The theta vector should be size 43 in length according to the specs given
    # above.
    
    print 'hi'