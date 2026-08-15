text = "python programming"


print("1.", text[0:6])


print("2.", text[7:])


if "java" not in text.lower():
    new_text = text.replace(" ", " java ")
else:
    new_text = text

print("3.", new_text)


print("4. Length =", len(new_text))


print("5. Number of words =", len(new_text.split()))


capitalized_text = new_text.title()
print("6.", capitalized_text)


no_space_text = capitalized_text.replace(" ", "")
print("7.", no_space_text)


print("8.")
print("Frequency of A =", capitalized_text.count("A"))
print("Frequency of P =", capitalized_text.count("P"))
print("Frequency of R =", capitalized_text.count("R"))
print("Frequency of M =", capitalized_text.count("M"))