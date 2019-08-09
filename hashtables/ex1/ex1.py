#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    hash_table = {}
    arr = []
    if len(weights) <= 1:
        return None

    for i in range(0, len(weights)):
        limit_weight_diff = limit - weights[i]
        hash_table[weights[i]] = limit_weight_diff

    for i in range(0, len(weights)):
        if limit - weights[i] in hash_table:
            arr.insert(0, i)

    return arr


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
