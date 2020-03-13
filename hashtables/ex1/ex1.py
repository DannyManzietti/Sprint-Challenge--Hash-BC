#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,

                        hash_table_retrieve,)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for index in range(length):
        compare = hash_table_retrieve(ht, limit - weights[index])
        if compare is None:
            hash_table_insert(ht, weights[index], index)
        else:
            answer = (index, compare)
            return answer

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
