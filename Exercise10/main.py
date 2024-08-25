import requests

response = requests.get("https://api.github.com/users/SolangeBV/repos")
my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['html_url']}\n")
