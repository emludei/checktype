#!/usr/bin/env python3


__all__ = ['checktype']


class AnnotationsException(Exception):
    pass


class AnnotationsNotExist(AnnotationsException):
    pass


def checktype(function):
    if not function.__annotations__:
        raise AnnotationsNotExist(
            'Function {0} must provide annotations '
            'for arguments and return value'.format(function.__name__)
        )

    def wrapper(*args, **kwargs):
        if args:
            raise AnnotationsException(
                'Function {0} does not take positional arguments'.format(function.__name__)
            )

        for arg_key in kwargs:
            if arg_key not in function.__annotations__:
                raise AnnotationsException(
                    'Function {0} does not provide arg {1}'.format(function.__name__, arg_key)
                )

            if not isinstance(kwargs[arg_key], function.__annotations__[arg_key]):
                raise AnnotationsException(
                    'Attribute {0} must be ({1})'.format(
                        arg_key,
                        function.__annotations__[arg_key].__name__
                    )
                )

        result = function(**kwargs)

        if not isinstance(result, function.__annotations__['return']):
            raise AnnotationsException(
                'Function {0} must returns value type ({1})'.format(
                    function.__name__,
                    function.__annotations__['return'].__name__
                )
            )

        return result

    wrapper.__name__ = function.__name__
    wrapper.__doc__ = function.__doc__
    wrapper.__annotations__ = function.__annotations__

    return wrapper
