import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
import json
 
def read_article(filename):
    f = open(filename, "r")
    filedata = f.readlines()
    article = filedata[0].split(". ")
    sentences = []

    for sentence in article:
        # print(sentence)
        # data cleaning for removinf words
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    #removing last full stop
    sentences.pop()
    
    return sentences

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
 
    all_words = list(set(sent1 + sent2))
 
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
 
    # build the vector for the first sentence
    for word in sent1:
        if word in stopwords:
            continue
        vector1[all_words.index(word)] += 1
 
    # build the vector for the second sentence
    for word in sent2:
        if word in stopwords:
            continue
        vector2[all_words.index(word)] += 1
 
    return 1 - cosine_distance(vector1, vector2)
 
def build_similarity_matrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i == j:
                continue
            similarity_matrix[i][j] = sentence_similarity(
                    sentences[i], sentences[j], stop_words)

    return similarity_matrix


def generate_summary(filename, top_n=5):
    #loading stop wordds
    stop_words = stopwords.words('english')
    summarize_text = []

    sentences =  read_article(filename)

    
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)
    # Return a graph from numpy matrix.
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    '''PageRank computes a ranking of the nodes in the graph G based on the 
    structure of the incoming links. It was originally designed
    as an algorithm to rank web pages'''
    scores = nx.pagerank(sentence_similarity_graph)


    ranked_sentence = sorted(((scores[i],s) for i, s in enumerate(sentences)), reverse=True)    
    print("Indexes of top ranked_sentence order are ")



    for i in range(top_n):
        summarize_text.append(" ".join(ranked_sentence[i][1]))


    summ = ". ".join(summarize_text)

    data = {
        'id': '1',
        'summary': summ,
        'link': ''
    }

    with open('hack.json', 'w') as file:
        json.dump(data, file)   


    # with open('summary.txt', 'w') as file:
    #     print("Summarize Text: \n", ". ".join(summarize_text), file=file)

