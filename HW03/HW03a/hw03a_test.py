import unittest
from hw03a import getInfo

class TestGitHubInfo(unittest.TestCase):

    def testGetInfo(self):
        result = getInfo("Billyye4")
        expected = ["Repo: aaa-refactor-tool-python- Number of commits: 5", "Repo: SSW-567 Number of commits: 11"]
        self.assertEqual(result, expected)

    def testGetInfoInvalidUser(self):
        result = getInfo("InvalidUser!")
        expected = "Error: 404"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()