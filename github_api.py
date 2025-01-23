import requests


class GitHubAPI:
    def __init__(self, token, owner, repo):
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json"
        }
        self.base_url = f"https://api.github.com/repos/{owner}/{repo}"

    def get_repo_info(self):
        url = self.base_url
        response = requests.get(url, headers=self.headers)
        return response.json() if response.status_code == 200 else None

    def get_issues(self, state="open", per_page=100):
        url = f"{self.base_url}/issues"
        params = {"state": state, "per_page": per_page}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json() if response.status_code == 200 else None

    def get_collaborators(self, per_page=100):
        url = f"{self.base_url}/collaborators"
        params = {"per_page": per_page}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json() if response.status_code == 200 else None

    def get_branches(self):
        url = f"{self.base_url}/branches"
        response = requests.get(url, headers=self.headers)
        return response.json() if response.status_code == 200 else None

    def get_commits(self, per_page=100):
        url = f"{self.base_url}/commits"
        params = {"per_page": per_page}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json() if response.status_code == 200 else None