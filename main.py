import datetime
import copy
import nltk

from utils import *
from tfidf import TF_IFD
from doc2vec import doc2vec


def EX_3_2_code():
    folders = ['docs\\Clean_Punctuation\\', 'docs\\prefSufWord\\', 'docs\\rootWord\\']
    query_str = "חמאס מלחמה עזה טיל טילים פלסטינים"

    for folder in folders:
        docs_files = [folder + file for file in os.listdir(folder) if file.endswith(".txt")]
        docs = read_files(docs_files)
        # We used these lines to print and copy the results to README.
        print_README_table(TF_IFD(copy.deepcopy(docs), False, query_str)[:10])
        print_README_table(doc2vec(copy.deepcopy(docs), query_str, n_top_docs=10, is_matrix_mode=False))


def EX_4_code():

    folders = ['docs\\Clean_Punctuation\\', 'docs\\prefSufWord\\', 'docs\\rootWord\\']
    groups = [['A', 'B'], ['A', 'C'], ['C', 'B']]
    max_vector_size = 1000

    for group in groups:
        groups_docs = {}
        for symbol in group:
            groups_docs = {**groups_docs, **{str(doc): symbol for doc in my_csv(symbol)}}

        for folder in folders:
            folder_name = folder.split('\\')[1]
            group_name = ', '.join(group)
            print(group_name, ":", folder_name)
            docs_locations = [folder + file for file in os.listdir(folder) if get_file_name(file) in groups_docs.keys()]
            docs = read_files(docs_locations)
            # tf_idf = TF_IFD(copy.deepcopy(docs), max_bow_size=max_vector_size)
            # tf_idf['symbol'] = tf_idf.apply(lambda row: groups_docs[get_file_name(row.doc_name)], axis=1)
            # tf_idf = tf_idf.drop('doc_name', axis=1)
            # real_symbols = tf_idf.loc[:, "symbol"]
            # plot_kmeans(tf_idf.drop('symbol', axis=1), real_symbols, 'TF-IDF ' + folder_name + ' ' + group_name)
            doc2vec_vector, doc_locations = doc2vec(copy.deepcopy(docs))
            real_symbols = [groups_docs[get_file_name(doc)] for doc in doc_locations]
            plot_kmeans(doc2vec_vector, real_symbols,  'DOC2VEC ' + folder_name + ' ' + group_name)


def main():
    """
    Since this exercise is an exercise that is divided into several sub-exercises, we built a separate function for
    each sub-exercise.
    """
    EX_3_2_code()
    # EX_4_code()


if __name__ == '__main__':
    nltk.download('punkt')
    # my_unzip(my_csv())    # for the first time you need to unzip all docs.
    tic = datetime.datetime.now()
    main()
    toc = datetime.datetime.now()
    print('\n' + str((toc - tic)))
