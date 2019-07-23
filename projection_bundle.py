class projection_bundle():
    from projection_processing import calculate_consistency

    def __init__(self, projections):
        self.projections = projections
        self.consistency = calculate_consistency(projections)

    def set_consistency(matrix):
        self.consistency = self.consistency = calculate_consistency(
            matrix=matrix, projections=projections)
