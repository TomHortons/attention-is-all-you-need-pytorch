#%%
import spacy

# %%
nlp = spacy.load("en_core_web_sm")

# %%
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# %%
src_lang_model = spacy.load("de_core_news_sm")
trg_lang_model = spacy.load("en_core_news_sm")