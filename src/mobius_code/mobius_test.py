import ctypes
import os
import unittest


dldlib = ctypes.CDLL(os.path.abspath('mobius.so'))
dldmobius = dldlib.mobius
dldmobius.argtypes = [ctypes.c_longlong]


class TestMobius(unittest.TestCase):
    def test_mobius_small(self):
        self.assertEqual(dldmobius(0), 0)

        self.assertEqual(dldmobius(1), 1)

        self.assertEqual(dldmobius(2), -1)
        self.assertEqual(dldmobius(3), -1)
        self.assertEqual(dldmobius(5), -1)
        self.assertEqual(dldmobius(7), -1)

        self.assertEqual(dldmobius(4), 0)
        self.assertEqual(dldmobius(9), 0)

        self.assertEqual(dldmobius(6), 1)
        self.assertEqual(dldmobius(10), 1)

    def test_mobius_large(self):
        self.assertEqual(dldmobius(7*11*13), -1)
        self.assertEqual(dldmobius(2*3*5*7*11), -1)
        self.assertEqual(dldmobius(2*3*5*7*11*11), 0)
        self.assertEqual(dldmobius(2*3*5*7*11*13), 1)
