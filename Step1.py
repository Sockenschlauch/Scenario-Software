from consistency_matrix_creation import *
from easygui import *

factors_path = r"E:\Git\Scenario-Software\SimpleTest_Factors.xlsx"

factors_path = fileopenbox(msg='Choose the list of factors and projections!',
                           title='Creating consistency matrix', default="*\SimpleTest_Factors.xlsx", filetypes=["*.xlsx"])

projections = read_projections(factors_path)
print("Creating consistency matrix...")
write_consistency_matrix(path=factors_path, factor_list=projections)
print("Consistency matrix created!")
