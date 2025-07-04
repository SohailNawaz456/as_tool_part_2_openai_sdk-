🧠 Multi-Agent Assistant with Gemini API
This project demonstrates a multi-agent system using Google's Gemini language model API. It includes agents that handle shopping, support, and triage (delegation of queries), built with a flexible Agent framework.

🚀 Features
🤖 Triage Agent: Delegates tasks to the appropriate agent.

🛍️ Shopping Agent: Assists users in finding products and making purchase decisions.

🔧 Support Agent: Helps users with post-purchase issues like returns.

✅/❌ Emojis used for agent response identity.

✅ Powered by gemini-2.0-flash-lite model.

📁 Project Structure
.
├── agents/
│   ├── __init__.py
│   └── (Agent, Runner, Models defined here)
├── .env
├── main.py
└── README.md
🛠️ Requirements
Python 3.9+

Google Gemini API Access

python-dotenv

rich

Install dependencies:
pip install -r requirements.txt
Or manually:

pip install python-dotenv rich

🔐 Environment Setup
GEMINI_API_KEY=your_gemini_api_key

Example Output
✅ I found some great wrist watches for you! Would you prefer analog or smart?

🧩 Agents Overview
triage_agent
Delegates input based on query type.

Never replies directly — uses tools only.

shopping_agent
Handles product search.

Replies start with ✅ emoji.

support_agent
Handles post-purchase help.

Replies start with ❌ emoji.

📬 Feedback
Pull requests and issues are welcome. Feel free to contribute or ask questions!
