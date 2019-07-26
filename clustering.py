import scipy
import scipy.cluster.hierarchy as sch
from math import sqrt


def calculate_distance(bundle1, bundle2):
    distance = 0
    for i in range(len(bundle1)):
        sum = 0
        for j in range(len(len(bundle1[i]))):
            sum += (bundle1[i][j]-bundle2[i][j])**2
        distance += sqrt(sum)
    return distance


def create_distance_matrix(bundles):
    pass
