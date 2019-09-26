
from sklearn import manifold
from matplotlib import pyplot as plt
import scipy.spatial.distance as ssd


def show_mds(Z, c):

    similarities = ssd.squareform(Z)
    print("\nÄhnlichkeitsmatrix:" + str(len(similarities)) +
          "x" + str(len(similarities)))

    # metric multidimensional scaling
#     mds = manifold.MDS(n_components=2, max_iter=3000, eps=1e-9,
#                        dissimilarity="precomputed", n_jobs=1)

    # non-metric multidiemensional scaling
    mds = manifold.MDS(n_components=2, metric=False, max_iter=30000, eps=1e-15,
                       dissimilarity="precomputed", n_init=10)
    pos = mds.fit_transform(similarities)

    fig, ax = plt.subplots()

    scatter = ax.scatter(pos[:, 0], pos[:, 1], c=c,
                         s=100, lw=0, label='MDS')

    # produce a legend with the unique colors from the scatter
    legend1 = ax.legend(*scatter.legend_elements(),
                        loc="lower left", title="Classes")
    ax.add_artist(legend1)

    # # Points with numbers
    # for i in range(len(pos)):
    #     ax.annotate(i, (pos[i, 0], pos[i, 1]))

    plt.show()
