import os.path
from faker import Faker

fake = Faker('en_UK')

# Generate a list of 16 test addresses (8 originals, 4 updated originals, 4 unique updates)

# 8 original addresses

for n in range(8):
    fake.seed_instance(n)
    name = fake.name()
    name_list = name.split()
    last_name = name_list[-1]

    address = fake.address()
    contact = name + '\n' + address

# Add each one to a file named {lastname} within the originals folder

    directory = './target_directory/originals'
    file = f"{last_name}"
    path = os.path.join(directory, file)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    result = open(path, "a")
    result.write(contact)
    result.close()

# 4 updated original addresses
for n in range(4):
    fake.seed_instance(n)
    name = fake.name()
    name_list = name.split()
    last_name = name_list[-1]
    fake.seed_instance(n+5)
    address = fake.address()
    contact = name + '\n' + address

# Add each one to a file named {lastname} within the updates folder

    directory = './target_directory/updates'
    file = f"{last_name}"
    path = os.path.join(directory, file)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    result = open(path, "a")
    result.write(contact)
    result.close()


# 4 unique update addresses
for n in range(4):
    name = fake.name()
    name_list = name.split()
    last_name = name_list[-1]

    address = fake.address()
    contact = name + '\n' + address

# Add each one to a file named {lastname} within the updates folder

    directory = './target_directory/updates'
    file = f"{last_name}"
    path = os.path.join(directory, file)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    result = open(path, "a")
    result.write(contact)
    result.close()