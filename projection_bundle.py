class projection_bundle():
    from projection_processing import calculate_consistency

    def __init__(self, bundle):
        self.bundle = bundle
        self.consistency = calculate_consistency(bundle)

    def set_consistency(matrix):
        self.consistency = self.consistency = calculate_consistency(
            matrix=matrix, bundle=bundle)


class iterator():

    def __init__(self, projections):
        self._overflow = []
        self._counter = []

        for projection in projections:
            self._overflow.append(len(projection))
            self._counter.append(1)
        # important to start iterations with the first value
        self._counter[0] = 0

    def get_next(self):
        self._counter[0] += 1
        for i in range(len(self._counter)):
            if self._counter[i] > self._overflow[i] and i == len(self._counter)-1:
                return False
            elif self._counter[i] > self._overflow[i]:
                self._counter[i] = 1
                self._counter[i+1] += 1
        return self._counter

    def get_counter(self):
        return self._counter


# Making the Iterator iteratable


    def __iter__(self):
        return self

    def __next__(self):
        self._counter[0] += 1
        for i in range(len(self._counter)):
            if self._counter[i] > self._overflow[i] and i == len(self._counter):
                return False
            elif self._counter[i] > self._overflow[i]:
                self._counter[i] = 1
                self._counter[i+1] += 1
        return self._counter
