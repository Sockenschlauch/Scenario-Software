from consistency_matrix_creation import *
from consistency_matrix_reading import *
from projection_processing import *
from projection_bundle import *
from clustering import *

factors_path = r"E:\Git\Scenario-Software\SimpleTest_Factors.xlsx"
matrix_path = r"E:\Git\Scenario-Software\consistency_matrix_test.xlsx"
keep_n_projections = 1000  # How many projections should be kept for clustering

# projections = read_projections(factors_path)
# print("Creating consistency matrix...")
# write_consistency_matrix(path=factors_path, factor_list=projections)
# print("Consistency matrix created!")

projections = read_projections_from_matrix(matrix_path)
matrix = read_matrix(matrix_path, projections)

print("\nProjections: ", projections)
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

show_dendrogram(Z)
show_elbow(Z)

print(get_clusters(Z, 4))
