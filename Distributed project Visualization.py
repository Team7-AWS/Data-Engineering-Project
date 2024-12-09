#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df3 = pd.read_csv("athena3.csv")
df3


# In[3]:


plt.figure(figsize=(8, 5))
plt.plot(df3["subject"], df3["avg_score"], marker='o', linestyle='-', color='blue')

# Add titles and labels
plt.title("Average Score by Subject", fontsize=14)
plt.xlabel("Subject", fontsize=12)
plt.ylabel("Average Score", fontsize=12)

# Display gridlines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()


# In[4]:


df5 = pd.read_csv("athena5.csv")
df5


# In[5]:


plt.figure(figsize=(8, 6))
plt.scatter(df5['weekly_self_study_hours'], df5['total_score'], alpha=0.6, color='blue')

# Add titles and labels
plt.title('Scatter Plot of Weekly Self-Study Hours vs Total Score', fontsize=14)
plt.xlabel('Weekly Self-Study Hours', fontsize=12)
plt.ylabel('Total Score', fontsize=12)

# Display gridlines for better readability
plt.grid(alpha=0.3)

# Show the plot
plt.show()


# In[6]:


df7 = pd.read_csv("athena7.csv")
df7


# In[7]:


plt.figure(figsize=(10, 6))
plt.hist(df7['total_score'], bins=20, color='blue', edgecolor='black', alpha=0.7)

# Adding title and labels
plt.title('Distribution of Total Scores', fontsize=14)
plt.xlabel('Total Score', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()


# In[8]:


df8 = pd.read_csv('athena8.csv')
df8


# In[9]:


# Create the box plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df8, x='standardized_category', y='total_score', palette='Set2')

# Add titles and labels
plt.title('Distribution of Total Scores by Performance Category', fontsize=16)
plt.xlabel('Performance Category', fontsize=14)
plt.ylabel('Total Score', fontsize=14)

# Show the plot
plt.show()


# In[ ]:




