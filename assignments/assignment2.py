import nltk
import math

corpus = ['I am Sam', 'Sam I am', 'I am Sam', 'I do not like green eggs and Sam']

extra_tokens = ['START', 'STOP']

#total_trigrams = []

trigram_counts = {}
bigram_counts = {}


for sentence in corpus:
    words = [extra_tokens[0]] + [extra_tokens[0]] + sentence.split() + [extra_tokens[1]]
    bigrams = tuple(nltk.bigrams(words))
    for bigram in bigrams:
        if bigram in bigram_counts.keys():
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1
    trigrams = tuple(nltk.trigrams(words))
    for trigram in trigrams:
        if trigram in trigram_counts.keys():
            trigram_counts[trigram] += 1
        else:
            trigram_counts[trigram] = 1

# Trigrams: based on occurrence of trigram / occurrence of starting bigram

trigram_probs = {}
trigram_log_probs = {}

for k in trigram_counts.keys():
    prob = trigram_counts[k] / float(bigram_counts[k[:2]])
    log_prob = math.log(prob, 2)
    trigram_probs[k] = prob
    trigram_log_probs[k] = log_prob

print('Trigram Probabilities:')
print(trigram_probs)
print('Log Probabilities:')
print(trigram_log_probs)
