import unittest
from unittest.mock import patch, Mock
from hw03a import getInfo

class TestGitHubInfo(unittest.TestCase):

    @patch('hw03a.requests.get')
    def testGetInfo(self, mock_GetInfo):
        # Mock the response for the user's repositories
        mock_RepoResponse = Mock()
        mock_RepoResponse.status_code = 200
        mock_RepoResponse.json.return_value = [{'name': 'SSW-567'}]

        # Mock the response for the commits in the repository
        mock_CommitsResponse = Mock()
        mock_CommitsResponse.status_code = 200
        mock_CommitsResponse.json.return_value = [1] * 6  # Simulating 6 commits

        # Set the side effects for the mock
        mock_GetInfo.side_effect = [mock_RepoResponse, mock_CommitsResponse]
        result = getInfo("BillyYe1")
        expected = ['Repo: SSW-567 Number of commits: 6']
        self.assertEqual(result, expected)

    @patch('hw03a.requests.get')
    def testGetInfoInvalidUser(self, mock_GetInfo):
        mock_InvalidResponse = Mock()
        mock_InvalidResponse.status_code = 404
        mock_GetInfo.return_value = mock_InvalidResponse
        #Side effect not required here since we are only testing one call to requests.get

        result = getInfo("InvalidUser!")
        expected = "Error: 404"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()