#Task 1: 
# Restaurant Menu Update 
# You are given an initial structure of a restaurant menu stored in a nested dictionary. 
# Your task is to update this menu based on given instructions
#  - Add a new category called "Beverages" with at least two items.
#- Update the price of "Steak" to 17.99.
#- Remove "Bruschetta" from "Starters". 
"""
def add_category(menu, category): #Menu is entire dict. Category is sub dict
  if category not in menu:
    menu[category] = []
    print(f"New menu category: {menu} has been added!")
  else:
    print(f"Category already exists!")

def newly_add_item(menu, category, item): ##item are the keys/values within the category the sub dict
  if category in menu:
    if item not in menu[category]:
      menu[category].append(item)
      print(F"You have added {item} to {category}")
    else:
      print(f"Item: {item} already exists within {category}")
  else:
    print(f"{category} does not exist within the menu")

def update_menu(menu, category, item):
  menu.update({category: item})
  print(f"{category} was updated and the cost is now {item}")

def delete_item(menu, category, item):
  if category in menu:
    if item in menu[category]:
      menu[category].pop(item)
      print(f"{item} has been removed!")
    else:
      print(f"{item} is already deleted!")
  else:
    print(f"{item} does not exist!")

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

add_category(restaurant_menu, "Berverages") #Beverages is its own dict
delete_item(restaurant_menu, "Starters", "Bruschetta") #starters is its own dict
update_menu(restaurant_menu, "steak", "17.99") #Steak is a key and price is the value
#print(restaurant_menu)
"""
#Task 2
# Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops 
# by creating a system to track customer service tickets.

def add_ticket(ticket_data_base, ticket_number, customer_name, issues, status):
  if ticket_number not in ticket_data_base:
    ticket_data_base[ticket_number] = {"Customer": customer_name, "Issue": issues, "Status": status}
    print(f"Ticket Number: {ticket_number}\nAdded to Ticket Data Base!")
  else:
    print(f"{ticket_number} already exists! Please enter a new ticket that does not exist in the data base!")

def update_ticket(ticket_data_base, ticket_number, status):
  if ticket_number in ticket_data_base:
    ticket_data_base[ticket_number]["Status"] = status
    print(f"The following {ticket_number} has been updated to {status}")
  else:
    print(f"{ticket_number} was not found!")

def view_tickets(ticket_data_base):
  for ticket_number, details in ticket_data_base.items():
    print(f"{ticket_number}, Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details["Status"]}")
    #This print MUST ALLIGN WITH ORIGINAL DICT
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

#service_tickets2 = {} note: test dict for trial and error, comparing

while True:
  print("\nWelcome to Ticket Data Base Inc.")
  print("1: Add Ticket\n2: Update Ticket Status\n3: View Ticket Data Base\n4: Exit Program")
  choice = input("Enter selection: ")

  if choice == "1":
    ticketNum = input("Please type ticket number (e.g. Ticket001):  ")
    customer = input("Enter customer's first name: ")
    issue = input("Enter indicated issue: ")
    current_status = input("What is the current status [(open/closed)]: ")
    add_ticket(service_tickets, ticketNum, customer, issue, current_status)

  elif choice == "2":
    ticketNum = input("Please enter existing ticket number to be updated: ")
    status = input("Please enter updated status (open/closed): ")
    update_ticket(service_tickets, ticketNum, status)
  
  elif choice == "3":
    view_tickets(service_tickets) #dict must be called from here

  elif choice == "4":
    print("Exiting system. Good day!")
    break
  else:
    print("Invalid entry")