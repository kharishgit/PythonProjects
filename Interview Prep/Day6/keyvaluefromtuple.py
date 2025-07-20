def group_values(pairs):
    d={}
    for i in pairs:
        if i[0] in d.keys():
            d[i[0]].append(i[1])
        else:
            d[i[0]]=[i[1]]
    return d

print(group_values([(1, 10), (2, 20), (1, 30), (3, 40), (2, 50)]))




def group_values(pairs):
    groups = {}
    for key, value in pairs:
        if key in groups:
            groups[key].append(value)
        else:
            groups[key] = [value]
    return groups

# Test cases
print(group_values([(1, 10), (2, 20), (1, 30), (3, 40), (2, 50)]))  # Output: {1: [10, 30], 2: [20, 50], 3: [40]}
print(group_values([(1, 5), (1, 5), (2, 10)]))                       # Output: {1: [5, 5], 2: [10]}
print(group_values([]))                                               # Output: {}