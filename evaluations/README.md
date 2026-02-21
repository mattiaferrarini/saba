# Evaluations

## Evaluation notebooks

Notebooks used to carry out the evaluations.

- **perplexity.ipynb**: Compute loss and perplexity on test dataset.
- **authorship.ipynb**: Authoship task (author classification).
- **rhyme_classification-ipynb**: Classify words base on rhymes.
- **rhyme_generation.ipynb**: Generate the last word of a poem.

## Analysis notebooks

Notebooks used to analyse the inner working of the model.

- **rhyme_attention.ipynb**: Compute attention scores for rhymes.
- **find_rhyme_head.ipynb**: Find heads with highest attention scores for rhymes.
- **rhyme_attention_visualization.ipynb**: Visualize attention scores for a certain poem.

## Scripts

Scripts used to create the evaluation datasets.

- **annotate_poems_with_rhymes.py**: Annotates a full poem with rhyme scheme.
- **annotate_stanzas_with_rhymes.py**: Splits a poem into stanzas and annotates each with rhyme scheme.
- **create_rhymes_dict.py**: Create a dataset of words grouped by rhymes.
- **create_authorship_dataset.py**: Creates the dataset for the authorship task.
