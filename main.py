import os
from dotenv import load_dotenv
from utils import save_to_parquet
from github_api import GitHubAPI

# Charger les variables d'environnement depuis .env
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = "microsoft"
REPO_NAME = "vscode"

# Définir le répertoire où les fichiers Parquet seront enregistrés
PARQUET_DIRECTORY = "parquet_directory"
# PARQUET_DIRECTORY = os.path.join(BASE_DIRECTORY, "parquet_directory")

# Créer le répertoire automatiquement s'il n'existe pas
os.makedirs(PARQUET_DIRECTORY, exist_ok=True)

if __name__ == "__main__":
    if not GITHUB_TOKEN:
        raise ValueError("Le token GitHub n'est pas défini dans les variables d'environnement.")

    # Initialiser l'API GitHub
    github = GitHubAPI(token=GITHUB_TOKEN, owner=REPO_OWNER, repo=REPO_NAME)

    # Récupérer les données et les sauvegarder dans des fichiers Parquet
    repo_info = github.get_repo_info()
    if repo_info:
        save_to_parquet(repo_info, os.path.join(PARQUET_DIRECTORY, "repo_info.parquet"))

    issues = github.get_issues()
    if issues:
        save_to_parquet(issues, os.path.join(PARQUET_DIRECTORY, "issues.parquet"))

    collaborators = github.get_collaborators()
    if collaborators:
        save_to_parquet(collaborators, os.path.join(PARQUET_DIRECTORY, "collaborators.parquet"))

    branches = github.get_branches()
    if branches:
        save_to_parquet(branches, os.path.join(PARQUET_DIRECTORY, "branches.parquet"))

    commits = github.get_commits()
    if commits:
        save_to_parquet(commits, os.path.join(PARQUET_DIRECTORY, "commits.parquet"))