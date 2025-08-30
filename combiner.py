import json
import os
import argparse

def load_poems_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            poems = json.load(f)
        print(f"Loaded {len(poems)} poems from {file_path}")
        return poems
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return []

def create_poem_key(poem):
    title = poem.get('title') or ''
    author = poem.get('author') or ''
    
    # Ensure we have strings before calling lower() and strip()
    title = str(title).lower().strip()
    author = str(author).lower().strip()
    
    return (title, author)

def combine_unique_poems(file_paths):
    all_poems = []
    seen_poems = {}  # Maps (title, author) to source_file
    duplicate_count = 0
    source_counts = {}
    duplicate_counts = {}  # track duplicates per source file

    for file_path in file_paths:
        if not os.path.exists(file_path):
            print(f"Warning: File {file_path} does not exist, skipping...")
            continue

        poems = load_poems_from_file(file_path)
        source_name = os.path.basename(file_path)
        source_counts[source_name] = 0
        duplicate_counts[source_name] = 0  # Initialize duplicate count for this file

        for poem in poems:
            poem_key = create_poem_key(poem)

            # Check if we've seen this poem before
            if poem_key in seen_poems:
                existing_source = seen_poems[poem_key]
                # Only consider it a duplicate if it's from a different file
                if existing_source != source_name:
                    duplicate_count += 1
                    duplicate_counts[source_name] += 1  # Increment per-file duplicate count
                    # print(f"Duplicate found: '{poem.get('title', 'Unknown')}' by '{poem.get('author', 'Unknown')}' (in {source_name}, already exists in {existing_source})")
                    continue  # Skip this poem as it's a duplicate from another file
                # If it's from the same file, it's not a duplicate, so we add it
            else:
                # First time seeing this poem, record its source
                seen_poems[poem_key] = source_name

            # Add the poem (either first occurrence or same-file occurrence)
            poem_with_source = poem.copy()
            all_poems.append(poem_with_source)
            source_counts[source_name] += 1

    print(f"\nTotal unique poems: {len(all_poems)}")
    print(f"Total duplicates removed: {duplicate_count}")
    print(f"\nDuplicates by source file:")
    for source_file, count in duplicate_counts.items():
        print(f"  - {source_file}: {count} duplicates")

    return all_poems, source_counts

def save_combined_poems(poems, output_path):
    try:
        # Create output directory if it doesn't exist and path contains a directory
        output_dir = os.path.dirname(output_path)
        if output_dir:  # Only create directory if path contains one
            os.makedirs(output_dir, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(poems, f, ensure_ascii=False, indent=2)
        
        print(f"Successfully saved {len(poems)} unique poems to {output_path}")
    except Exception as e:
        print(f"Error saving to {output_path}: {e}")

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Combine unique poems from multiple JSON files')
    parser.add_argument('output_path', help='Output path for the combined poems JSON file')
    args = parser.parse_args()
    
    # Input files
    files = [
        "cleaned_biblitaliana.json", 
        "wikisource_poems_it.json"
    ]
    
    # Output file from command line
    output_file = args.output_path
    
    print("Starting poem combination process...")
    print(f"Input files: {files}")
    print(f"Output file: {output_file}")
    print("-" * 50)
    
    # Combine unique poems
    unique_poems, source_counts = combine_unique_poems(files)
    
    if unique_poems:
        # Save to output file
        save_combined_poems(unique_poems, output_file)
        
        # Print some statistics
        print("-" * 50)
        print("SUMMARY:")
        print(f"Total unique poems: {len(unique_poems)}")
        
        # Print source statistics
        print(f"\nPoems by source file:")
        total_from_sources = 0
        for source_file, count in source_counts.items():
            print(f"  - {source_file}: {count} poems")
            total_from_sources += count
    else:
        print("No poems found to combine!")

if __name__ == "__main__":
    main()
