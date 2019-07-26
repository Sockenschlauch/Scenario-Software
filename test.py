from consistency_matrix_creation import *
from consistency_matrix_reading import *
from projection_processing import *
from projection_bundle import *

factors_path = r"E:\Git\Scenario-Software\SimpleTest_Factors.xlsx"
matrix_path = r"E:\Git\Scenario-Software\consistency_matrix_test.xlsx"
keep_n_projections = 4  # How many projections should be kept for clustering

# projections = read_projections(factors_path)
# print("Creating consistency matrix...")
# write_consistency_matrix(path=factors_path, factor_list=projections)
# print("Consistency matrix created!")

projections = read_projections_from_matrix(matrix_path)
matrix = read_matrix(matrix_path, projections)

print("\nProjections: ", projections)
print("\nMatrix: ", matrix)

print("Iterations: ")
iter = iterator(projections)

bundles = []
while iter.get_next():
    bundle = iter.get_counter()
    bundles.append(projection_bundle(bundle, matrix))
    bundles.sort(key=lambda x: x.consistency, reverse=True)

    if len(bundles) > keep_n_projections:
        bundles.pop()

for object in bundles:
    print("Projection: ", object.bundle,
          "\tConsistency: ", object.consistency)

print("#Iterations: ", iter.get_n_permutations())
