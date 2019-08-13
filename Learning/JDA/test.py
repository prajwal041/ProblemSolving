import unittest
import Jda_assignment
import sys
import time

class MyTestCase(unittest.TestCase):
    def test_args(self):            # testing arguments
        url, filename = Jda_assignment.download_jpg('http://mywebserver.com/images/271947.jpg', 'save_file',0, 'args')
        testurl = url[-3:]
        self.assertEqual(testurl, 'jpg')

    def test_file(self):            # testing input file format
        testfiles = Jda_assignment.file
        testfile = testfiles[-3:]
        self.assertEqual(testfile, 'txt')

    def test_time(self):            # verifying the runtime complexity should not exceed 3 seconds
        start_time = time.time()
        Jda_assignment.download_jpg('http://mywebserver.com/images/271947.jpg', 'save_file', 0, 'args')
        self.assertLessEqual(time.time()-start_time, 3.0)

    def test_text_file_count(self):     # No of lines should be greater than 0
        self.assertGreaterEqual(len(Jda_assignment.lines),0)

    def test_error_count(self):         # Error count after 10th line
        self.assertLessEqual(Jda_assignment.count,10)

if __name__ == '__main__':
    unittest.main(argv=[sys.argv[1]])
