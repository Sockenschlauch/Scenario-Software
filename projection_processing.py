def calculate_consistency(matrix, bundle):
    sum = 0
    for colum in range(len(bundle)):
        for row in range(len(bundle)):
            if row <= colum:
                pass
            else:
                # Only for checking how value is calulated
                # print("Colum: ", colum, "\tRow: ", row, "\tValue: ", matrix[colum][row][bundle[colum]-1][bundle[row]-1])
                value = matrix[colum][row][bundle[colum]-1][bundle[row]-1]

                # Here is decided, at which level of part-inconsistency a bundle is omited
                if value == 0:
                    return False
                sum += value

    return sum


def get_projections(projection_list, bundle):
    projections = []
    for i in range(len(projection_list)):
        projections.append(projection_list[i][bundle[i]-1])
    return projections


def calculate_permutations(projections):
    n_permutations = 1
    for factor in projections:
        n_permutations *= len(factor)
    return n_permutations
