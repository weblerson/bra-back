import re


class Validator:
    @staticmethod
    def blank_inputs(*args):
        return all(map(lambda x: x.strip(), *args))
