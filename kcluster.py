"""
Tools to an run an alternating UMKL algorithm on TCGA data.
"""

import numpy as np
import matplotlib.pyplot as plt

class Clusterer():
    """
    Class for clustering sparsely labeled data. Includes visualization
    functionality.
    """
    def __init__(self,datafile=None,generate_test=False,kernel_dim=10):
        if generate_test:
            self.X = self.generate_test_data()
        else:
            self.X = self.read_data(datafile)

        # record dimensions
        self.dim,self.n = self.X.shape # (n=samples, dim=dimensions)
        self.m = kernel_dim

        # initialize P
        self.P = np.dot(self.X.T,self.X)

        # initialize M-matrix
        self.M = np.tile(np.einsum('ij,ji->i',self.X.T,self.X),(n,1)).T
        self.M += np.tile(np.einsum('ij,ji->i',self.X.T,self.X),(n,1))
        self.M += -2*P

        # initialize mu
        self.mu = np.ones(self.m)/self.m

    def generate_test_data(self):
        """
        Generates 2D test data by randomly sampling 4 multivariate gaussians
        """
        data = np.zeros((2,100))
        data[:,:25] = np.random.multivariate_normal([20,20], [[20,0],[0,20]], 25).T
        data[:,25:50] = np.random.multivariate_normal([-20,20], [[5,0],[0,20]], 25).T
        data[:,50:75] = np.random.multivariate_normal([20,-20], [[20,0],[0,5]], 25).T
        data[:,75:100] = np.random.multivariate_normal([-20,-20], [[5,0],[0,5]], 25).T

        return data

    def plot_data(self):
        plt.plot(self.X[0,:],self.X[1,:],'o')
        plt.axis('equal')
        plt.show()

    def read_data(self,datafile):
        with open(datafile) as f:
            return np.load(f,allow_pickle=False)

    def cluster(self):
        print ("Clustering...")

    def get_clustering(self):
        pass
    def get_optimal_kernel(self):
        pass

    def display_2d(self):
        pass

if __name__ == "__main__" :
    c = Clusterer(generate_test=True)
    c.plot_data()
