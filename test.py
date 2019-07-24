from consistency_matrix_creation import *
from consistency_matrix_reading import *
from projection_processing import *
from projection_bundle import *

factors_path = r"E:\Git\Scenario-Software\SimpleTest_Factors.xlsx"
matrix_path = r"E:\Git\Scenario-Software\consistency_matrix_test.xlsx"

bundle = [1, 1, 1]

# projections = read_projections(factors_path)
# print("Creating consistency matrix...")
# write_consistency_matrix(path=factors_path, factor_list=projections)
# print("Consistency matrix created!")

projections = read_projections_from_matrix(matrix_path)
matrix = read_matrix(matrix_path, projections)

print("Iterations: ")
iter = iterator(projections)
while iter.get_next():
    bundle = iter.get_counter()
    print(get_projections(projections, bundle))


bundle = [1, 1, 1]
print("\nProjections: ", projections)
print("\nMatrix: ", matrix)
print("\nBundle: ", bundle)
print("\nget Projections: ", get_projections(projections, bundle))
print("\nConsistency: ", calculate_consistency(matrix, bundle))
