# checktype
Decorator for validating type of function arguments and return value.

## Usage:

```python
>>> from checktypes import checktype
>>> @checktype
... def test_func(string: str) -> int:
...     return len(string)
... 
>>> test_func(string=2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/marsohod/projects/python/checktypes/src/checktypes/core.py", line 38, in wrapper
    function.__annotations__[arg_key].__name__
checktypes.core.AnnotationsException: Attribute string must be (str)
>>> test_func(string='asd')
3
>>> @checktype
... def test_func(string):
...     return len(string)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/marsohod/projects/python/checktypes/src/checktypes/core.py", line 19, in checktype
    'for arguments and return value'.format(function.__name__)
checktypes.core.AnnotationsNotExist: Function test_func must provide annotations for arguments and return value
>>> @checktype
... def test_func(string: str) -> int:
...     return string
... 
>>> test_func(string='asd')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/marsohod/projects/python/checktypes/src/checktypes/core.py", line 48, in wrapper
    function.__annotations__['return'].__name__
checktypes.core.AnnotationsException: Function test_func must returns value type (int)
>>> test_func('asd')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/marsohod/projects/python/checktypes/src/checktypes/core.py", line 25, in wrapper
    'Function {0} don`t takes positional arguments'.format(function.__name__)
checktypes.core.AnnotationsException: Function test_func don`t takes positional arguments

```
