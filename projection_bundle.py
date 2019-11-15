from projection_processing import calculate_consistency


class projection_bundle():
    def __init__(self, bundle, matrix):
        self.bundle = bundle
        self.consistency = calculate_consistency(matrix, bundle)


class iterator():
    def __init__(self, projections):
        self._overflow = []
        self._counter = []
        self._n_permutations = self.calculate_permutations(projections)
        self._current_iteration = 1

        # building counter & overflow
        for projection in projections:
            self._overflow.append(len(projection))
            self._counter.append(1)
        # important to start iterations with the first value
        self._counter[0] = 0

    # return the next iteration
    def get_next(self):
        self._counter[0] += 1
        for i in range(len(self._counter)):
            if self._counter[i] > self._overflow[i] and i == len(self._counter)-1:
                return False
            elif self._counter[i] > self._overflow[i]:
                self._counter[i] = 1
                self._counter[i+1] += 1

        # Prints out the progress of the Iterator
        self._current_iteration += 1
        if self._current_iteration*10 % self._n_permutations == 0:
            print("We are at ", self._n_permutations /
                  self._current_iteration, " percent progress!")

        return self._counter

    # returns the current iteration
    def get_counter(self):
        return self._counter

    # Calculating the number of permutations
    def calculate_permutations(self, projections):
        n_permutations = 1
        for factor in projections:
            n_permutations *= len(factor)
        return n_permutations

    # returns the number of permutations
    def get_n_permutations(self):
        return self._n_permutations


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
