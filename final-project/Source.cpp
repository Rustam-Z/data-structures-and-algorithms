#include <conio.h> // need to use getch()
#include <fstream> // file handling
#include <iostream> // input/output handling
#define Line "------------------------------------------ " // macros

using namespace std;

class Carriage {
protected:
	// identifires
	string carriageType, carriageID;
	int carriagePlaces;
public:
	// setting data (name and tell)
	void setData(string carriageType, string carriageID, int carriagePlaces) {
		this->carriageType = carriageType;
		this->carriageID = carriageID;
		this->carriagePlaces = carriagePlaces;
	}

	// get name and tell
	string getCarriageType() { return carriageType; }
	string getCarriageID() { return carriageID; }
	int getCarriagePlace() { return carriagePlaces; }

	// displaying name and tell
	void Display() {
		cout << Line << endl;
		cout << "  Carriage: " << carriageID << " " << carriageType << " " << carriagePlaces << endl;
	}
};

class Passenger {
protected:
	// identifires
	string firstName, lastName, ticketType;
public:
	// setting data 
	void setData(string firstName, string lastName, string ticketType) {
		this->firstName = firstName;
		this->lastName = lastName;
		this->ticketType = ticketType;
	}

	// get name and tell
	string getFirstName() { return firstName; }
	string getFamilyName() { return lastName; }
	string getTicketType() { return ticketType; }

	// displaying name and tell
	void Display() {
		cout << Line << endl;
		cout << "  Passenger: " << firstName << " " << lastName << " " << ticketType << endl;
	}
};

// Node needed to implement linked list
class Node {
public:
	int data;
	Node* next;
};

// Linked list implementation
class LinkedList {
public:
	LinkedList() { // constructor
		head = NULL;
	}

	~LinkedList() {}; // destructor
	void addNode(int val);
	void deleteFirst();
	int getFirstElement();
	void display();

private:
	Node* head;
};

int LinkedList::getFirstElement() {
	return head->data;
}

// Add a node in linked list
void LinkedList::addNode(int val) {
	// function to add node to a list
	Node* newnode = new Node();
	newnode->data = val;
	newnode->next = NULL;
	if (head == NULL) {
		head = newnode;
	}
	else {
		Node* temp = head; // head is not NULL
		while (temp->next != NULL) {
			temp = temp->next; // go to end of list
		}
		temp->next = newnode; // linking to newnode
	}
}

// Displays the linked list
void LinkedList::display() {
	if (head == NULL) {
		cout << "Passengers list is empty!" << endl;
	}
	else {
		Node* temp = head;
		while (temp != NULL) {
			cout << temp->data << " --> ";
			temp = temp->next;
		}
		cout << endl;
	}
}

// Removing element from Linked list
void LinkedList::deleteFirst() {
	// if empty
	if (head == NULL)
		cout << "Passengers list is empty!" << endl;

	// delete the first element
	else {
		Node* temp = head;
		head = head->next;
		delete(temp);
	}
}

// Stack implementation
class Stack {
	Node* front;  // points to the head of list
public:
	Stack() {
		front = NULL;
	}
	
	void push(int); // push method to add data element
	void pop(); // pop method to remove data element
	void printStack();
};

// Inserting Data in Stack (Linked List)
void Stack::push(int d) {
	// creating a new node
	Node* temp;
	temp = new Node();
	
	temp->data = d; // setting data to it

	// add the node in front of list
	if (front == NULL)
		temp->next = NULL;
	else
		temp->next = front;
	front = temp;
}

// Removing Element from Stack (Linked List)
void Stack::pop() {
	// if empty
	if (front == NULL)
		cout << "UNDERFLOW";

	// delete the first element
	else {
		Node* temp = front;
		front = front->next;
		delete(temp);
	}
}

// Displays the linked list
void Stack::printStack() {
	if (front == NULL) {
		cout << "UNDERFLOW!";
	}
	else {
		Node* temp = front;
		while (temp != NULL) {
			cout << temp->data << " <--> ";
			temp = temp->next;
		}
		cout << endl;
	}
}

