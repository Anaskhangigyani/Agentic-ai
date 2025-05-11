# Agentic AI Streaming Chatbot with Integrated Tool Calling

This project showcases a real-time, interactive AI chatbot experience, built within a single Python file for simplicity and ease of deployment. It harnesses the power of **Chainlit** for a user-friendly interface, the intelligent agentic capabilities of the **OpenAI Agents SDK**, and the advanced language understanding of **Gemini**. The chatbot features **tool calling**, enabling it to interact with defined functions to provide richer and more context-aware responses. The **streaming** functionality allows you to watch the chatbot's responses unfold in real-time, enhancing the conversational flow.

This self-contained chatbot is equipped with **two tools**, both implemented within the same file:

* **`get_weather`**: Retrieves weather information for a given city name.
* **`piaic_student_finder`**: Locates student details based on a provided roll number.

## How to Run the Application Locally (Single File Implementation)

Follow these simple steps to get this tool-calling chatbot running on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/yourrepository.git](https://github.com/yourusername/yourrepository.git)
    ```
2.  **Navigate into the project directory:**
    ```bash
    cd toolcalling-ai-chatbot
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
    uv run chainlit run src/toolcalling-ai-chatbot/chatbot.py -w
    ```

Once executed, this single-file tool-calling chatbot will be accessible through the Chainlit UI, ready for you to interact with its weather and student information retrieval capabilities!