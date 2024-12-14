import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

df = pd.read_csv('DataSets/unsafe_speed_data.csv')
plt.figure(figsize=(10,6))
sns.barplot(data=df, x='BOROUGH', y='NUMBER OF PERSONS INJURED', color='skyblue', label='Persons injured')
sns.barplot(data=df, x='BOROUGH', y='NUMBER OF PERSONS KILLED', color='orange', label='Persons killed')
# df.plot(kind='bar', x='BOROUGH')
plt.title('Number of deaths and injuries caused by speeding')
plt.xlabel('Borough in NYC')
plt.ylabel('Number of persons')
st.pyplot(plt)
