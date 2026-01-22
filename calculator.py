import subprocess

# Function to get contributors
def get_contributors(repo_path):
    # Run the git command to get contributors
    result = subprocess.run(
        ["git", "-C", repo_path, "shortlog", "-s", "-n"],
        capture_output=True,
        text=True
    )
    
    # Print contributors
    print(result.stdout)

# Replace with your local repository path
repo_path = "/path/to/your/repo"

# Get and print contributors
get_contributors(repo_path)
