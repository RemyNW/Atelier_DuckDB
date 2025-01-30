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
    
    def get_contributors(self):
        url = f"{self.base_url}/contributors"
        all_contributors = []
        page = 1
        while True:
            params = {"per_page": 100, "page": page}
            response = requests.get(url, headers=self.headers, params=params)
            if response.status_code == 200:
                contributors = response.json()
                all_contributors.extend(contributors)
                if len(contributors) < 100:
                    break
                page += 1
            else:
                print(f"Error: {response.status_code}")
                break
        return all_contributors
    
    def get_branches(self):
        url = f"{self.base_url}/branches"
        all_branches = []
        page = 1
        while True:
            params = {"per_page": 100, "page": page}
            response = requests.get(url, headers=self.headers, params=params)
            if response.status_code == 200:
                branches = response.json()
                all_branches.extend(branches)
                if len(branches) < 100:
                    break
                page += 1
            else:
                print(f"Error: {response.status_code}")
                break
        return all_branches

    def get_commits(self):
        url = f"{self.base_url}/commits"
        all_commits = []
        page = 1
        while True:
            params = {
                "per_page": 100,
                "page": page,
                "since": "2024-01-01T00:00:00Z",
                }
            response = requests.get(url, headers=self.headers, params=params)
            if response.status_code == 200:
                commits = response.json()
                all_commits.extend(commits)
                if len(commits) < 100:
                    break
                page += 1
            else:
                print(f"Error: {response.status_code}")
                break
        return all_commits
