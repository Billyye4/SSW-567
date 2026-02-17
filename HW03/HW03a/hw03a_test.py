import unittest
from hw03a import getInfo

class TestGitHubInfo(unittest.TestCase):

    def testGetInfo(self):
        result = getInfo("BillyYe1")
        expected = ['Repo: SSW-567 Number of commits: 6']
        self.assertEqual(result, expected)

    def testGetInfoInvalidUser(self):
        result = getInfo("InvalidUser!")
        expected = "Error: 404"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()