# LinkedIn Post Bot

This project is a Python application designed to automate the process of generating professional LinkedIn posts for new GitHub projects. It leverages the GitHub API to fetch project details and the Google Generative AI API (Gemini 2.5 Flash) to create engaging, concise, and relevant social media content based on the repository's information.

## Overview

The `linked-post-bot` simplifies the task of announcing new software projects on LinkedIn. By utilizing AI, it reads the project's README and repository metadata, then crafts a compelling LinkedIn post tailored for a technical audience, complete with relevant hashtags.

## Features

  * **GitHub Integration:** Fetches repository details, including the README, description, topics, and stargazers count, using the `PyGithub` library.
  * **AI-Powered Content Generation:** Uses the Google Generative AI API (specifically `gemini-2.5-flash`) to analyze project information and generate a professional LinkedIn post.
  * **Concise and Engaging Output:** Generates posts designed to highlight key features, encourage engagement, and include appropriate technical hashtags.
  * **Dynamic User Input:** Prompts the user for API keys and the target GitHub repository at runtime, eliminating the need to edit the script directly.

## Requirements

The project requires Python 3.x and the dependencies listed in `requirements.txt`.

## Setup and Installation

To get started, you will need API access for both GitHub and Google Generative AI.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/juto-shogan/linked-post-bot.git
    cd linked-post-bot
    ```

    *(Note: Replace `juto-shogan/linked-post-bot.git` with your actual repository URL if it differs.)*

2.  **Set up a Python virtual environment (recommended):**

    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Obtain API Keys:**

      * **GitHub Personal Access Token:** Create one on GitHub (Settings \> Developer settings \> Personal access tokens). Ensure it has read access to the repository data.
      * **Google Generative AI API Key:** Obtain an API key for Google's Generative AI services.

## Usage

Once dependencies are installed, run the `main.py` script from your terminal:

```bash
python main.py
```

The script will prompt you to enter your GitHub Personal Access Token, Google Generative AI API key, and the target GitHub repository name (e.g., `juto-shogan/adidas-Analysis`). It will then retrieve the repository data, generate a LinkedIn post, and print the generated content to the console.

## How It Works

The bot performs the following steps:

1.  **User Input:** Prompts the user for necessary credentials and the target repository.
2.  **Initialization:** Connects to GitHub and Google Generative AI using the user-provided API keys.
3.  **Data Retrieval:** Accesses the specified GitHub repository and retrieves essential information (README, description, topics, etc.).
4.  **AI Generation:** Sends the project details to the Gemini 2.5 Flash model with a prompt designed for technical LinkedIn content.
5.  **Output:** Prints the AI-generated LinkedIn post to the terminal, ready for review and posting.

## Author

**Somto Mbonu**

  * GitHub: [juto-shogan](https://github.com/juto-shogan)
  * Email: somtombonu53@gmail.com