int main() {
	// identifires
	string firstName, lastName, ticketType, carriageType, carriageID; int carriagePlaces;
	int Num = 1;
	int numOfBusiness = 0, numOfFirst = 0;
	double businessSpace = 0, firstSpace = 0;

	// objects
	Passenger Psg;
	Carriage Crg;

	// start
	for (int i = 0; i < 1000; i++) { // loop for Menu
		system("cls");

		cout << "\t*** MENU *** " << endl;
		cout << "1. Add passenger to file" << endl;
		cout << "2. Read passengers info from file" << endl;
		cout << "3. Add carriage to file" << endl;
		cout << "4. Read carriage info from file" << endl;
		cout << "5. Show linked lists" << endl; // Sort and Divide Info which comes from File and will add to linked list
		cout << "Your choice:";

		switch (_getch()) {
		case 49: { // write to file a passenger
			cout << "\n" << Line << endl;
			ofstream out;
			out.open("Passengers", ios::binary | ios::app);

			cout << "\t*** Add Passenger ***" << endl;
			cout << "Enter first name: "; cin >> firstName;
			cout << "Enter last name: "; cin >> lastName;
			cout << "Enter ticket type (Business/First): "; cin >> ticketType;

			Psg.setData(firstName, lastName, ticketType);
			out.write((char*)&Psg, sizeof(Passenger));
			out.close();

			cout << endl;
			system("pause");
		}
			   break;

		case 50: { // read from file passengers
			cout << "\n\t*** Passenger File *** " << endl;

			ifstream in;
			in.open("Passengers", ios::binary);
			while (in.read((char*)&Psg, sizeof(Passenger))) {
				cout << Num << "." << endl;
				Psg.Display();
				Num++;
			}
			cout << Line << endl;
			Num = 1;
			in.close();

			cout << endl;
			system("pause");
		}
			   break;

		case 51: { // write to file carriages
			cout << "\n" << Line << endl;
			ofstream out;
			out.open("Carriages", ios::binary | ios::app);

			cout << "\t*** Add Carriages ***" << endl;
			cout << "Enter ID: "; cin >> carriageID;
			cout << "Enter type (Business/First): "; cin >> carriageType;
			cout << "Enter number of seets: "; cin >> carriagePlaces;

			Crg.setData(carriageType, carriageID, carriagePlaces);
			out.write((char*)&Crg, sizeof(Carriage));
			out.close();

			cout << endl;
			system("pause");
		}
			   break;

		case 52: { // read from file carriages
			cout << endl;
			cout << "\n\t*** Carriage File ***" << endl;
			ifstream in;
			in.open("Carriages", ios::binary);
			while (in.read((char*)&Crg, sizeof(Carriage))) {
				cout << Num << "." << endl;
				Crg.Display();
				Num++;
			}
			cout << Line << endl;
			Num = 1;
			in.close();

			cout << endl;
			system("pause");
		}
			   break;

		case 53: {
			// Sort Passengers into Linked Lists
			LinkedList* listBusiness = new LinkedList();
			LinkedList* listFirst = new LinkedList();
			numOfBusiness = 0;
			numOfFirst = 0;
			ifstream in;
			in.open("Passengers", ios::binary);
			while (in.read((char*)&Psg, sizeof(Passenger))) {
				if (Psg.getTicketType() == "Business") {
					listBusiness->addNode(Num);
					numOfBusiness++;
				}
				else {
					listFirst->addNode(Num);
					numOfFirst++;
				}
				Num++;
			}
			cout << endl << Line << endl;
			Num = 1;
			in.close();
			// ---------------------------------------
			cout << "Linked List - 'Business class'" << endl;
			listBusiness->display();
			cout << "Overall 'Business': " << numOfBusiness << endl << endl;

			cout << "Linked List - 'First class'" << endl;
			listFirst->display();
			cout << "Overall 'First': " << numOfFirst << endl;
		    // ---------------------------------------

			for (int j = 0; j < 100; j++) {
				cout << "\n\t*** INNER MENU *** " << endl;
				cout << "1. Distribute 'Business class'" << endl;
				cout << "2. Distribute 'First class'" << endl;
				cout << "0. Go back " << endl;
				cout << "Your choice:";

				businessSpace = 0;
				firstSpace = 0;

				ifstream in;
				in.open("Carriages", ios::binary);
				while (in.read((char*)&Crg, sizeof(Carriage))) {
					if (Crg.getCarriageType() == "Business") {
						businessSpace = businessSpace + Crg.getCarriagePlace();
					}
					else {
						firstSpace = firstSpace + Crg.getCarriagePlace();
					}
				}
				businessSpace = round(businessSpace / 2.0);
				firstSpace = round(firstSpace / 2.0);
				in.close();

				switch (_getch()) {
				case 49: { 
					// Distribute 'Business class'
					Stack* stackBusiness = new Stack();

					// Free spaces we have in business class
					cout << endl << Line << endl;
					cout << "Number of free spaces (Business): " << businessSpace << endl;

					if (numOfBusiness <= businessSpace) {
						// take the first element from list, PUSH() it to stack, delete that element
						for (int i = numOfBusiness; i > 0; i--) {
							int distributedPerson = listBusiness->getFirstElement();
							stackBusiness->push(distributedPerson);
							listBusiness->deleteFirst();
							businessSpace--;
						}
						// shows the number of free spaces
						cout << "Free spaces left: " << businessSpace << endl;
					}
					else if (numOfBusiness > businessSpace) {
						for (int i = businessSpace; i > 0; i--) {
							int distributedPerson = listBusiness->getFirstElement();
							stackBusiness->push(distributedPerson);
							listBusiness->deleteFirst();
						}
						cout << "You need " << numOfBusiness - businessSpace << " more spaces!" << endl;
					}
					else {
					// Overflow case
						cout << "You need " << numOfBusiness - businessSpace << " free spaces!"<< endl;
					}

					cout << "Business class passengers list: ";
					// listBusiness->display(); // displays old linked list
					stackBusiness->printStack(); // displays new stack

					cout << endl;
					system("pause");
				}
					   break;
				case 50: { // Distribute 'First class'
					Stack* stackFirst = new Stack();

					// Free spaces we have in first class
					cout << endl << Line << endl;
					cout << "Number of free spaces (Fist): " << firstSpace << endl;

					if (numOfFirst <= firstSpace) {
						// take the first element from list, PUSH() it to stack, delete that element
						for (int i = numOfFirst; i > 0; i--) {
							int distributedPerson = listFirst->getFirstElement();
							stackFirst->push(distributedPerson);
							listFirst->deleteFirst();
							firstSpace--;
						}
						// shows the number of free spaces
						cout << "Free spaces left: " << firstSpace << endl;
					}
					else if (numOfFirst > firstSpace) {
						for (int i = firstSpace; i > 0; i--) {
							int distributedPerson = listFirst->getFirstElement();
							stackFirst->push(distributedPerson);
							listFirst->deleteFirst();
						}
						cout << "You need " << numOfFirst - firstSpace << " more spaces!" << endl;
					}
					else {
						// Overflow case
						cout << "You need " << numOfFirst - firstSpace << " spaces!" << endl;
					}

					cout << "First class passengers list: ";
					stackFirst->printStack(); // displays new stack

					cout << endl;
					system("pause");
				}
					   break;
				case 48: { // go back
					j = 101;
				}
					   break;
				}
				
			} // inner menu

			cout << endl;
			// system("pause");
		}
			   break;

		default: {
			cout << "\n\nYour choice is not available in the menu!" << endl;
			cout << endl;
			system("pause");
		}
			   break;
		} // end of switch
	} // end of loop
	system("pause");
	return 0;
}