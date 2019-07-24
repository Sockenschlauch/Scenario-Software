def calculate_consistency(matrix, bundle):
    sum = 0
    for colum in range(len(bundle)):
        for row in range(len(bundle)):
            if row <= colum:
                pass
            else:
                print("Colum: ", colum, "\tRow: ", row, "\tValue: ",
                      matrix[colum][row][bundle[colum]-1][bundle[row]-1])
                sum += matrix[colum][row][bundle[colum]-1][bundle[row]-1]

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


def iterate_permuations(projections):
    permutations = []
    for projection in projections:
        permutations.append(1)

    return permutations
