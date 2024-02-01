# Project : Automated Blog Creation System 🤖

## Overview
This project aims to create an automated blog creation system using the Gemini Pro language model and various agents orchestrated by CrewAI. The system includes a Telegram bot for user interaction, a multi-agent setup for blog creation, integration with Notion for storing drafts, and a notification system for approval and publishing.

## Architecture
![System Architecture](https://github.com/vanshpatelx/AutomatedBlogCreationSystemWithApproval/blob/main/img/img.png)


## How Works ?
- **User Interaction:** Users initiate the blog creation process by interacting with a Telegram bot and providing a blog name.
- **Agent Orchestration:** CrewAI orchestrates three agents for specific roles: Content Generator, Notion Publisher, and Notifier.
- **Agent Roles:**
   - **Content Generator:** Utilizes the Gemini Pro language model to create engaging blog content based on the provided blog name with four agents.
       - Senior Researcher
       - Insight Researcher
       - Tech Content Strategist
       - Markdown Formatter
   -  **Notion Publication:** The Notion Publisher Agent adds the generated content to a designated Notion workspace for draft storage.
  - **Notification for Approval:** The Notifier Agent sends a notification to the user, containing a preview link to the blog draft in Notion, indicating that the blog is ready for review.
  - **User Review and Approval:** Users receive the notification and review the blog draft in Notion.
     - Users approve the draft through the Telegram bot interface.
  - **Automated Publishing (Optional):** An optional step can be added to automate the publishing of approved content.

## Requirements
- CrewAI library
- LangChain community tools
- LangChain Google Generative AI (Gemini Pro)
- Streamlit
- python-telegram-bot
- Notion SDK (notion-sdk-python)
- postgreSQL

## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/vanshpatelx/AutomatedBlogCreationSystemWithApproval
    cd AutomatedBlogCreationSystemWithApproval
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
