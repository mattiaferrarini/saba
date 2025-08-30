import json

def load_and_clean_data(input_file='biblitaliana.json', output_file='cleaned_biblitaliana.json'):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    cleaned_data = []
    for obj in data:
        # Flatten the text field from list of lists of {"verse": "..."} to list of list of strings
        flattened_text = []
        if obj.get('text'):
            for section in obj['text']:
                if isinstance(section, list):
                    verse_list = [verse.get('verse', '') for verse in section if isinstance(verse, dict)]
                    flattened_text.append(verse_list)
        
        cleaned_obj = {
            'title': str(obj.get('title', '')),
            'author': str(obj.get('author', '')),
            'url': str(obj.get('url', '')),
            'text': flattened_text
        }
        
        # Only add poems that have non-empty text
        if flattened_text:
            cleaned_data.append(cleaned_obj)
        else:
            print(f"Skipping empty poem: {obj.get('title', 'Unknown Title')} by {obj.get('author', 'Unknown Author')}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=2)
    
    return cleaned_data

if __name__ == "__main__":
    cleaned_data = load_and_clean_data()
    print(f"Processed {len(cleaned_data)} items")