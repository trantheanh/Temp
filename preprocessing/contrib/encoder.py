import numpy as np
import tensorflow as tf


# CONVERT LABEL ENCODE TO ONE HOT ENCODE 1d -> 2d
def to_one_hot_categorical(label_encode, n_label):
    assert len(label_encode.shape) == 1, 'label encode must be 1d numpy array'

    n_example = len(label_encode)

    result = np.zeros((n_example, n_label))
    result[np.arange(n_example), label_encode] = 1

    return result


def to_one_hot_multi_label(label_encode, n_label):
    assert len(label_encode.shape) == 2, 'label encode must be 2d numpy array'

    n_example = len(label_encode)

    result = np.zeros((n_example, n_label))

    return


def to_one_hot(label_encode, n_label, is_multi_label):
    assert type(label_encode).__module__ == np.__name__, 'type of label encode must be numpy array'
    assert n_label > 0, 'n_label must be greater than 0'
    assert n_label > np.max(label_encode), 'label index can not be greater than n_label'

    if is_multi_label:
        to_one_hot_multi_label(label_encode, n_label)
    else:
        to_one_hot_categorical(label_encode, n_label)

    return

input = np.array([1,2,4,0,2,1])
print(to_one_hot(input, 5))