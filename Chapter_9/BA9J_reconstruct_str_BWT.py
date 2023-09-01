def BWT_to_text(string):
    rotation_table = ['']*len(string)

    for i in range(len(string)):
        for j in range(len(string)):
            rotation_table[j] = string[j] + rotation_table[j]
        rotation_table = sorted(rotation_table)
    
    result = ''
    for s in rotation_table:
        if s[-1] == "$":
            result = s
            break
    return result

if __name__ == "__main__":
    BWT = 'ard$rcaaaabb'
    reverse_BWT = BWT[::-1]
    # with open('rosalind_ba9j.txt', 'r') as f:
    #     BWT = f.read().strip()
    print(reverse_BWT)
    print(BWT_to_text(reverse_BWT))