"""DATASTRUCTURES"""
'List-ordered allow duplicate values'
states=["Andhra Pradesh", "Arunachal Pradesh", "Assam",
        "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
        "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala",
        "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
        "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
        "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
        "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu",
        "Lakshadweep", "Delhi", "Puducherry"]
print(states[3])

list_comp=[states[x]for x in range(len(states))]
print(list_comp)
"""nested lists"""
engineering=["civil","mechanical","electronics","computers","datascience","artificial intelligence"]
core=["civil","mechanical","electronics"]
tech=["computers","datascience","artificial intelligence"]
nested=[core,tech]
print(nested[0])
print(nested[1])
print(nested[1][2])
