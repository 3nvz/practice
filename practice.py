class ContactInformation:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.country = None

person1 = ContactInformation("John", "Doe", "test@gmail.com", "123456789")
person2 = ContactInformation("Jane", "Doe", "test2@gmail.com", "987654321")