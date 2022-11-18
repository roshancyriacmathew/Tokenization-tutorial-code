#!/usr/bin/env python
# coding: utf-8

# In[1]:


text = '''Welcome to another video by the AI and DS Channel. In todays video we are going to study about tokenization. Dont forget to subscribe and leave a like if you enjoyed this video. '''


# In[2]:


tokens = text.split()
print(tokens)


# In[3]:


tokens = text.split('.')
print(tokens)


# In[4]:


import nltk
from nltk.tokenize import word_tokenize, sent_tokenize


# In[5]:


word_tokens = word_tokenize(text)
print(word_tokens)


# In[6]:


sentence_tokens = sent_tokenize(text)
print(sentence_tokens)


# In[7]:


from spacy.lang.en import English
nlp = English()


# In[9]:


word_tokens = nlp(text)
word_tokens_list = []
for token in word_tokens:
    word_tokens_list.append(token.text)
print(word_tokens_list)


# In[10]:


nlp = English()
nlp.add_pipe('sentencizer')
sent_tokens = nlp(text)
sent_tokens_list = []
for sent in sent_tokens.sents:
    sent_tokens_list.append(sent.text)
print(sent_tokens_list)


# In[11]:


from keras.preprocessing.text import text_to_word_sequence


# In[12]:


word_tokens = text_to_word_sequence(text)
print(word_tokens)


# In[13]:


sent_tokens = text_to_word_sequence(text, split=".")
print(sent_tokens)


# In[ ]:




