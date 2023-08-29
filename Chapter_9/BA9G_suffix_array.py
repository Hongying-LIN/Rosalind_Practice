import operator

def suffix_array(string):
    suffix_arr = dict()
    for i in range(len(string)):
        temp = string[i:]
        suffix_arr[temp] = i
    suffix_arr = dict(sorted(suffix_arr.items(), key = operator.itemgetter(0)))
    return suffix_arr.values()

if __name__ == "__main__":
    string = "AACGATAGCGGTAGA$"
    # with open("rosalind_ba9g.txt", "r") as f:
    #     string = f.readline().strip()
    result = suffix_array(string)
    print(", ".join(str(value) for value in result))