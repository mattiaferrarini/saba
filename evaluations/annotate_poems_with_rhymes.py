import json
from rhymetagger import RhymeTagger
from tqdm import tqdm

data = json.load(open("datasets/italian_poems_test.json"))

unlabeled = []

for entry in data:
    txt = entry["text"]
    stanzas_txt = txt.split("\n\n")
    stanzas = [stanza.split("\n") for stanza in stanzas_txt]
    poem = [line for stanza in stanzas for line in stanza if line.strip() != ""]
    unlabeled.append([poem, txt])

rt = RhymeTagger()
rt.load_model(model="it")
labeled = []

for poem, txt in tqdm(unlabeled, desc="Tagging poems"):
    rhyme_tags = rt.tag(poem, output_format=3)
    labeled.append({"text": txt, "rhyme_tags": rhyme_tags})
json.dump(labeled, open("evaluations/italian_poems_test_rhymes.json", "w"), indent=2, ensure_ascii=False)