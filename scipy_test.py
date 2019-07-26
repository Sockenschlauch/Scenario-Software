# needed imports
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import scipy.cluster.hierarchy as sch
import numpy as np

bundle2 = [2, 2, 3]
bundle1 = [1, 1, 3]
bundle3 = [1, 2, 1]
bundle4 = [1, 1, 1]
bundles = np.array([bundle1, bundle2, bundle3, bundle4])

# generate two clusters: a with 100 points, b with 50:
# np.random.seed(4711)  # for repeatability of this tutorial
# a = np.random.multivariate_normal([10, 0], [[3, 1], [1, 4]], size=[100, ])
# b = np.random.multivariate_normal([0, 20], [[3, 1], [1, 4]], size=[50, ])
# X = np.concatenate((a, b),)
# print(X.shape)  # 150 samples with 2 dimensions
# plt.scatter(X[:, 0], X[:, 1])
# plt.show()

# generate the linkage matrix
# custom metric: 0 if same, 1 if different
print(bundles)
d = sch.distance.pdist(bundles, 'hamming')
Z = linkage(d, 'average')

# Plotting the dendrogram more fancy


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


# calculate full dendrogram
fancy_dendrogram(
    Z,
    truncate_mode='lastp',
    p=12,
    leaf_rotation=90.,
    leaf_font_size=12.,
    show_contracted=True,
    annotate_above=10,  # useful in small plots so annotations don't overlap
)
plt.show()


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
print("clusters:", k)
