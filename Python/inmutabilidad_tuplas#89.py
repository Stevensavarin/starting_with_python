"""
nums_tuple = (1, 2, 3, 4, 5)
nums_tuple[0] = 5
"""
"""
info_tuple = ([1, 2, 3], {"uno": 1, "dos": 2}, (3, 2))
info_tuple[]
"""
info_tuple = ([1, 2, 3], {"uno": 1, "dos": 2}, (3, 2))
print(f"Tupla original: {info_tuple}")
info_tuple[0][1] = 99
print(f"Tupla [0][1]: {info_tuple} \n")

print(f"Tupla original: {info_tuple}")
info_tuple[1]["dos"] = 88
print(f"Tupla [1]['dos']: {info_tuple}")


