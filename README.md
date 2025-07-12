
# LinkedIn Post Bot

This project, named `linkedin-post-bot`, is a Python application designed to automate the process of generating professional LinkedIn posts for new GitHub projects. It leverages the GitHub API to fetch project details and the Google Gemini API (Gemini 2.5 Flash) to generate engaging, concise, and relevant social media content based on the repository's information.

## Overview

The `linkedin-post-bot` simplifies announcing new software projects on LinkedIn. By utilizing AI, it reads the project's README and repository metadata, then crafts a compelling LinkedIn post tailored for technical audiences, complete with relevant hashtags.

## Features

* **GitHub Integration:** Fetches repository details, including the README, description, topics, and stargazers count, using the PyGithub library.
* **AI-Powered Content Generation:** Uses the Google Gemini API (specifically `gemini-2.5-flash`) to analyze project information and generate a professional LinkedIn post.
* **Concise and Engaging Output:** Generates posts designed to highlight key features, encourage engagement, and include appropriate technical hashtags.
* **Customizable Targets:** Easily configured to generate posts for different GitHub repositories.

## Requirements

The project requires Python 3.x and the dependencies listed in `requirements.txt`.

## Setup and Installation

To get started, you will need API access for both GitHub and Google GenAI.

1. **Clone the repository:**
   **Bash**

   ```
   git clone https://github.com/juto-shogan/linkedin-post-bot.git
   cd linkedin-post-bot
   ```

   *(Note: Replace `linkedin-post-bot` with your repository name if it differs.)*
2. **Set up a Python virtual environment (recommended):**
   **Bash**

   ```
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   **Bash**

   ```
   pip install -r requirements.txt
   ```
4. Configure API Keys:
   You must obtain API keys and update the main.py script:

   * **GitHub Personal Access Token:** Create one on GitHub (Settings > Developer settings > Personal access tokens). Ensure it has read access to the repository data.
   * **Google GenAI API Key:** Obtain an API key for Google's Generative AI services.

   Open `main.py` and replace the placeholder values:
   **Python**

   ```
   # Initialize GitHub and Google GenAI clients
   g = Github('YOUR_GITHUB_ACCESS_TOKEN')
   client = genai.Client(api_key="YOUR_GOOGLE_GENAI_API_KEY")

   # Replace with your GitHub username/repository name
   repo_name = "juto-shogan/adidas-Analysis" # Update this to the target repository
   ```

## Usage

Once configured, run the `main.py` script:

**Bash**

```
python main.py
```

The script will retrieve the repository data, generate a LinkedIn post, and print the generated content to the console.

## How It Works

The bot performs the following steps:

1. **Initialization:** Connects to GitHub and Google GenAI using the provided API keys.
2. **Data Retrieval:** Accesses the specified GitHub repository and retrieves essential information (README, description, topics, etc.).
3. **AI Generation:** Sends the project details to the Gemini 2.5 Flash model with a prompt designed for technical LinkedIn content.
4. **Output:** Prints the AI-generated LinkedIn post, ready for review and posting.

## Author

**Somto Mbonu**

* GitHub: [juto-shogan
  ](https://www.google.com/search?q=https://github.com/juto-shogan)
