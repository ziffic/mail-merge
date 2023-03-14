with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()

for name in names:
    current_name = str(name.replace("\n", ""))
    new_letter = str(letter.replace("[name]", current_name))
    with open(f"Output/ReadyToSend/letter_to_{current_name}.txt", mode="w") as data:
        data.write(new_letter)
