player1_name = input("Enter player 1 name: ")
player2_name = input("Enter player 2 name: ")
def remove_common_characters(name1, name2):
    common_chars = []
    for char in name1:
        if char not in name2:
            common_chars.append(char)
    name1 = ''
    for char in name1:
        if char not in common_chars:
            name1 += char
    name2 = ''
    for char in name2:
        if char not in common_chars:
            name2 += char
    return name1, name2
def get_flames_result(count):
    flames = ["F", "L", "A", "M", "E", "S"]
    index = (count - 1) % len(flames)
    return flames[index]

# Get input from the user


# Remove common characters
name1, name2 = remove_common_characters(player1_name, player2_name)

# Calculate the count of remaining characters
count = len(name1) + len(name2)

# Get the FLAMES result
result = get_flames_result(count)

# Define relationship status dictionary
relationship_status = {
    "F": "Friends",
    "L": "Lovers",
    "A": "Affectionate",
    "M": "Marriage",
    "E": "Enemies",
    "S": "Sibling"
}

# Print the relationship status
if result in relationship_status:
    print("Relationship status:", relationship_status[result])
else:
    print("Unknown relationship status")
