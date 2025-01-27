# 📰 News Research Tool

## 📌 Overview
The **News Research Tool** is an AI-powered application that extracts and analyzes news content from multiple sources using a **Retrieval-Augmented Generation (RAG)** approach. It combines **FAISS** for vector storage and **Google Gemini API** for language processing to generate fact-based answers. The **Streamlit** UI ensures easy accessibility for users.  

---

## ✨ Features
- **RAG-Based Query Answering** – Combines retrieval and generation for accurate responses.
- **Multi-Source News Extraction**: Input multiple news URLs to extract content automatically.
- **Content Chunking & Vector Storage**: Processes and stores extracted text in a **FAISS** vector database.
- **Intelligent Query Answering**: Retrieves the most relevant content chunks and generates accurate responses using the **Google Gemini API** (I have also included example using Ollama if you want to run the model on your local PC).
- **Streamlit UI**: A lightweight web interface for seamless interaction.


## 🔥 What is RAG?  
**Retrieval-Augmented Generation (RAG)** is an advanced AI technique that enhances the accuracy of generated responses by combining **information retrieval** with **language generation**.  
- **Retrieval**: Extracts and stores relevant text in a **FAISS vector database**.  
- **Augmentation**: Fetches the most relevant content based on the user’s query.  
- **Generation**: Uses the **Google Gemini API** to generate responses based on the retrieved data.  

This approach ensures **factually grounded** and **context-aware** answers, making the tool reliable for news analysis.  

---

## 🛠️ Installation Guidelines
Follow these steps to set up the News Research Tool:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/news-research-tool.git
   cd news-research-tool

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   
4. **Set up your Gemini API key by creating a .env file in the project root and add your API**
   ```
   GEMINI_API_KEY = "Your API Key"

5. **Run Application**
   ```bash
   streamlit run main.py

## 🚀 Usage Example  

Run the application using the above command. The web app will open in your browser

### 🔹 Step 1: Enter News URLs  
- Paste up to **three** news article URLs in the input fields.  

### 🔹 Step 2: Process URLs  
- The system fetches, splits, and stores the extracted text in the vectorIndex.pkl file.  

### 🔹 Step 3: Ask a Question  
- Enter your query in the provided input box.  

### 🔹 Step 4: Receive an Answer  
- The tool retrieves relevant content from the vector store, processes it using the **Google Gemini API**, and displays an answer.  

---

## 🏗️ Technologies Used  
- 🐍 **Python** – Core programming language.  
- 🔗 **Langchain** – The base of every feature.
- 🎨 **Streamlit** – Used for the web-based UI.  
- 🗄️ **FAISS** – Vector store for efficient data retrieval.  
- 🧠 **Google Gemini API** – Generates intelligent responses.   