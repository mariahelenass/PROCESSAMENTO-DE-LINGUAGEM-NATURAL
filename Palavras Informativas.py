#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk


# In[5]:


nltk.corpus.gutenberg.fileids()


# In[7]:


hamlet = nltk.corpus.gutenberg.words("shakespeare-hamlet.txt")


# In[8]:


hamlet_fd = nltk.FreqDist(hamlet)


# In[9]:


hamlet_fd


# In[15]:


hamlet_fd_100 = hamlet_fd.most_common(100)


# In[16]:


# Comparação com outro livro
moby = nltk.corpus.gutenberg.words("melville-moby_dick.txt")
moby_fd = nltk.FreqDist(moby)
moby_fd_100 = moby_fd.most_common(100)


# In[17]:


hamlet_fd_100


# In[18]:


hamlet_100 = [word[0] for word in hamlet_fd_100]
moby_100 = [word[0] for word in moby_fd_100]


# In[19]:


# Palavras mais descrivas de hamlet
set(hamlet_100) - set(moby_100)


# In[20]:


# Palavras mais descritivas de moby dick
set(moby_100) - set(hamlet_100)

