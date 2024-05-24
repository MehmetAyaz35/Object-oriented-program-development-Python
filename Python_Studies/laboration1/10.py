names = ["tobias", "andreas", "tove"]
new_names = []


# "in" is the keyword used to specify the list (or any other iterable) over which the loop should iterate.
# So "in" here acts as a join between the keyword "for", the temporary variable name "name" and the list to be iterated over, "names". 
# It allows the loop to go through each element of the list one by one and perform the specified action for each element.

for name in names:
    if "to" in name:   #Here "in" is inside a condition .This condition determines whether the name should be included in the new list based on whether the name contains the string "to".
        new_names.append(name)