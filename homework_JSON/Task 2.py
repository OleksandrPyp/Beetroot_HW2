#Task 2 Phone book
import json


class Phonebook:
    def __init__(self, file_name):
        self.name = file_name
        try:
            with open(f"{file_name}.json", "r") as f:
                self.new_input = json.load(f)
        except FileNotFoundError:
            self.new_input = list()

    def saver(self):
        with open(f"{self.name}.json", "w") as f:
            json.dump(self.new_input, f)

    def adder(self, fname, lname, p_number, city, state):
        self.new_input.append({
            "first name": fname,
            "last name": lname,
            "phone number": p_number,
            "city": city,
            "state": state
        })

    def search(self, k, v):
        return [i for i in self.new_input if i.get(k) == v]

    def deleter(self, p_number):
        for i in self.new_input:
            if i["phone number"] == p_number:
                self.new_input.remove(i)
                print("The number was deleted")
            else:
                print("Can not find the number")

    def updater(self, p_number, k, v):
        for i in self.new_input:
            if i["phone number"] == p_number:
                i[k] = v
                print("The contact is updated")
            else:
                print("Entry is not found")

    #def display_all(self):
        #for i in range(len(Phonebook)):
            #print(Phonebook[i])

    def menu(self):
        while True:
            print("Choose an option:")
            print("1. Add new entry")
            print("2. Search by first name")
            print("3. Search by last name")
            print("4. Search by full name")
            print("5. Search by telephone number")
            print("6. Search by city or state")
            print("7. Delete a record for a given telephone number")
            print("8. Update a record for a given telephone number")
            print("0. Exit")

            query = input("Please select an option: ")

            if query == "1":
                fname = input("Enter the first name: ")
                lname = input("Enter the last name: ")
                p_number = input("Enter the phone number: ")
                city = input("Enter the city: ")
                state = input("Enter the state: ")
                self.adder(fname, lname, p_number, city, state)
                print("Contact was added")
            elif query == "2":
                fname = input("Enter the first name: ")
                result = self.search("first name", fname)
                if result:
                    for e in result:
                        print(e)
                else:
                    print("No entries found")
            elif query == "3":
                lname = input("Enter the last name: ")
                result = self.search("last name", lname)
                if result:
                    for e in result:
                        print(e)
                else:
                    print("No entries found")
            elif query == "4":
                full_name = input("Enter the full name: ")
                x = full_name.split()
                result = self.search("last name", x[1])
                if result:
                    for e in result:
                        print(e)
                else:
                    print("No entries found")
            elif query == "5":
                p_number = input("Enter the phone number: ")
                result = self.search("phone number", p_number)
                if result:
                    for e in result:
                        print(e)
                else:
                    print("No entries found")
            elif query == "6":
                city_state = input("Enter city or state: ")
                result = self.search("city", city_state) + self.search("state", city_state)
                if result:
                    for e in result:
                        print(e)
                else:
                    print("No entries found")
            elif query == "7":
                p_number = input("Enter the phone number: ")
                self.deleter(p_number)
            elif query == "8":
                p_number = input("Enter the phone number: ")
                k = input("Enter the field you want to update: ")
                v = input("Enter the new value for the field: ")
                self.updater(p_number, k, v)
            elif query == "0":
                self.saver()
                print("Data was saved, closing the program")
                break
            else:
                print("Wrong input, try again. ")

