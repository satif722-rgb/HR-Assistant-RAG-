🧠 HR Policy Assistant (RAG-based AI Application)

An AI-powered HR assistant built using Retrieval-Augmented Generation (RAG) that answers employee questions strictly based on internal HR policy documents such as Leave Policy, Employee Handbook, and HR Manual.
The system uses semantic search and a local LLM to provide accurate, context-only, and hallucination-free answers through a clean chat interface.

✨ Features

📄 Supports multiple HR documents (PDFs)

🔍 Semantic document retrieval using FAISS

🧠 Context-aware answers using RAG architecture

🚫 Hallucination control using similarity thresholds

💬 Chat-style UI with conversation history

🔒 Uses a local LLM (Ollama) for privacy & offline usage

🎯 Simple, employee-friendly English responses

User Question
      |
      v
Streamlit UI
      |
      v
ask_hr()  ←───────────────┐
      |                   |
      v                   |
FAISS Vector Search       |
      |                   |
      v                   |
Relevant Document Chunks  |
      |                   |
      v                   |
Prompt Construction (Context + Question)
      |
      v
Local LLM (Ollama)
      |
      v
Final Answer (Context-only)


HR-RAG/
│
├── data/
│   ├── leave_policy.pdf
│   ├── employee_handbook.pdf
│   └── hr_policy_manual.pdf
│
├── vector_store/
│   ├── index.faiss
│   └── index.pkl
│
├── ingest.py          # PDF loading, chunking & vector indexing
├── rag.py             # Core RAG logic (retrieval + LLM)
├── prompt.py          # Prompt template & response rules
├── logger.py          # Logs similarity scores for threshold tuning
├── app.py              # Streamlit chat interface
├── similarity_logs.csv# Generated similarity score logs
├── requirements.txt
└── README.md

RAG Flow (Step-by-Step)

HR PDFs are loaded and split into chunks

Each chunk is converted into embeddings

Embeddings are stored in FAISS vector database

User asks a question via UI

Relevant chunks are retrieved using semantic similarity

Low-quality matches are filtered using similarity thresholds

A strict prompt is built using retrieved context

Local LLM generates a grounded answer

Answer is shown in chat UI

🧩 Core Components Explained
1️⃣ Document Ingestion (ingest.py)

Loads multiple HR PDFs

Adds metadata (document type, file name, page)

Splits text into overlapping chunks

Stores embeddings in FAISS

2️⃣ Prompt Control (prompt.py)

Forces context-only answers

Prevents hallucinations

Uses simple, employee-friendly English

Returns a fixed “I don’t know” response when data is missing

3️⃣ RAG Logic (rag.py)

Performs similarity search

Applies document-specific similarity thresholds

Builds final prompt

Invokes local LLM

Returns only the answer (no fake sources)

4️⃣ User Interface (app.py)

Chat-style interface (user right, bot left)

Persistent conversation history

Fixed bottom input bar

Clean, professional UI theme

🛠️ Tech Stack

Language: Python

LLM: Ollama (Local)

Framework: LangChain

Vector DB: FAISS

Embeddings: HuggingFace (BGE)

UI: Streamlit

🚀 How to Run the Project
1️⃣ Create Virtual Environment
python -m venv renv
renv\Scripts\activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Ingest Documents
python ingest.py

4️⃣ Run the App
streamlit run app.py

🧪 Example Questions

How many medical leaves are allowed?

What is the dress code policy?

Is work from home allowed?

What happens if I exhaust all leaves?

What is the maternity leave policy?

🎯 Key Learnings

Built a complete RAG pipeline end-to-end

Learned prompt engineering for hallucination control

Implemented similarity threshold tuning

Designed clean UI–backend separation

Worked with local LLMs for privacy-focused AI

📌 Future Improvements

Add authentication for internal use

Support DOCX / TXT files

Add admin dashboard for document updates

Deploy using Docker

## 📊 Similarity Threshold Logging & Tuning

To reduce hallucinations and improve answer quality, this project includes a
**similarity score logging mechanism**.

During development, similarity scores between user queries and retrieved
document chunks are logged into a CSV file using `logger.py`.

### How it works:
- Each user query retrieves document chunks with similarity scores
- Scores, document metadata, and text previews are logged into a CSV file
- The CSV file is analyzed to determine optimal similarity thresholds
- Document-specific thresholds are then applied in the RAG pipeline

This approach ensures:
- Irrelevant documents are filtered out
- Answers are generated only from highly relevant context
- Better control over hallucinations and response accuracy

This tuning process was used to define different similarity thresholds for:
- Leave Policy
- Employee Handbook
- HR Policy Manual
- 
### Similarity Logger (`logger.py`)
- Logs similarity scores, document metadata, and text previews into a CSV file
- Helps analyze retrieval quality across different types of HR documents
- Used to empirically determine optimal similarity threshold values
- Improves reliability and trustworthiness of RAG responses


👤 Author
Siddiqui Atif Iqbal
AI / ML Enthusiast
GitHub: your-github-link
LinkedIn: your-linkedin-link

This project demonstrates real-world RAG design, not just a demo chatbot.
It focuses on accuracy, trust, and clean architecture, which are critical in enterprise AI systems.

