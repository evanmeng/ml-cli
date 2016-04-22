#! /usr/bin/env python3


from dataset import load_dataset, DataSet
import shlex
from filters import create_filter_func


class MLSession:
    def __init__(self, data_path):
        self.history = []
        self.full_ds = load_dataset(data_path)
        self.it = self.full_ds

    def str_it(self):
        return self.it.items()

    def reset(self):
        self.history.clear()
        self.it = self.full_ds

    def filter(self, line):
        tokens = shlex.split(line)
        if len(tokens) < 2:
            raise ValueError("A filter needs at least a field and a verb.")
        field, verb, *rest = tokens
        field = field.lower()
        verb = verb.lower()
        try:
            filter_f = create_filter_func(field, verb, rest)
        except Exception as ex:
            print("error when applying filter: %s" % ex)
            return
        new_mvs = [m for m in self.it.movies if filter_f(m)]
        new_ds = DataSet(new_mvs)
        self.history.append(new_ds)
        self.it = new_ds

    def back(self):
        if self.history:
            self.history.pop()
            if self.history:
                self.it = self.history[-1]
            else:
                self.it = self.full_ds

    def stack(self):
        lines = ["%3d: %s" % (0, self.full_ds)]
        rest_lines = ["%3d: %s" % (i + 1, ds)
                      for i, ds in enumerate(self.history)]
        lines.extend(rest_lines)
        return '\n'.join(lines)
