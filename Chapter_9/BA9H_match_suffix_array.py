import operator

def suffix_array(string):
    suffix_arr = dict()
    for i in range(len(string)):
        temp = string[i:]
        suffix_arr[temp] = i
    suffix_arr = dict(sorted(suffix_arr.items(), key=operator.itemgetter(0)))
    return list(suffix_arr.values())

def pattern_match(text, suffix_arr, patterns):
    result = []
    for pattern in patterns:
        for i in suffix_arr:
            if text[i: i + len(pattern)] == pattern:
                result.append(i)
                continue
            if len(text[i:]) > len(pattern) and text[i:] > pattern:
                break
    result.sort()
    return result

if __name__ == "__main__":
    text = "AATCGGGTTCAATCGGGGT"
    patterns = ["ATCG", "GGGT"]
    # with open("rosalind_ba9h.txt", "r") as f:
    #     lines = f.read().splitlines()
    #     text = lines[0]
    #     patterns = []
    #     for i in range(1, len(lines)):
    #         patterns.append(lines[i])
    suffix_arr = suffix_array(text)
    result = pattern_match(text, suffix_arr, patterns)
    for x in result:
        print(x, end=" ")
