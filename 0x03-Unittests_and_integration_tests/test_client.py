#!/usr/bin/env python3
"""
GithubOrgClient module
"""

import requests
from typing import List

class GithubOrgClient:
    """GithubOrgClient class to interact with GitHub API"""

    def __init__(self, org_name: str):
        self.org_name = org_name

    @property
    def _public_repos_url(self) -> str:
        """Return the URL for the public repositories of the organization"""
        return f"https://api.github.com/orgs/{self.org_name}/repos"

    def public_repos(self, license: str = None) -> List[str]:
        """Return the list of public repositories"""
        repos = requests.get(self._public_repos_url).json()
        if license:
            repos = [repo for repo in repos if repo.get('license', {}).get('key') == license]
        return [repo['name'] for repo in repos]
