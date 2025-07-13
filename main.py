from github import Github
from google import genai

github_pat = input("Enter your GitHub PAT: ")
gemini_api_key = input("Enter your Google GenAI API Key: ")
username = input("Enter your GitHub username: ")

# Initialize GitHub and Google GenAI clients
g = Github(github_pat)
client = genai.Client(api_key=gemini_api_key)

while True:
    # Replace with your GitHub_username/repository_name
    repo1 = input(f"{username}, please enter your repository_name: ")
    repo_name = f"{username}/{repo1}"
    print(f"Fetching repository: {repo_name}")

    try:
        repo = g.get_repo(repo_name)
    except Exception as e:
        print(f"Could not fetch repository: {e}")
        continue

    # Get the README content
    try:
        readme = repo.get_readme().decoded_content.decode('utf-8')
        print(f"Successfully retrieved README for {repo.name}")
    except Exception as e:
        print(f"Could not retrieve README: {e}")
        readme = None

    # You can also retrieve other metadata:
    repo_info = {
        "name": repo.name,
        "description": repo.description,
        "stargazers": repo.stargazers_count,
        "topics": repo.get_topics(),
        "readme_content": readme
    }

    # Generating linkedin post using gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        You are an expert technical writer specializing in LinkedIn content. 
        Your task is to generate a professional LinkedIn post announcing a new GitHub project. 

        The post should:
        - Be concise (aim for under 1600 characters).
        - Highlight key features and benefits of the project.
        - Include relevant technical hashtags.
        - Encourage engagement (e.g., asking for feedback or linking to the repo).
        - Use a professional and engaging tone.
        - Be easily copy-paste ready for LinkedIn.
        - please no markdown formatting, just plain text.

        Project Details:{repo_info}
        Readme for the project: {readme}

        Generate the LinkedIn post:
        """
    )

    # Printing the generated LinkedIn post
    print("\nGenerated LinkedIn post:\n")
    print(response.text)
    print("\n" + "-"*60 + "\n")

    again = input("Would you like to generate a post for another repository? (y/n): ").strip().lower()
    if again != 'y':
        print("Exiting.")
        break
