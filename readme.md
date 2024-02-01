# Project Readme: Automated Blog Creation System 🤖

## Overview
This project aims to create an automated blog creation system using the Gemini Pro language model and various agents orchestrated by CrewAI. The system includes a Telegram bot for user interaction, a multi-agent setup for blog creation, integration with Notion for storing drafts, and a notification system for approval and publishing.

## Requirements
- CrewAI library
- LangChain community tools
- LangChain Google Generative AI (Gemini Pro)
- Streamlit
- Python-dotenv
- python-telegram-bot
- Notion SDK (notion-sdk-python)

## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables by creating a `.env` file and adding necessary keys:

    ```dotenv
    TELEGRAM_API_TOKEN=your_telegram_api_token_here
    NOTION_API_TOKEN=your_notion_api_token_here
    GOOGLE_API_KEY=your_google_api_key_here
    ```

## Usage

### 1. Telegram Bot Setup
- Create a Telegram bot using the BotFather on Telegram. Obtain the API token and set it in the `.env` file.

### 2. Agent Configuration
- Configure agents for blog creation, including roles such as "Content Generator," "Notion Publisher," and "Notifier."

### 3. Task Definition
- Define tasks for each agent, including creating blog content, adding it to Notion, and sending notifications for approval.

### 4. Crew Formation
- Create a crew named `blog_crew` consisting of the configured agents and tasks. Set the crew to execute tasks sequentially.

### 5. Main Function
- Implement the main function to set up the Telegram bot interface and handle user inputs. When the user provides the blog name via the Telegram bot, trigger the execution of the defined crew tasks.

### 6. Running the Script
- Execute the script by running the following command:

    ```bash
    python your_script_name.py
    ```

- Interact with the Telegram bot by providing the blog name to initiate the automated blog creation process.

## Additional Notes
- Ensure secure storage of API keys in the `.env` file.
- Customize agent roles, goals, and backstories based on your project requirements.
- Integrate with Notion using the Notion SDK for adding and managing blog drafts.
- Utilize the notification system for approval and preview links.

Feel free to extend the functionality, experiment with different language models, and adapt the system to your specific use case for seamless and automated blog creation!# AutomatedBlogCreationSystemWithApproval
# AutomatedBlogCreationSystemWithApproval
