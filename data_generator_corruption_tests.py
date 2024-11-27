import os.path
from faker import Faker

fake = Faker('en_UK')

# Generate a list of 40 test addresses (20 originals, 20 updated originals)

# 20 original addresses

for n in range(20):
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

# 20 updated original addresses
for n in range(20):
    fake.seed_instance(n)
    name = fake.name()
    name_list = name.split()
    last_name = name_list[-1]
    fake.seed_instance(n+20)
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
