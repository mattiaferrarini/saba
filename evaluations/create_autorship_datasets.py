import os
import json
import random

filename_val = "datasets/italian_poems_val.json"
filename_test = "datasets/italian_poems_test.json"
out_val = "evaluations/italian_poems_val_autorship.json"
out_test = "evaluations/italian_poems_test_autorship.json"

def compute_author_stats(filename):
     author_stats = {}
     data = json.load(open(filename))
     for poem in data:
         author = poem.get("author")
         if author:
             author_stats[author] = author_stats.get(author, 0) + 1
     return author_stats

def filter_dataset(filename, chosen_authors):
    data = json.load(open(filename))
    filtered_data = [poem for poem in data if poem.get("author") in chosen_authors]
    return filtered_data

if __name__ == "__main__":
    stats_val = compute_author_stats(filename_val)
    stats_test = compute_author_stats(filename_test)

    intersect = set(stats_val.keys()).intersection(set(stats_test.keys()))
    print(f"Number of authors in {os.path.basename(filename_val)}: {len(stats_val)}")
    print(f"Number of authors in {os.path.basename(filename_test)}: {len(stats_test)}")
    print(f"Number of common authors: {len(intersect)}")

    filtered_authors = []
    for author in intersect:
        if author != "unknown":
            if 0 <= abs(stats_val[author] - stats_test[author]) <= 20 and stats_val[author] >= 10 and stats_test[author] >= 10:
                filtered_authors.append(author)

    print(f"Number of filtered authors: {len(filtered_authors)}")
    to_keep = max(len(filtered_authors), 10)
    print(f"Number of authors to keep in both datasets: {to_keep}")

    random.seed(42)
    if len(filtered_authors) <= to_keep:
        chosen_authors = filtered_authors.copy()
    else:
        chosen_authors = random.sample(filtered_authors, to_keep)

    print(f"Randomly selected {len(chosen_authors)} authors to keep.")
    print(chosen_authors)
    
    filtered_val = filter_dataset(filename_val, chosen_authors)
    filtered_test = filter_dataset(filename_test, chosen_authors)
    print(f"Filtered validation set size: {len(filtered_val)}")
    print(f"Filtered test set size: {len(filtered_test)}")

    json.dump(filtered_val, open(out_val, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    json.dump(filtered_test, open(out_test, "w", encoding="utf-8"), indent=2, ensure_ascii=False)