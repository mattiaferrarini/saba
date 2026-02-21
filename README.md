# Saba 📜🖋🇮🇹

## About the model

Saba is a BERT model for Italian poetry. 
It was obtained via continued pretraining of [`dbmdz/bert-base-italian-xxl-cased`](https://huggingface.co/dbmdz/bert-base-italian-xxl-cased) 
on ~40k Italian song lyrics from [Wikisource](https://huggingface.co/datasets/mattiaferrarini/wikisource-italian-poems) and [Biblioteca Italiana](https://github.com/linhd-postdata/biblioteca_italiana).
The objective was Masked Language Modeling (MLM). 

The model is available on [Hugging Face](https://huggingface.co/mattiaferrarini/saba).
The training, validation and test datasets have been available in `datasets`.

## Evaluation

We evaluate Saba, the base model and Alberti (a prominent multilingual model for poetry) on various tasks.

### Test loss and pseudo-perplexity
Evaluates the model's statistical modeling of Italian poetry by computing the cross-entropy loss and pseudo-perplexity (PPPL) on test poems with 15% masked tokens.

| Model | Loss | PPPL |
|---|---|---|
| Base Model | 3.43 | 30.76 |
| Alberti | 5.41 | 223.86 |
| **Saba** | **1.90** | **6.68** |

### Rhyme classification
Evaluates the model's ability to capture phonetic information by predicting the rhyme (the last three characters) of words using a multinomial logistic regression classifier trained on the embeddings of multiple words. We consider the top 50 most frequent rhymes for evaluation.

| Model | Accuracy (%) | Macro F1 (%) |
|---|---|---|
| Base Model | 55.24 | 50.05 |
| Alberti | 67.07 | 63.36 |
| **Saba** | **71.26** | **69.12** |


### Author attribution
Evaluates stylistic understanding by predicting the author of a poem using a multinomial logistic regressor fitted on the [CLS] token embeddings.

| Model | Accuracy (%) | F1 Score (%) |
|---|---|---|
| Base Model | 61.63 | 57.04 |
| Alberti | 64.34 | 60.33 |
| **Saba** | **70.93** | **65.24** |

### Poem completion
Assesses the model's generative abilities through masked language modeling by predicting the masked final word of a poem, evaluated on both token-level and word-level accuracy.

| Model | Rhyming poems (Token) | Rhyming poems (Word) | Non-rhyming poems (Token) | Non-rhyming poems (Word) | Overall (Token) | Overall (Word) |
|---|---|---|---|---|---|---|
| Base Model | 6.11 | 5.43 | 19.35 | 17.95 | 6.51 | 7.24 |
| Alberti | 2.40 | 1.46 | 0.78 | 0.00 | 1.34 | 2.27 |
| **Saba** | **21.72** | **20.29** | **33.06** | **30.77** | **22.69** | **21.19** |

### Rhyme attention
Analyzes the model's internal computations by calculating the average attention score for the last tokens of previous lines (both rhyming and non-rhyming) to determine if it has developed specific mechanisms to detect and process rhymes. 

| Model | All endings | Rhyming endings |
|---|---|---|
| Base model | 12.37 | 2.45 |
| Alberti | 6.55 | 0.88 |
| **Saba** | **18.96** | **7.07** |


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

6. Run the code in the notebook `saba.ipynb` to train and evaluate the model step by step. The notebook is intended to be run on Google Colab. Modifying the first few cells is enough to be able to run it locally.

7. You can use the code in `evaluations/` to evaluate the already trained model available on Hugging Face.
