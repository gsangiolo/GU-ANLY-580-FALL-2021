# ANLY-580 Assignment 2

This assignment covers concepts from ANLY-580 Module 2 dealing with distributional semantics.

To submit this assignment, either enter your answers directly in the `assignments/assignment-2.md` using markdown syntax, or upload a separate file containing your solutions, for example `assignments/assignment-2-solutions.pdf`.

#
**Format**: take home, open note/wiki

**Due dates**:
 
 - Section I: Oct 10
 - Section II: Oct 06

**Grade**: 10% (100 pts)

**Your name**:

**Your NET ID**:

#
## Problems


1. (10 pts) Describe why the BOW feature representation limits our ability to model human language. What aspect of language, and specifically word meaning, does BOW ignore?
The major limitation of BoW is its lack of Part of Speech understanding, which can add layers of complexity relating to sentiment, context, and even homonyms (such as lead vs lead -- "I sunk like a lead balloon" vs "I lead the balloon animals through the store"). Similarly, BoW also ignores word order, which can also affect contextual meanings and distinguish between words. BoW representations are also sparse (many 0 terms) due to the fact that features continually grow when new data points (sentences) are added. This is generally a big issue in text processing, although vectorized processing algorithms like BERT or Word2Vec avoid this issue to a degree. 

2. (20 pts) The word2vec language modeling approach was perhaps the first successful method to learn meaningful word representations. Answer these questions:

    (a) How does word2vec assign/measure similarity between two words?
    Word2Vec generally uses cosine distance or the dot product to measure the similarity of words. 

    (b) When $N$ is large, what computational bottle neck arises in word2vec that requires us to change the algorithm?
    Word2Vec relies on the ability to perform a LOT of tensor computations to perform training, read context of the words, etc. This causes it to scale poorly for large corpuses, even with large GPU processing capabilities.
    
    *Note: we did not tweak the algorithm in the in-class demo, but did mention it during the lecture/demo?*


3. (20 pts) Why are the inner product and cosine similarity used to measure similarity and not euclidean distance?
Euclidean distance is not always useful for similarity because it relies heavily on amplitudes (or frequencies) of each word/feature. For example, a document with the word "banana" x1000 might be very far (in Euclidean measure) from a shorter document that references "plantains" x20, but less far from a document with the word "orange" x1200. This can be mitigated via preprocessing and normalization, but in the end Euclidean distances are still affected by document length. Cosine and Dot products, however, mitigate this by measuring the angles between two vectors. It is also important to note that most vectorizing algorithms are written under the assumption that cosine distance/angles between vectors are the measure for similarity, and so those measures better represent the aim of the training (perhaps someone has/will write a model that assumes a Euclidean distance between similar words/texts, in which case that measure will be more useful).


4. (50 pts) Write a Python program to compute the trigram ($n=3$) probabilities of the following Dr. Suess corpus:

    *Hint: See Jurafsky & Martin Chp. 3 for bigram estimation from a similar corpus*

    ```
    <s> I am Sam </s>
    <s> Sam I am </s>
    <s> I am Sam </s>
    <s> I do not like green eggs and Sam </s>
    ```

5. (10 pts Extra Credit) Recall from Lecture 03 that the principle of maximum likelihood makes two qualifying assumptions for any dataset/model combination:

    - all examples are drawn from the same distribution

    - all examples are drawn independently

    Which of these qualifying assumptions does word2vec break (many other LMs do too, as it turns)?

    *Hint: We make the Markov assumption in language modeling out of necessity; this doesn't mean that it reflects reality!*
