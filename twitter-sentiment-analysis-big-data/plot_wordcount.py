import pandas as pd 

import matplotlib.pyplot as plt 

 



df = pd.read_csv("/home/hadoop_user/Downloads/wordcount_output.tsv", sep="\t", header=None, names=["Word", "Frequency"]) 

 



df = df.sort_values(by="Frequency", ascending=False) 

 



plt.figure(figsize=(12,6)) 

plt.bar(df["Word"][:20], df["Frequency"][:20], color="skyblue") 

plt.title("Top 20 Most Frequent Words in Tweets") 

plt.xlabel("Words") 

plt.ylabel("Frequency") 

plt.xticks(rotation=45) 

plt.tight_layout() 

 



plt.savefig("/home/hadoop_user/Downloads/word_freq_en.png") 