from consistency_matrix_creation import *
from easygui import *

# factors_path = r"E:\Git\Scenario-Software\Factorlist.xlsx"

factors_path = fileopenbox(msg='Choose the list of factors and projections!',
                           title='Creating consistency matrix', default="*\SimpleTest_Factors.xlsx", filetypes=["*.xlsx"])

projections = read_projections(factors_path)
print("Creating consistency matrix...")

consistency_matrix_path = filesavebox(msg='Pick a place to save the Consistencymatrix!',
                                      title='Save matrix', default="*\\consistency_matrix.xlsx", filetypes=["*.xlsx"])
write_consistency_matrix(path=consistency_matrix_path, factor_list=projections)
print("Consistency matrix created!")
