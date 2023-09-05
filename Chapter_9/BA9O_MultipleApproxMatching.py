import operator

def burrows_wheeler_transform(text):
    patterns = []
    for i in range(len(text)):
        patterns.append(text[i:]+text[:i])
    patterns = sorted(patterns)
    bwt = ''.join([str[-1] for str in patterns])
    return bwt

def find_first_occurance(BWT):
    first_occurrences = dict()
    for idx, symbol in enumerate(sorted(BWT)):
        if symbol not in first_occurrences.keys():
            first_occurrences[symbol] = idx
    return first_occurrences

def create_check_point_array(BWT, C):
    symbol_list = list(set(BWT))
    check_point_array = dict()
    for idx in range(0, len(BWT), C):
        check_point_array[idx] = {}
        for symbol in symbol_list:
            check_point_array[idx][symbol] = BWT[:idx].count(symbol)
    return check_point_array

def create_suffix_array(string):
    suffix_arr = dict()
    for i in range(len(string)):
        temp = string[i:]
        suffix_arr[temp] = i
    suffix_arr = dict(sorted(suffix_arr.items(), key=operator.itemgetter(0)))
    return list(suffix_arr.values())

def create_partial_suffix_array(text, k):
    suffixes = []
    suffix_array = create_suffix_array(text)
    partial_suffix_array = {i: x for i, x in enumerate(suffix_array) if x % k == 0}
    return partial_suffix_array

def count_symbol(check_point_array, idx, last_column, symbol):
    values = [x for x in check_point_array.keys() if x <= idx]
    nearest_idx = min(values, key=lambda x: abs(x - idx))
    count = check_point_array[nearest_idx][symbol]
    count += last_column[nearest_idx:idx].count(symbol)
    return count

def multiple_pattern_matching(first_occurrences, last_column, pattern, check_point_array):
    top = 0
    bottom = len(last_column) - 1
    while top <= bottom:
        if len(pattern) != 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if symbol in last_column[top: bottom + 1]:
                top = first_occurrences[symbol] + count_symbol(check_point_array, top, last_column, symbol)
                bottom = first_occurrences[symbol] + count_symbol(check_point_array, bottom + 1, last_column, symbol) - 1
            else:
                return False, False
        else:
            return top, bottom

def pattern_to_seeds(pattern, d):
    minsize = len(pattern) // (d + 1)
    cut_points = list(range(0, len(pattern) - minsize + 1, minsize))
    cut_points.append(len(pattern))
    seeds = []
    offsets = []
    for i in range(1, len(cut_points)):
        seeds.append(pattern[cut_points[i - 1]: cut_points[i]])
        offsets.append(cut_points[i - 1])
    return seeds, offsets

def find_seed_positions(seed, first_occurrences, BWT, check_point_array, partial_suffix_array):
    seed_pos_list = []
    top, bottom = multiple_pattern_matching(first_occurrences, BWT, seed, check_point_array)
    if top:
        for idx in range(top, bottom + 1):
            to_add = 0
            while idx not in partial_suffix_array.keys():
                idx = first_occurrences[BWT[idx]] + count_symbol(check_point_array, 
                                                                 idx, BWT, BWT[idx])
                to_add += 1
            seed_pos_list.append(partial_suffix_array[idx] + to_add)
    return seed_pos_list

def find_all_approximate_occurance(text, pattern_list, d, C):
    BWT = burrows_wheeler_transform(text + '$')
    first_occurrences = find_first_occurance(BWT)

    check_point_array = create_check_point_array(BWT, C)
    partial_suffix_array = create_partial_suffix_array(text+'$', C)

    positions_list = []
    for pattern in pattern_list:
        seeds_list, offsets_list = pattern_to_seeds(pattern, d)
        pattern_pos_list = set()
        for candidate_seed, offset in zip(seeds_list, offsets_list):
            seed_pos_list = find_seed_positions(candidate_seed, first_occurrences, 
                                                BWT, check_point_array, 
                                                partial_suffix_array)
            for candidate_pos in seed_pos_list:
                pattern_position = candidate_pos - offset
                if pattern_position >= 0 and pattern_position + len(pattern) <= len(text):
                    approximate_match_flag = True
                    num_mismatch = 0
                    for idx, symbol in enumerate(pattern):
                        if symbol != text[pattern_position + idx]:
                            num_mismatch += 1
                            if num_mismatch > d:
                                approximate_match_flag = False
                                break
                    if approximate_match_flag:
                        pattern_pos_list.add(pattern_position)
        positions_list += list(pattern_pos_list)

    return sorted(positions_list)

if __name__ == "__main__":
    # text = "ACATGCTACTTT"
    # pattern_list = ['ATT', 'GCC', 'GCTA', 'TATT']
    # d = 1
    with open("rosalind_ba9o.txt", "r") as f:
        f = f.read().splitlines()
        text = f[0]
        pattern_list = [pattern for pattern in f[1].split(' ')]
        d = int(f[2])

    positions_list = find_all_approximate_occurance(text, pattern_list, d, C=100)
    print(' '.join(str(pos) for pos in positions_list))