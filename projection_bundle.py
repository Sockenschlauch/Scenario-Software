class projection_bundle():
    from projection_processing import calculate_consistency

    def __init__(self, bundle):
        self.bundle = bundle
        self.consistency = calculate_consistency(bundle)

    def set_consistency(matrix):
        self.consistency = self.consistency = calculate_consistency(
            matrix=matrix, bundle=bundle)


class iterator():
    _overflow = []
    _counter = []

    def __init__(self, projections):

        for projection in projections:
            _overflow.append(len(projection))
            _counter.append(1)

    def get_next():
        _counter[0] += 1
        for i in range(len(_counter)):
            if _counter[i] > _overflow[i] and i == len(_counter):
                return False
            elif _counter[i] > _overflow[i]:
                _counter[i] = 1
                _counter[i+1] += 1
        return _counter

    def get_counter():
        return _counter
