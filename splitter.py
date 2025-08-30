import json
import random
import sys

def text_to_str(poem):
    return "\n\n".join("\n".join(stanza) for stanza in poem.get("text", []))

def split_json(input_path, seed=42):
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    random.seed(seed)
    indices = list(range(len(data)))
    random.shuffle(indices)

    n = len(data)
    n_train = int(n * 0.95)
    n_val = int(n * 0.025)

    train_idx = indices[:n_train]
    val_idx = indices[n_train:n_train+n_val]
    test_idx = indices[n_train+n_val:]

    def process_item(item):
        return {
            "text": text_to_str(item),
            "url": item.get("url", "")
        }

    train = [process_item(data[i]) for i in train_idx]
    val = [process_item(data[i]) for i in val_idx]
    test = [process_item(data[i]) for i in test_idx]

    def out_path(suffix):
        if input_path.endswith('.json'):
            return input_path[:-5] + f'_{suffix}.json'
        return input_path + f'_{suffix}'

    train_path = out_path('train')
    val_path = out_path('val')
    test_path = out_path('test')

    with open(train_path, 'w', encoding='utf-8') as f:
        json.dump(train, f, ensure_ascii=False, indent=2)
    with open(val_path, 'w', encoding='utf-8') as f:
        json.dump(val, f, ensure_ascii=False, indent=2)
    with open(test_path, 'w', encoding='utf-8') as f:
        json.dump(test, f, ensure_ascii=False, indent=2)

    print(f"Train size: {len(train)} ({train_path})")
    print(f"Validation size: {len(val)} ({val_path})")
    print(f"Test size: {len(test)} ({test_path})")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python splitter.py <input_json>")
        sys.exit(1)
    split_json(sys.argv[1])
