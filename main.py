from github import Github
from google import genai

# Initialize GitHub and Google GenAI clients
g = Github('YOUR_GITHUB_ACCESS_TOKEN')
client = genai.Client(api_key="YOUR_GOOGLE_GENAI_API_KEY")

# Replace with your GitHub_username/repository_name
repo_name = "juto-shogan/adidas-Analysis"
repo = g.get_repo(repo_name)

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

# Generating linkedin post using using gemini
response = client.models.generate_content(
    model="gemini-2.5-flash", 
    # The prompt for generating the LinkedIn post
    # this is justa template, you can modify it as needed
    contents=f"""
    You are an expert technical writer specializing in LinkedIn content. 
    Your task is to generate a professional LinkedIn post announcing a new GitHub project. 

    The post should:
    - Be concise (aim for under 1600 characters).
    - Highlight key features and benefits of the project.
    - Include relevant technical hashtags.
    - Encourage engagement (e.g., asking for feedback or linking to the repo).

    Project Details:{repo_info}
    Readme for the project: {readme}

    Generate the LinkedIn post:
    """
)

# Printing the generated LinkedIn post
print(response.text)