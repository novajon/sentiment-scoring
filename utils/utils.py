import datetime
import pandas as pd
import numpy as np
import pickle
import copy

def save_data (dictionary, file_identifier, include_timestamp = True):

    now = datetime.datetime.now()
    prefix = ""
    if include_timestamp: prefix = now.strftime("%Y%m%d_%H%M_")
    with open('data/output/' + prefix + file_identifier + '.pickle', 'wb') as handle:
        pickle.dump(dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_data (file_name):
    with open('data/output/' + file_name + ".pickle", 'rb') as handle:
        return pickle.load(handle)

def apply_on_dict(data_input_, func, params = []):
    data_input = copy.deepcopy(data_input_)
    for key in data_input.keys():
        l_text = data_input[key]
        temp = func(l_text, *params)
        data_input[key] = temp
    return data_input

def apply_on_list(list_data, func, params = []):
    for index, row in list_data.iteritems():
        list_data.loc[index] = func(row, *params)
    return list_data

def apply_on_real_list(list_data, func, params = []):
    for row_ind in range(len(list_data)):
        list_data[row_ind] = func(list_data[row_ind], *params)
    return list_data

def count_data (data_review): return {key: np.array([len(l) for l in text]) for text,key in zip(data_review.values(),data_review.keys())}

def plot_words(data_count):
    fig, axes = plt.subplots(2,2)
    for i in range(4):
        axes[int(i/2), i%2].plot(data_count[source_name[i]])
        axes[int(i/2), i%2].set_title(source_name[i])
        axes[int(i/2), i%2].set_ylabel("Number of words")
        axes[int(i/2), i%2].set_xlabel("Entry #")
    fig.tight_layout()
    plt.show()