import unittest
from vanhack.shortest_job_first import sjf

class Test(unittest.TestCase):
    def test_should_handle_the_example(self):
        self.assertEqual(sjf([3,10,20,1,2],0), 6)
        self.assertEqual(sjf([3,10,10,20,1,2],2), 26)
        self.assertEqual(sjf([10,10,10,10],3), 40)