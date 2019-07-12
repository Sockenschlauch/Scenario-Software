import openpyxl

path = r"E:\Git\Scenario-Software\SimpleTest_Factors.xlsx"


def read_projections(path):
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    cell_value = sheet
    matrix = []

    i = 0
    for row in sheet.iter_rows():
        matrix.append([])
        for cell in row:
            if cell.value:
                matrix[i].append(cell.value)
        i += 1
    return matrix


def print_projections(matrix):
    for factor in matrix[1:]:
        print(factor[0], end=": ")
        for projection in factor[1:-1]:
            print(projection, end=", ")
        print(factor[-1])


def main():
    print_projections(read_projections(path))


if __name__ == "__main__":
    main()
