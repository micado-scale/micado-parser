"""Exceptions for the MiCADO Parser"""

class ValidationError(Exception):
    """Base error for validation"""


class MultiError(ValidationError):
    """Errors occured during validation..."""

    def __init__(self, error_set, msg=None):
        super().__init__()
        msg = msg if msg else ""
        self.msg = "\n--{}--".format(msg)
        for error in error_set:
            self.msg += "\n  {}".format(error)
        self.msg += "\n----{}".format("-" * len(msg))

    def __str__(self):
        """Overload __str__ to return msg when printing/logging"""
        return self.msg

