import pandas as pd 

import matplotlib.pyplot as plt 

 



df = pd.read_csv('/home/hadoop_user/Downloads/wordcount_output.tsv', sep='\t', names=['word', 'count']) 

 


top5 = df.sort_values(by='count', ascending=False).head(5) 

 



plt.figure(figsize=(6,6)) 

plt.pie(top5['count'], labels=top5['word'], autopct='%1.1f%%', startangle=140) 

plt.title("Top 5 Most Frequent Words") 

plt.axis('equal') 

 



plt.savefig('/home/hadoop_user/Downloads/top5_words_pie.png') 