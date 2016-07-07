import unittest

from checktypes import checktype, AnnotationsException, AnnotationsNotExist


class TestChecktype(unittest.TestCase):
    def test_function_without_annotations(self):
        with self.assertRaises(AnnotationsNotExist):
            @checktype
            def test_func(string):
                return len(string)

    def test_pass_positional_arguments(self):
        @checktype
        def test_func(string: str) -> int:
            return len(string)

        with self.assertRaises(AnnotationsException) as err:
            test_func('text')

        self.assertEqual(
            str(err.exception),
            'Function {0} don`t takes positional arguments'.format(test_func.__name__)
        )

    def test_pass_arg_with_wrong_type(self):
        @checktype
        def test_func(string: str) -> int:
            return len(string)

        with self.assertRaises(AnnotationsException) as err:
            test_func(string=2)

        self.assertEqual(
            str(err.exception),
            'Attribute {0} must be ({1})'.format(
                'string',
                test_func.__annotations__['string'].__name__
            )
        )

    def test_wrong_return_type(self):
        @checktype
        def test_func(string: str) -> int:
            return string

        with self.assertRaises(AnnotationsException) as err:
            test_func(string='asd')

        self.assertEqual(
            str(err.exception),
            'Function {0} must returns value type ({1})'.format(
                test_func.__name__,
                test_func.__annotations__['return'].__name__
            )
        )

if __name__ == '__main__':
    unittest.main()
