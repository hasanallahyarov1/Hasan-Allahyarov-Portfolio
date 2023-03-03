import streamlit as st
import spacy

nlp = spacy.load("en_core_web_sm")

st.title("spaCy Named Entity Recognition Demo")

text = st.text_area("Enter some text to process:", height=200)

if st.button("Process"):
    doc = nlp(text)

    counts = {}
    for ent in doc.ents:
        if ent.label_ in counts:
            counts[ent.label_] += 1
        else:
            counts[ent.label_] = 1

    st.subheader("Named Entities")
    if len(doc.ents) > 0:
        for ent in doc.ents:
            st.write(f"{ent.text} - {ent.label_}")
    else:
        st.write("No named entities found.")

    st.subheader("Number of Entity by Type")
    for label, count in counts.items():
        subheads = f"{label} - {count}"
        st.write(subheads)

    st.subheader("Lemmas")
    if len(doc) > 0:
        for token in doc:
            st.write(f"{token.text} - {token.lemma_}")
    else:
        st.write("No text to process.")
