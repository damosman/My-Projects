# Write a program to remove the duplicates in a list


# method 1

new_duplicate = []
duplicate = [8, 6, 4, 9, 10, 7, 12, 7, 30, 7]
for i in range(len(duplicate)):
    if duplicate[i] not in new_duplicate:
        new_duplicate.append(duplicate[i])
print(new_duplicate)

# method 2
duplicate = [8, 6, 4, 9, 10, 7, 12, 7, 30, 7]

final_list = list(dict.fromkeys(duplicate))

print(final_list)