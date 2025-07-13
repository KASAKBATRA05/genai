import nltk
nltk.download('punkt')

import streamlit as st
from backend.reader import extract_text_from_pdf, extract_text_from_txt
from backend.summarizer import summarize_text
from backend.qna_engine import answer_question
from backend.challenge_mode import generate_questions, evaluate_answer

st.title("GenAI NLP Assistant")

uploaded = st.file_uploader("Upload PDF or TXT", type=["pdf","txt"])
text = ""
if uploaded:
    ext = uploaded.name.split('.')[-1]
    if ext=="pdf":
        text = extract_text_from_pdf(uploaded)
    else:
        text = extract_text_from_txt(uploaded)
    st.success("Text extracted!")

if st.button("Generate Summary"):
    st.write(summarize_text(text))

q = st.text_input("Ask question:")
if q:
    ans, ctx = answer_question(q, text)
    st.write("**Answer:**", ans)
    st.write("**Context:**", ctx)

if st.button("Challenge Me"):
    qs = generate_questions(text)
    for i, (question, correct, sent) in enumerate(qs):
        st.write(f"Q{i+1}: {question}")
        uans = st.text_input(f"Your answer Q{i+1}:", key=i)
        if uans:
            verdict, feedback = evaluate_answer(uans, correct)
            st.write(verdict, feedback)
