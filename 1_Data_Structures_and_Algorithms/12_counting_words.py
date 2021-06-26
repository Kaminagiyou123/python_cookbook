from collections import Counter
words = [
       'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
       'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
       'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
       'my', 'eyes', "you're", 'under'
]
 
word_count=Counter(words)
print(word_count)
top_three=word_count.most_common(3)
print(top_three)
print(word_count['nose'])

# manually increment the count manually
more_words=['why','are','you','not','looking','in','my','eyes']
for word in more_words:
 word_count[word]+=1


word_count.update(more_words)
print(word_count)

a=Counter(words)
b=Counter(more_words)
print(a+b)