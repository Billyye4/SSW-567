import requests
import json

def getInfo(userID):
    url = f"https://api.github.com/users/{userID}/repos"
    req = requests.get(url)

    if req.status_code != 200:
        return f"Error: {req.status_code}"

    data = req.json()
    repos = []

    for repo in data:
        name = repo['name']
        repo_url = f"https://api.github.com/repos/{userID}/{name}/commits"
        repo_req = requests.get(repo_url)

        if repo_req.status_code == 200:
            commit_count = len((repo_req.json()))
            repos.append(f"Repo: {name} Number of commits: {commit_count}")
    return repos

if __name__ == "__main__":
    info = getInfo("Billyye4")
    print(info)