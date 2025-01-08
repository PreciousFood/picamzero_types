from typing import Optional

class PicameraZeroException(Exception):
    """
    Base class for exceptions thrown by the picamera-zero
    library.
    """

    def __init__(self, message: str, hint: Optional[str] = None, *args) -> None:
        """
        :param str message - The reason for the exception.
        :param Optional[str] hint - An optional hint to resolve the exception.
        """

    def _format_exception(self) -> str:
        """
        This function is called to 'render' the exception
        """

    def __str__(self) -> str: ...

def override_sys_except_hook():
    """
    When called, this function overrides the default
    sys.except hook to control how exceptions are formatted to the
    user. It could be used, for example, to control how much of
    the stack trace is shown to the library user - beginner
    beginner programmers may find a full stack trace quite
    intimidating.

    This would be called either in picamera-zero's __init__.py or when
    instantiating picamera-zero's Camera object:

    """