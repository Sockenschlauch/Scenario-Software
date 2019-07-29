from consistency_matrix_reading import *
from projection_processing import *
from projection_bundle import *
from clustering import *
from cluster_writing import write_clusters


matrix_path = r"E:\Git\Scenario-Software\consistency_matrix_test.xlsx"
keep_n_projections = 1000  # How many projections should be kept for clustering

projections = read_projections_from_matrix(matrix_path)
matrix = read_matrix(matrix_path, projections)
factors = read_factors_from_matrix(matrix_path)

print("\nFactors: \t", factors)
print("Projections: ", projections)
print("Matrix: ", matrix)

print("\n-------- Starting Iterations ---------\n")


iter = iterator(projections)

print("#Iterations: ", iter.get_n_permutations())

bundles = []
while iter.get_next():
    bundle = iter.get_counter()
    bundles.append(projection_bundle(list(iter.get_counter()), matrix))
    bundles.sort(key=lambda x: x.consistency, reverse=True)

    if len(bundles) > keep_n_projections:
        del bundles[keep_n_projections]

for object in bundles:
    print("Projection: ", object.bundle,
          "\tConsistency: ", object.consistency)


print("\n-------- Starting Clustering ---------\n")

Z = create_distance_matrix(bundles)

# show_dendrogram(Z)
# show_elbow(Z)

n = int(input("How many clusters are there? "))

cluster_array = get_clusters(Z, n)

# creating a list of clusters
cluster_list = []
for i in range(n):
    cluster_list.append(cluster(i+1, projections))

# sorting the projection bundles in the cluster in the cluster list
for i in range(len(cluster_array)):
    cluster_list[cluster_array[i]-1].add_bundle(bundles[i].bundle)

for i in range(n):
    print(cluster_list[i].get_mixture())

write_clusters(factors, projections, cluster_list)
