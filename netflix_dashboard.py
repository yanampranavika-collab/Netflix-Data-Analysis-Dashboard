import streamlit as st
import pandas as pd

st.title("🎬 Netflix Data Analysis Dashboard")

st.write("Exploratory Data Analysis of Netflix Movies and TV Shows")

df = pd.read_csv("netflix_titles.csv")

movies = len(df[df["type"] == "Movie"])
tv_shows = len(df[df["type"] == "TV Show"])

col1, col2, col3 = st.columns(3)

col1.metric("Total Titles", len(df))
col2.metric("Movies", movies)
col3.metric("TV Shows", tv_shows)

st.subheader("Movies vs TV Shows")

type_count = df["type"].value_counts()

st.bar_chart(type_count)

st.subheader("Top 10 Countries")

country_count = df["country"].value_counts().head(10)

st.bar_chart(country_count)

st.subheader("Content by Rating")

rating_count = df["rating"].value_counts()

st.bar_chart(rating_count)

st.subheader("Titles Added by Year")

year_count = df["release_year"].value_counts().sort_index()

st.line_chart(year_count)

st.subheader("Top 10 Directors")

director_count = df["director"].value_counts().head(10)

st.bar_chart(director_count)

st.subheader("Top 10 Genres")

genre_count = df["listed_in"].value_counts().head(10)

st.bar_chart(genre_count)

st.subheader("Movies vs TV Shows by Year")

type_year = df.groupby(["release_year", "type"]).size().unstack(fill_value=0)

st.line_chart(type_year)