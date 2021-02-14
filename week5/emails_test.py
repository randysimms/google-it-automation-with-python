
#!/usr/bin/env python3
import unittest

from week5_emails import find_email


class EmailsTest(unittest.TestCase):
    def test_basic(self):
        testcase = [None, "Bree", "Campbell"]
        expected = "breee@utnisia.net"
        self.assertEqual(expected,find_email(testcase))

    def test_one_name(self):
        testcase = [None, "John"]
        expected = "Missing parameters"
        self.assertEqual(expected,find_email(testcase))

    def test_two_name(self):
        testcase = [None, "Roy", "Cooper"]
        expected = "No email address found"
        self.assertEqual(expected,find_email(testcase))

    if __name__ == '__main__':
        unittest.main()
