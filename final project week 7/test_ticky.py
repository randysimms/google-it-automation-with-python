import unittest


class MyTestCase(unittest.TestCase):

    def test_foundfile(self):
        self.assertRaises(self, FileNotFoundError, "doesnotexist.log")

    def test_syslogmsg(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
