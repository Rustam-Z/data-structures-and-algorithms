import os
import math

class Carriage:
    def __init__(self):
	self.carriageType = ""
	self.carriageID = ""
	self.carriagePlaces = 0

    def set_data(self, carriageType, carriageID, carriagePlaces):
	self.carriageType = carriageType
	self.carriageID = carriageID
	self.carriagePlaces = carriagePlaces

    def get_carriage_type(self):
	return self.carriageType

    def get_carriage_id(self):
	return self.carriageID

    def get_carriage_places(self):
	return self.carriagePlaces

    def display(self):
	print("------------------------------------------ ")
	print("  Carriage: " + self.carriageID + " " + self.carriageType + " " + str(self.carriagePlaces))

class Passenger:
    def __init__(self):
	self.firstName = ""
	self.lastName = ""
	self.ticketType = ""

    def set_data(self, firstName, lastName, ticketType):
	self.firstName = firstName
	self.lastName = lastName
	self.ticketType = ticketType

    def get_first_name(self):
	return self.firstName

    def get_last_name(self):
	return self.lastName

    def get_ticket_type(self):
	return self.ticketType

    def display(self):
	print("------------------------------------------ ")
	print("  Passenger: " + self.firstName + " " + self.lastName + " " + self.ticketType)

class Node:
    def __init__(self, data):
	self.data = data
	self.next = None

class LinkedList:
    def __init__(self):
	self.head = None

    def add_node(self, val):
	new_node = Node(val)
	if self.head is None:
	    self.head = new_node
	else:
	    temp = self.head
	    while temp.next is not None:
		temp = temp.next
	    temp.next = new_node

    def delete_first(self):
	if self.head is None:
	    print("Passengers list is empty!")
	else:
	    self.head = self.head.next

    def get_first_element(self):
	if self.head is not None:
	    return self.head.data

    def display(self):
	if self.head is None:
	    print("Passengers list is empty!")
	else:
	    temp = self.head
	    while temp is not None:
		print(temp.data, end=" --> ")
		temp = temp.next
	    print()

class Stack:
    def __init__(self):
	self.front = None

    def push(self, d):
	new_node = Node(d)
	if self.front is None:
	    new_node.next = None
	else:
	    new_node.next = self.front
	    self.front = new_node

    def pop(self):
	if self.front is None:
	    print("UNDERFLOW")
	else:
	    self.front = self.front.next

    def print_stack(self):
	if self.front is None:
	    print("UNDERFLOW!")
	else:
	    temp = self.front
	    while temp is not None:
		print(temp.data, end=" <--> ")
		temp = temp.next
	    print()

