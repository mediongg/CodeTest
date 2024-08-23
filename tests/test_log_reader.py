

from log_reader import LogReader
import unittest
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

class TestLogReader(unittest.TestCase):
    LogReader.LogFolder = '{}/logs/'.format(dir_path)

    def test_exceptions(self):
        logReader = LogReader('i_dont_exist')
        with self.assertRaises(FileNotFoundError):
            logReader.read_log(5, 'blah')

        logReader = LogReader('i_am_dir')
        with self.assertRaises(IsADirectoryError):
            logReader.read_log(5, 'blah')

    def test_read_log(self):
        logReader = LogReader('log')

        res = logReader.read_log(5, '')
        expected = [
            '10. u1234',
            '9. y1234',
            '8. z1234',
            '7. g1234',
            '6. f1234',
        ]

        self.assertListEqual(res, expected)


        # test read log entries greater than the total line of log contents
        res = logReader.read_log(15, '')

        expected = [
            '10. u1234',
            '9. y1234',
            '8. z1234',
            '7. g1234',
            '6. f1234',
            '5. e1234',
            '4. f1234',
            '3. c1234',
            '2. b1234',
            '1. a1234',
        ]

        self.assertListEqual(res, expected)


        # test filter
        res = logReader.read_log(10, 'f1234')

        expected = [
            '6. f1234',
            '4. f1234',
        ]

        self.assertListEqual(res, expected)

