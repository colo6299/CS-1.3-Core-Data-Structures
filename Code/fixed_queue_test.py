from arq import FixedQ
import unittest

class FixedQueueTest(unittest.TestCase):
    
    def test_buffer(self): # that's all, folks
        f = FixedQ(4, [1, 2, 3, 4])
        assert f.ndqueue(5) == 1
        assert f.items() == [2, 3, 4, 5]

        f = FixedQ(4, [1, 2, 3, 4])
        f.ndqueue(5)
        f.ndqueue(5)
        f.ndqueue(5)
        f.ndqueue(5)
        f.ndqueue(5)
        f.ndqueue(5)
        f.ndqueue(5)
        f.ndqueue(5)
        f.ndqueue(5)
        f.ndqueue(5)
        f.ndqueue(5)
        f.ndqueue(5)
        f.ndqueue(5)
        f.ndqueue(5)
        f.ndqueue(5)

        assert f.items() == [5, 5, 5, 5]