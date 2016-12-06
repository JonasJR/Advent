from operator import itemgetter
import heapq
import collections

input = open("data.txt", 'r').readlines()

def least_common_values(array, to_find=None):
    counter = collections.Counter(array)
    if to_find is None:
        return sorted(counter.items(), key=itemgetter(1), reverse=False)
    return heapq.nsmallest(to_find, counter.items(), key=itemgetter(1))

def main():
    col1 = ""
    col2 = ""
    col3 = ""
    col4 = ""
    col5 = ""
    col6 = ""
    col7 = ""
    col8 = ""
    for line in input:
        col1 += line[0]
        col2 += line[1]
        col3 += line[2]
        col4 += line[3]
        col5 += line[4]
        col6 += line[5]
        col7 += line[6]
        col8 += line[7]

    result = collections.Counter(col1).most_common(1)[0] + collections.Counter(col2).most_common(1)[0] + collections.Counter(col3).most_common(1)[0] + collections.Counter(col4).most_common(1)[0] + collections.Counter(col5).most_common(1)[0] + collections.Counter(col6).most_common(1)[0] + collections.Counter(col7).most_common(1)[0] + collections.Counter(col8).most_common(1)[0]
    result2 = least_common_values(col1,1) + least_common_values(col2,1) + least_common_values(col3,1) + least_common_values(col4,1) + least_common_values(col5,1) + least_common_values(col6,1) + least_common_values(col7,1) + least_common_values(col8,1)
    print(result2)
main()
