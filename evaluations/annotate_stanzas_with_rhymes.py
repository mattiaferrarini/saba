import json
from rhymetagger import RhymeTagger
from tqdm import tqdm

data = json.load(open("datasets/italian_poems_test.json"))

unlabeled = []

for entry in data:
    txt = entry["text"]
    stanzas_txt = txt.split("\n\n")
    stanzas = [stanza.split("\n") for stanza in stanzas_txt]
    unlabeled.extend([[stanza, "\n".join(stanza)] for stanza in stanzas])

rt = RhymeTagger()
rt.load_model(model="it")
labeled = []

for stanza, stanza_txt in tqdm(unlabeled, desc="Tagging stanzas"):
    rhyme_tags = rt.tag(stanza, output_format=3)
    labeled.append({"text": stanza_txt, "rhyme_tags": rhyme_tags})

json.dump(labeled, open("evaluations/italian_poems_test_stanzas_rhymes.json", "w"), indent=2, ensure_ascii=False)