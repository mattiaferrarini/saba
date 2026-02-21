import json
import string

TOP_RHYMES = 125
filename = "evaluations/italian_poems_test_rhymes.json"
output_file = f"evaluations/italian_rhymes_dict_{TOP_RHYMES}.json"

def clear_word(word):
    return word.rstrip(string.punctuation)

def get_rhyme(word1, word2):
    i = 0
    while i < len(word1) and i < len(word2) and word1[-1 - i] == word2[-1 - i]:
        i += 1
    return word1[-i:] if i > 0 else ""

if __name__ == "__main__":
    tagged_poems = json.load(open(filename, "r"))
    rhymes_dict = {}
    for poem in tagged_poems:
        stanzas = poem["text"].split("\n\n")
        lines = []
        for stanza in stanzas:
            lines.extend(stanza.split("\n"))

        rhymes = poem["rhyme_tags"]
        grouped = dict()
        last_words = [clear_word(line.split()[-1]) for line in lines if line.strip() != '']
        
        for i, w in enumerate(last_words):
            if rhymes[i] is not None and rhymes[i] in grouped:
                for match in grouped[rhymes[i]]:
                    rhyme_part = get_rhyme(w, match)
                    if rhyme_part:
                        if rhyme_part not in rhymes_dict:
                            rhymes_dict[rhyme_part] = set()
                        rhymes_dict[rhyme_part].add(w)
                        rhymes_dict[rhyme_part].add(match)
                grouped[rhymes[i]].add(w)
            else:
                grouped[rhymes[i]] = set([w])

    filtered = []
    for rhyme_part in rhymes_dict:
        if len(rhymes_dict[rhyme_part]) >= 10 and 3 <= len(rhyme_part) <= 3:
            filtered.append([rhyme_part, list(rhymes_dict[rhyme_part])])
    filtered.sort(key=lambda x: len(x[1]), reverse=True)

    tot_words = 0
    res = dict()
    for rhyme, words in filtered[:TOP_RHYMES]:
        res[rhyme] = words
        tot_words += len(words)

    print("Total rhyme parts found:", len(res))
    print("Total rhyming words:", tot_words)

    json.dump(res, open(output_file, "w", encoding="utf-8"), indent=2, ensure_ascii=False)