from abc import ABCMeta


class ApplicationException(Exception, metaclass=ABCMeta):
    """Base Exception"""

    @property
    def message(self) -> str:
        return 'An application error occurred'

