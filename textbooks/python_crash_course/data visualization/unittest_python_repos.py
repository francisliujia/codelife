import unittest

import python_repos as pr

class PythonReposTestCase(unittest.TestCase):
    '''tests for python_repos.py'''

    def setUp(self):
        '''call all the functuons here, and test elements seperately'''
        self.r = pr.get_response()
        self.repo_dicts = pr.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.repo_links, self.stars, self.labels, self.repo_names = pr.get_project_data(
            self.repo_dicts)

    def test_get_response(self):
        '''test that we get a valid response'''
        self.assertEqual(self.r.status_code, 200)

    def test_repo_dicts(self):
        '''test we're getting the data we think we are'''
        # we should get the dics for 30 respositories
        self.assertEqual(len(self.repo_dicts), 30)

        # repositories should have required keys.
        required_keys = ['name', 'owner', 'stargazes-count', 'html_url']
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())


if __name__ == '__main__':
    unittest.main()