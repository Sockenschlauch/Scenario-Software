from consistency_matrix_creation import *

factors_path = r"E:\Git\Scenario-Software\SimpleTest_Factors.xlsx"

projections = read_projections(factors_path)
print("Creating consistency matrix...")
write_consistency_matrix(path=factors_path, factor_list=projections)
print("Consistency matrix created!")
