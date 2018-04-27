import pickle
import matplotlib.pyplot as plt
import time
import numpy as np
import math
from collections import defaultdict
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
import string
import csv



def pickle_in(filename):
    with open(filename, 'rb') as pickleFile:
        return pickle.load(pickleFile)

def pickle_out(filename, object_to_dump):
    with open(filename, 'wb') as pickleFile:
        pickle.dump(object_to_dump, pickleFile)
        pickleFile.close()


def get_vocab(documents):
    vocab = []
    for title in documents:
        for word in title.split():
            if word not in vocab:
                vocab.append(word)
    vocab.sort()
    return vocab

def prepare_documents(documents):
    result = []
    for title in documents:
        translator = str.maketrans('', '', string.punctuation)
        title = title.translate(translator)
        title = title.lower()
        result.append(title)
    return result

def print_top_words(model, feature_names, n_top_words):
    topic_words = {}
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
        topic_words[topic_idx] = (" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))

    print()
    return topic_words
###############################################################

# remove_unupdated_posts()
subs = ['Historians','Academia','Anthropology','Culinary','Men','Science','SocialScience','Women']

for sub in subs:
    posts = pickle_in('processed_'+sub)
    # print(posts)
    documents = posts[:,0]

    documents = prepare_documents(documents)
    documents_not_vectorized = documents


    vocab = get_vocab(documents)


    vectorizer = CountVectorizer(stop_words='english')
    vectorizer = vectorizer.fit(vocab)
    documents = vectorizer.transform(documents).toarray()

    num_topics = 10
    lda = LatentDirichletAllocation(n_components=num_topics, total_samples=len(documents), learning_method='batch', max_iter=300, random_state=42)

    doc_topics_distributions = lda.fit(documents)

    tf_feature_names = vectorizer.get_feature_names()
    topic_words = print_top_words(lda, tf_feature_names, 3)

    result = []
    for topic_num in range(num_topics):
        top3_words = topic_words[topic_num].split()
        karma = []
        for doc_num, title in enumerate(documents_not_vectorized):
            if top3_words[0] in title or top3_words[1] in title or top3_words[2] in title:
                karma.append(int(posts[doc_num][4]))    #get the karma
        # print(np.mean(karma))
        result.append([top3_words[0],top3_words[1],top3_words[2], np.mean(karma)])

    with open('topic_modeling_'+sub+'.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['word1', 'word2', 'word3', 'mean karma'])
        for idx in range(len(result)):
            writer.writerow(result[idx])
        




