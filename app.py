import streamlit as st
import spacy
import json
import re
from spacy.tokens import Doc
from datetime import datetime
import csv
import io

# Load spaCy models
nlp = spacy.load("en_core_web_sm")

# Load product database
with open("database.json", "r") as f:
    raw_database = json.load(f)

# Create lemmatized version of the product database
product_database = {}
for product, shelf in raw_database.items():
    doc = nlp(product.lower())
    lemma = doc[0].lemma_
    product_database[lemma] = shelf
    product_database[product.lower()] = shelf


def preprocess_text(text: str) -> str:
    """
    Normalize text: lowercase, remove punctuation and extra whitespace
    """
    text = text.lower()
    text = re.sub(r"[^\w\s,]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def classify_intent(doc: Doc) -> str:
    """
    Classify the intent of the user's request

    """
    intent = "list"

    if any(token.text in ["where", "what", "which"] for token in doc):
        intent = "query"
    elif any(token.text in ["find", "locate", "get"] for token in doc):
        intent = "locate"
    return intent


def extract_products(doc: Doc) -> list:
    """
    Extract product mentions using NER, POS tagging, and lemmatization
    """
    products = set()

    # Using Named Entity Recognition for product identification
    for ent in doc.ents:
        if ent.label_ in ["PRODUCT", "FOOD", "ORG"]:
            products.add(ent.text.lower())
            products.add(ent.root.lemma_.lower())

    # Using POS tagging and lemmatization
    for token in doc:
        if token.pos_ == "NOUN" and not token.is_stop:
            products.add(token.text.lower())
            products.add(token.lemma_.lower())

    return list(products)


def process_input(text: str) -> dict:
    # Normalize text
    text = preprocess_text(text)

    # Process with spaCy
    doc = nlp(text)

    intent = classify_intent(doc)
    products = extract_products(doc)

    # Match products with database
    found_products = {}
    for product in products:
        if product in product_database:
            found_products[product] = product_database[product]

    return {"intent": intent, "products": found_products}


# Set up the Streamlit
st.title("Supermarket Assistant Chatbot")
st.write("Enter your shopping list and I'll tell you where to find each item!")

user_input = st.text_area(
    "What would you like to buy today?",
    placeholder="Example: I need bread, rice and chicken",
)

if user_input:
    results = process_input(user_input)

    # Show different responses based on intent
    if results["products"]:
        if results["intent"] == "query":
            st.write("### Here's the location of your items:")
        elif results["intent"] == "locate":
            st.write("### I've found these items for you:")
        else:
            st.write("### Here's where you can find your items:")

        # Display items in the app
        for product, shelf in results["products"].items():
            st.write(f"{product:10} → {shelf}")

        # List generation
        csv_content = io.StringIO()
        writer = csv.writer(csv_content)
        writer.writerow(["Shopping List"])
        writer.writerow([])
        writer.writerow(["Item", "Location"])
        for product, shelf in results["products"].items():
            writer.writerow([product.title(), shelf])

        # Download
        st.download_button(
            label=" Download Shopping List",
            data=csv_content.getvalue(),
            file_name="shopping_list.csv",
            mime="text/csv",
        )
