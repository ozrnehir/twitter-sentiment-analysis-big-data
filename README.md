
# 📊 Twitter Sentiment Analysis using Big Data Tools

## 🚀 Overview
This project analyzes Twitter data related to the Iran–Israel conflict using Big Data technologies. The goal is to extract meaningful insights such as trending keywords and public sentiment from large-scale tweet data.

The project demonstrates a full data processing pipeline including data cleaning, MapReduce-based word counting, sentiment analysis, and data visualization.

---

## 🧠 Technologies Used
- Python
- Hadoop (MapReduce concept)
- Pandas
- Matplotlib
- PostgreSQL (SQL Analysis)
- VADER Sentiment Analysis

---

## ⚙️ Project Workflow
1. Data Collection  
   Tweets collected using Twitter API (JSON format)

2. Preprocessing  
   - Cleaning text (removing links, mentions, symbols)
   - Converting JSON to line-based format

3. MapReduce Processing  
   - mapper.py → emits word counts  
   - reducer.py → aggregates counts  

4. Sentiment Analysis  
   - Using VADER to classify tweets  
   - Output stored in CSV

5. Visualization  
   - Bar chart (Top 20 words)  
   - Pie chart (Top 5 words)

---

## ▶️ How to Run

# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install pandas matplotlib vaderSentiment

# 3. Preprocess data
python3 preprocessing.py

# 4. Run MapReduce
cat tweets_ldjson.json | python3 mapper.py | sort | python3 reducer.py > wordcount_output.tsv

# 5. Generate visualization
python3 plot_wordcount.py

---

## 📈 Sample Output
Top frequent words:
- Iran
- Israel
- War
- Military
- Conflict

(See wordcount_chart.png for visualization)

---

## 📄 Report
Detailed explanation of methodology, challenges, and results can be found here:

👉 Download Report

---

## 💡 Key Insights
- Majority of tweets show negative sentiment
- A small group of users contributes a large portion of content
- Discussions heavily focus on geopolitical conflict themes

---

## 📁 Project Structure
├── mapper.py ├── reducer.py ├── preprocessing.py ├── plot_wordcount.py ├── plot_wordcount_pie.py ├── add_sentiment.py ├── cleaned_tweets.csv ├── tweets_with_sentiment.csv ├── wordcount_output.tsv ├── wordcount_chart.png ├── report.pdf └── README.md

---

## 🎯 Conclusion
This project demonstrates how Big Data tools can be used to analyze social media data and extract meaningful insights about global events.

---

## 👤 Authors
- Elif Nehir Özer
