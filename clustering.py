# needed imports
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import scipy.cluster.hierarchy as sch
import numpy as np

# This determines the clustering method. Check https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html#scipy.cluster.hierarchy.linkage for details
method = 'average'  # average, ward, ...


class cluster():
    def __init__(self, cluster, projections):
        self.cluster = cluster
        self.bundles = []
        self.n = 0

        self.summation = []
        for factor in range(len(projections)):
            self.summation.append([])
            for projection in range(len(projections[factor])):
                self.summation[factor].append(0)

    def add_bundle(self, bundle):
        self.bundles.append(bundle)
        self.n += 1

        # adds 1 to one projection - specified in bundle - for each factor
        for i in range(len(self.summation)):
            self.summation[i][bundle[i]-1] += 1

    def get_mixture(self):
        mixture = []
        for factor in range(len(self.summation)):
            mixture.append([])
            for projection in range(len(self.summation[factor])):
                mixture[factor].append(
                    self.summation[factor][projection]/self.n)
        return mixture


def create_distance_matrix(bundles):
    # Need to convert the class projection bundle in a list of bundles
    bundles_list = []
    for object in bundles:
        bundles_list.append(object.bundle)

    bundles = np.array(bundles_list)
    # Hamming metric: 0 if same, 1 if different
    d = sch.distance.pdist(bundles, 'hamming')
    # generate the linkage matrix
    Z = linkage(d, method)
    return Z


def fancy_dendrogram(*args, **kwargs):
    max_d = kwargs.pop('max_d', None)
    if max_d and 'color_threshold' not in kwargs:
        kwargs['color_threshold'] = max_d
    annotate_above = kwargs.pop('annotate_above', 0)

    ddata = dendrogram(*args, **kwargs)

    if not kwargs.get('no_plot', False):
        plt.title('Hierarchical Clustering Dendrogram (truncated)')
        plt.xlabel('sample index or (cluster size)')
        plt.ylabel('distance')
        for i, d, c in zip(ddata['icoord'], ddata['dcoord'], ddata['color_list']):
            x = 0.5 * sum(i[1:3])
            y = d[1]
            if y > annotate_above:
                plt.plot(x, y, 'o', c=c)
                plt.annotate("%.3g" % y, (x, y), xytext=(0, -5),
                             textcoords='offset points',
                             va='top', ha='center')
        if max_d:
            plt.axhline(y=max_d, c='k')
    return ddata


def show_dendrogram(Z):
    fancy_dendrogram(Z, truncate_mode='lastp',
                     p=12,
                     leaf_rotation=90.,
                     leaf_font_size=12.,
                     show_contracted=True,
                     annotate_above=10,  # useful in small plots so annotations don't overlap
                     )
    plt.show()


def show_elbow(Z):
    # showing the elobow diagram
    last = Z[-10:, 2]
    last_rev = last[::-1]
    idxs = np.arange(1, len(last) + 1)
    plt.plot(idxs, last_rev)

    acceleration = np.diff(last, 2)  # 2nd derivative of the distances
    acceleration_rev = acceleration[::-1]
    plt.plot(idxs[:-2] + 1, acceleration_rev)
    plt.show()
    # if idx 0 is the max of this we want 2 clusters
    k = acceleration_rev.argmax() + 2
    print("Recommend clusters from elbow diagram:", k)


def get_clusters(Z, k):
    return sch.fcluster(Z, k, criterion='maxclust')
