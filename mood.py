import streamlit as st
import plotly.express as px
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import glob

analyzer = SentimentIntensityAnalyzer()
st.title("Diary Entry")

st. subheader("Positivity")

dates = ["2023-10-21", "2023-10-22", "2023-10-23", "2023-10-24", "2023-10-25", "2023-10-26", "2023-10-27"]
positivity = []
negativity = []
filepaths = glob.glob("diary/*.txt")
for filepath in sorted(filepaths):
    with open(filepath, "r") as file:
        entry = file.read()
        scores = analyzer.polarity_scores(entry)
        positivity.append(scores["pos"])
        negativity.append(scores["neg"])

figure = px.line(x=dates, y=positivity, labels={"x": "Dates", "y": "Positivity"})
st.plotly_chart(figure)

st. subheader("Negativity")

figure2 = px.line(x=dates, y=negativity, labels={"x": "Dates", "y": "Negativity"})
st.plotly_chart(figure2)
