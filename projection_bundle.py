class projection_bundle():
    from projection_processing import calculate_consistency

    def __init__(self, bundle):
        self.bundle = bundle
        self.consistency = calculate_consistency(bundle)

    def set_consistency(matrix):
        self.consistency = self.consistency = calculate_consistency(
            matrix=matrix, bundle=bundle)