def main():
    Num = 1
    numOfBusiness = 0
    numOfFirst = 0
    businessSpace = 0
    firstSpace = 0

    while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	print("\t*** MENU *** ")
	print("1. Add passenger to file")
	print("2. Read passengers info from file")
	print("3. Add carriage to file")
	print("4. Read carriage info from file")
	print("5. Show linked lists")
	choice = input("Your choice:")

	if choice == "1":
	    print("\n------------------------------------------ ")
	    with open("Passengers", "ab") as out:
		print("\t*** Add Passenger ***")
		firstName = input("Enter first name: ")
		lastName = input("Enter last name: ")
		ticketType = input("Enter ticket type (Business/First): ")
		Psg = Passenger()
		Psg.set_data(firstName, lastName, ticketType)
		out.write(Psg.__dict__.encode())
	    input("\nPress Enter to continue...")

	elif choice == "2":
	    print("\n\t*** Passenger File *** ")
	    Num = 1
	    with open("Passengers", "rb") as f:
		while True:
		    data = f.read(1024)
		    if not data:
			break
		    else:
			Psg = Passenger()
			Psg.__dict__.update(eval(data))
			print(f"{Num}.")
			Psg.display()
			Num += 1
	    input("\nPress Enter to continue...")

	elif choice == "3":
	    print("\n------------------------------------------ ")
	    with open("Carriages", "ab") as out:
		print("\t*** Add Carriages ***")
		carriageID = input("Enter ID: ")
		carriageType = input("Enter type (Business/First): ")
		carriagePlaces = int(input("Enter number of seats: "))
		Crg = Carriage()
		Crg.set_data(carriageType, carriageID, carriagePlaces)
		out.write(Crg.__dict__.encode())
	    input("\nPress Enter to continue...")

	elif choice == "4":
	    print("\n\t*** Carriage File ***")
	    Num = 1
	    with open("Carriages", "rb") as f:
		while True:
		    data = f.read(1024)
		    if not data:
			break
		    else:
			Crg = Carriage()
			Crg.__dict__.update(eval(data))
			print(f"{Num}.")
			Crg.display()
			Num += 1
	    input("\nPress Enter to continue...")

	elif choice == "5":
	    listBusiness = LinkedList()
	    listFirst = LinkedList()
	    numOfBusiness = 0
	    numOfFirst = 0
	    with open("Passengers", "rb") as f:
		while True:
		    data = f.read(1024)
		    if not data:
			break
		    else:
			Psg = Passenger()
			Psg.__dict__.update(eval(data))
			if Psg.get_ticket_type() == "Business":
			    listBusiness.add_node(Num)
			    numOfBusiness += 1
			else:
			    listFirst.add_node(Num)
			    numOfFirst += 1
			Num += 1
	    print("\n------------------------------------------ ")
	    print("Linked List - 'Business class'")
	    listBusiness.display()
	    print("Overall 'Business':", numOfBusiness, "\n")
	    print("Linked List - 'First class'")
	    listFirst.display()
	    print("Overall 'First':", numOfFirst)
	    print("------------------------------------------ ")
	    businessSpace = 0
	    firstSpace = 0
	    with open("Carriages", "rb") as f:
		while True:
		    data = f.read(1024)
		    if not data:
			break
		    else:
			Crg = Carriage()
			Crg.__dict__.update(eval(data))
			if Crg.get_carriage_type() == "Business":
			    businessSpace += Crg.get_carriage_places()
			else:
			    firstSpace += Crg.get_carriage_places()
			  businessSpace = math.ceil(businessSpace / 2)
		    firstSpace = math.ceil(firstSpace / 2)
		    while True:
			print("\n\t*** INNER MENU *** ")
			print("1. Distribute 'Business class'")
			print("2. Distribute 'First class'")
			print("0. Go back ")
			inner_choice = input("Your choice:")
			if inner_choice == "1":
			    stackBusiness = Stack()
			    print("\n------------------------------------------ ")
			    print("Number of free spaces (Business):", businessSpace)
			    if numOfBusiness <= businessSpace:
				for i in range(numOfBusiness):
				    distributedPerson = listBusiness.get_first_element()
				    stackBusiness.push(distributedPerson)
				    listBusiness.delete_first()
				    businessSpace -= 1
				print("Free spaces left:", businessSpace)
			    elif numOfBusiness > businessSpace:
				for i in range(businessSpace):
				    distributedPerson = listBusiness.get_first_element()
				    stackBusiness.push(distributedPerson)
				    listBusiness.delete_first()
				print("You need", numOfBusiness - businessSpace, "more spaces!")
			    else:
				print("You need", numOfBusiness - businessSpace, "free spaces!")
			    print("Business class passengers list: ", end="")
			    stackBusiness.print_stack()
			    input("\nPress Enter to continue...")
			elif inner_choice == "2":
			    stackFirst = Stack()
			    print("\n------------------------------------------ ")
			    print("Number of free spaces (First):", firstSpace)
			    if numOfFirst <= firstSpace:
				for i in range(numOfFirst):
				    distributedPerson = listFirst.get_first_element()
				    stackFirst.push(distributedPerson)
				    listFirst.delete_first()
				    firstSpace -= 1
				print("Free spaces left:", firstSpace)
			    elif numOfFirst > firstSpace:
				for i in range(firstSpace):
				    distributedPerson = listFirst.get_first_element()
				    stackFirst.push(distributedPerson)
				    listFirst.delete_first()
				print("You need", numOfFirst - firstSpace, "more spaces!")
			    else:
				print("You need", numOfFirst - firstSpace, "spaces!")
			    print("First class passengers list: ", end="")
			    stackFirst.print_stack()
			    input("\nPress Enter to continue...")
			elif inner_choice == "0":
			    break
			else:
			    print("\nYour choice is not available in the menu!")
			    input("\nPress Enter to continue...")
	    else:
		print("\nYour choice is not available in the menu!")
		input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
