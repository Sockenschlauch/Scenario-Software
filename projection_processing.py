def calculate_consistency(matrix, bundle):
    sum = 0
    for colum in range(len(bundle)):
        for row in range(len(bundle)):
            if row < colum:
                pass
            else:
                print()
                sum += matrix[colum][row][bundle[colum]][bundle[row]]

    return sum


def get_projections(projection_list, bundle):
    projections = []
    for i in range(len(bundle)):
        projections.append(projection_list[i][bundle[i]])
    return projections
