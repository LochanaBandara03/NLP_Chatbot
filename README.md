# Supermarket Assistant Chatbot

This is a web-based chatbot for a supermarket environment using Natural Language Processing (NLP) with spaCy and Streamlit.

The chatbot allows customers to type a shopping list in natural language and instantly returns the shelf numbers where each item can be found.

- **Input:** Free-text shopping list (e.g., “I want apples, milk, and detergent”).
- **Processing:** The chatbot uses spaCy NLP techniques (tokenization, POS tagging, Named Entity Recognition) to identify goods.
- **Output:** A web interface (Streamlit app) displays the shelf list mapping.

## Features

1. Web-based chatbot built with Streamlit.
2. Extracts goods using spaCy NLP pipeline.
3. Maps items to shelf numbers from a JSON product database.
4. Displays clean interactive results in the browser.
5. Handles at least 10+ goods with predefined shelf numbers.

## Installation

1. **Clone Repository**
   ```bash
   git clone https://github.com/LochanaBandara03/NLP_Chatbot.git
   cd NLP_Chatbot
   ```

2. **Create Virtual Environment (Not must)**
   ```bash
   python -m venv venv
   venv\Scripts\activate    # For the windows users
   ```

3. **Install Dependencies and Language Model**
   ```bash
   # Install all required packages
   pip install -r requirements.txt

   # Install spacy language model
   python -m spacy download en_core_web_sm
   ```

   > **Important Note:** The spaCy language model is required for the chatbot to work. If you get an error about missing 'en_core_web_sm', make sure to run the second command above.

## 📂 Project Structure

```
supermarket-chatbot/
├── app.py                 # Streamlit web app
├── database.json          # Product-to-shelf mapping
├── requirements.txt       # Python dependencies
├── README.md              # Setup and usage guide
└── user_guide.pdf         # User guide with examples
```

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Open your browser at http://localhost:8501 to interact with the chatbot.

## 🗄️ Database Example (database.json)

```json
{
  "apples": "Shelf 1",
  "bananas": "Shelf 1",
  "milk": "Shelf 3",
  "bread": "Shelf 2",
  "rice": "Shelf 4",
  "detergent": "Shelf 5",
  "shampoo": "Shelf 6",
  "toothpaste": "Shelf 6",
  "eggs": "Shelf 2",
  "chicken": "Shelf 7"
}
```

## 📖 How It Works

### User Input
Customer enters a shopping list in the Streamlit text input box.

### NLP Processing
spaCy extracts nouns/entities representing goods.

### Database Mapping
Matches goods with database.json.

### Output
Displays a formatted list of items with their shelf numbers in the Streamlit web app.

## 🧪 Example

**Input (via web app):**
```
I need bread, rice, and chicken.
```

**Output (displayed in Streamlit):**

```
bread   → Shelf 2
rice    → Shelf 4
chicken → Shelf 7
```

## 📦 Requirements

- Python 3.8+
- spaCy
- Streamlit
- JSON

Install with:

```bash
pip install spacy streamlit
```

## 🚀 Future Improvements

- Add voice input/output.
- Expand product database dynamically.
- Deploy app on Streamlit Cloud / Heroku for public use.
