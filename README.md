
# 📊 Twitter Sentiment Analysis using Big Data Tools

## 🚀 Overview
This project analyzes Twitter data related to the Iran–Israel conflict to extract insights about public sentiment and trending topics.

It demonstrates an end-to-end Big Data pipeline including data preprocessing, Hadoop-style MapReduce processing, SQL-based sentiment analysis, and data visualization.

---

## 🧠 Technologies Used
- Python (data processing & visualization)
- Hadoop & HDFS (conceptual usage for large-scale processing)
- MapReduce (word frequency analysis)
- PostgreSQL (SQL-based sentiment analysis)
- Pandas & Matplotlib
- VADER Sentiment Analysis

---

## ⚙️ Project Workflow
1. Data Collection
   - Tweets collected via Twitter API in JSON format

2. Preprocessing
   - Cleaning text (removing links, mentions, symbols)
   - Converting nested JSON into line-based format for processing

3. MapReduce Processing
   - mapper.py → emits word counts  
   - reducer.py → aggregates word frequencies  

4. Sentiment Analysis
   - Tweets labeled using VADER sentiment analysis  
   - Stored and analyzed using SQL queries  

5. Visualization
   - Bar chart (Top 20 most frequent words)
   - Pie chart (Top 5 keywords)

---

## ▶️ How to Run

Run the following commands step by step:

bash python3 -m venv venv source venv/bin/activate  pip install pandas matplotlib vaderSentiment  python3 preprocessing.py  cat tweets_ldjson.json | python3 mapper.py | sort | python3 reducer.py > wordcount_output.tsv  python3 plot_wordcount.py 

---

## 📈 Sample Output
The most frequent words reflect major themes such as:

- Iran  
- Israel  
- War  
- Military  
- Conflict  

These results highlight the focus of public discourse during the analyzed period.

---

## 📊 Visualization
See generated chart:

- wordcount_chart.png

---

## 📄 Detailed Report

The report is included in this repository and contains detailed explanations of the Hadoop-based processing, SQL sentiment analysis, methodology, and implementation steps.
---

## 💡 Key Insights
- Majority of tweets show negative sentiment
- Public discussion is heavily focused on geopolitical conflict
- A small number of users generate a large portion of content
- Data preprocessing is critical for accurate analysis   

---

## 📁 Project Structure
├── mapper.py ├── reducer.py ├── preprocessing.py ├── plot_wordcount.py ├── plot_wordcount_pie.py ├── add_sentiment.py ├── cleaned_tweets.csv ├── tweets_with_sentiment.csv ├── wordcount_output.tsv ├── wordcount_chart.png ├── report.pdf └── README.md

---

## 🎯 Conclusion
This project demonstrates how Big Data tools and social media analytics can be combined to understand global events and public opinion.

---

## 👤 Authors
- Elif Nehir Özer
