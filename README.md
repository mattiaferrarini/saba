# Saba 📜🖋🇮🇹

## About the model

Saba is a BERT model for Italian poetry. 
It was obtained via continued pretraining of [`dbmdz/bert-base-italian-xxl-cased`](https://huggingface.co/dbmdz/bert-base-italian-xxl-cased) 
on ~40k Italian song lyrics from [Wikisource](https://huggingface.co/datasets/mattiaferrarini/wikisource-italian-poems) and [Biblioteca Italiana](https://github.com/linhd-postdata/biblioteca_italiana).
The objective was Masked Language Modeling (MLM). 

The model is available on [Hugging Face](https://huggingface.co/mattiaferrarini/saba).

## Evaluation

The base model and the adapted model were tested on a held-out set of ~1k poems with the following results:

| Model | MLM Loss | Perplexity |
|----------|----------|----------|
| Base    | 3.39    | 29.56    |
| **Saba**    | **1.94**    | **6.94**    |

**Evaluation of the learned representations will be made available in the future, once a suitable dataset has been created / identified.**

## Why Saba?
Following the tradition of giving Italian names to BERT models for the Italian language 
(see [AlBERTo](https://github.com/marcopoli/AlBERTo-it), [GilBERTo](https://github.com/idb-ita/GilBERTo), [UmBERTo](https://github.com/musixmatchresearch/umberto)), 
we dedicate this model to the Italian poet and novelist [Umberto Saba](https://en.wikipedia.org/wiki/Umberto_Saba) (9 March 1883 – 25 August 1957).

## How to run the code

1. Clone the repository:
```
git clone https://github.com/mattiaferarrini/saba.git
```

2. Download the two datasets used for training:
- The CSV of Wikisource Italian Poems from [Kaggle](https://www.kaggle.com/datasets/mattiaferrarini/wikisource-italian-poems),
- The zip of Biblioteca Italiana from [GitHub](https://github.com/linhd-postdata/biblioteca_italiana/blob/master/biblitaliana.zip).

3. Unzip the `biblitaliana.zip` file and clean it:
```
python bibl_cleaner.py 
```

4. Combine the two datasets into a single one:
```
python combiner.py italian_poems.json
```

5. Split this dataset into train, validation and test:
```
python splitter.py italian_poems.json
```

6. Run the code in the notebook `saba.ipynb` to train and evaluate the model step by step.
