import nltk
from collections import Counter
from nltk.corpus import stopwords
import string

# Ensure you have the stopwords downloaded
nltk.download('stopwords')

def compute_word_frequencies(data):
    word_counter = Counter()
    for entry in data:
        words = entry['body'].lower().split()
        words = [word.strip(string.punctuation) for word in words]
        word_counter.update(words)
    return word_counter

def filter_stopwords(word_counter):
    stop_words = set(stopwords.words('english'))
    return Counter(word for word in word_counter if word not in stop_words and word)

def display_word_statistics(word_counter, filtered_counter, total_tokens):
    top_30_words = word_counter.most_common(30)
    top_30_filtered = filtered_counter.most_common(30)

    print(f'\n{"rank":<6}{"term":<12}{"freq.":<8}{"perc.":<8}')
    for i, (word, freq) in enumerate(top_30_words, 1):
        print(f'{i:<6}{word:<12}{freq:<8}{freq/total_tokens:.3f}')
    
    print(f'\n{"rank":<6}{"term":<12}{"freq.":<8}{"perc.":<8}')
    for i, (word, freq) in enumerate(top_30_filtered, 1):
        print(f'{i:<6}{word:<12}{freq:<8}{freq/total_tokens:.3f}')

def compute_statistics_part2(data, total_tokens):
    word_counter = compute_word_frequencies(data)
    filtered_counter = filter_stopwords(word_counter)
    display_word_statistics(word_counter, filtered_counter, total_tokens)

# Example usage:
compute_statistics_part2(data, total_tokens)
