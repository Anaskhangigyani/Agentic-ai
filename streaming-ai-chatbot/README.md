# Agentic AI Streaming Chatbot

This project offers a real-time, interactive AI chatbot experience, leveraging cutting-edge technologies to provide dynamic and engaging conversations. At its core, it combines the user-friendly interface of **Chainlit**, the powerful agentic capabilities of the **OpenAI Agents SDK**, and the advanced language understanding of **Gemini**. The implementation also features **streaming**, allowing you to see the chatbot's responses unfold in real-time, enhancing the conversational flow.

## How to Run the Application Locally

Follow these simple steps to get the chatbot up and running on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/yourrepository.git](https://github.com/yourusername/yourrepository.git)
    ```
2.  **Navigate into the project directory:**
    ```bash
    cd streaming-ai-chatbot
    ```
3.  **Set up a virtual environment (if you haven't already):**
    ```bash
    uv venv
    ```
4.  **Activate the virtual environment:**
    * **On Windows:**
        ```bash
        .\.venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```
5.  **Install the required dependencies:**
    ```bash
    uv add -r requirements.txt
    ```
6.  **Run the application:**
    ```bash
    uv run chainlit run src/streaming_ai_chatbot/chatbot.py -w
    ```

Once executed, your chatbot should be accessible through the Chainlit UI, ready for you to start interacting!