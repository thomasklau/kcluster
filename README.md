# kcluster - Multiple Genomics Cancer Subtype Discovery using Multiple Kernel Learning

kcluster is an open-source toolkit for applying kernel methods to cancer subtype discovery, specifically using Multiple Kernel Learning, k-means clustering, and stochastic optimization to generate subtype clusters for a given cancer dataset.

kcluster provides a Python API that can be run on TCGA (The Cancer Genome Atlas) datasets.

To read more about kcluster, please refer to ["Kernel Learning Framework For Cancer Subtype Analysis with Mutli-omics Data Integration"](https://github.com/thomasklau/kcluster/blob/master/Kernel%20Learning%20Framework%20for%20Cancer%20Subtype%20Analysis%20with%20Multi-omics%20Data%20Integration.pdf) (Bradbury, Lau, Roy 2015).

# Dependencies
[**Python (>=2.6)**](https://www.python.org/downloads/)

[**scikit-learn (>=0.17)**](http://scikit-learn.org/stable/install.html)

[**numpy (>=1.6.1)**](http://www.numpy.org/)

[**scipy (>=0.9)**](http://www.scipy.org/install.html)

[**requests (>=2.8.1)**](http://docs.python-requests.org/en/latest/)

[**firebrowse (>=0.1.5)**](https://confluence.broadinstitute.org/display/GDAC/fbget)

It is recommended to install these dependencies via the [**Anaconda**](https://www.continuum.io/downloads) package.

If you don't want to use Anaconda, you can install dependencies manually using `pip` inside a [**virtualenv**](http://docs.python-guide.org/en/latest/dev/virtualenvs/)