from faker import Faker

fake = Faker()


def generate_email():
    return fake.email()


def generate_name():
    return fake.name()


def generate_password(length=10):
    return fake.password(length=length)
