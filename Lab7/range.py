class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError("step cannot be 0")
        if stop is None:  # only one argument passed
            start, stop = 0, start
        self._start = start
        self._stop = stop
        self._step = step
        self._length = max(0, (stop - start + (step - 1 if step > 0 else step + 1)) // step)

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        if index < 0:
            index += self._length
        if not 0 <= index < self._length:
            raise IndexError("index out of range")
        return self._start + index * self._step

    def __str__(self):
        return f"Range({self._start}, {self._stop}, {self._step})"
