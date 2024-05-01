# Task 1: Customer Service Ticket Tracker 
# --- Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.
#--- Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).

# Problem Statement: implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.

def display_tickets():
    status= int(input("1.) display all tickets, 2.) display closed tickets, 3.) display open tickets "))
    if status == 1:
        for key,value in service_tickets.items():
            print(key)
            print('----------')
            print(value)
    elif status == 2:
        for key,value in service_tickets.items():
            if value['Status'] == 'closed':
                print(key)
                print('---------')
                print(value)
    elif status == 3:
        for key,value in service_tickets.items():
            if value['Status'] == 'open':
                print(key)
                print('---------')
                print(value)

def update_status():
    for key in service_tickets.keys():
        print(key)
    ticket_id = input("Enter the ticket ID you want to update: ")
    new_status = input("Enter the new status (open/closed): ")

    if ticket_id in service_tickets:
        service_tickets[ticket_id]['Status'] = new_status
        print("Ticket status updated successfully!")
    else:
        print("Ticket ID not found.")

    def add_new_ticket():
        ticket_id = input("Enter the ticket ID: ")
        customer_name = input("Enter the customer name: ")
        issue_description = input("Enter the issue description: ")
        status = "open"

        if ticket_id not in service_tickets:
            service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": status}
            print("New ticket added successfully!")
        else:
            print("Ticket ID already exists. Please choose a different ID.")
            return



while True:

    service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
    }

    print('''Hello and welocome to the Customer Service Ticket Tracker!
          The Customer Service Ticket Tracker can
          
          1: Open a new service ticket.
          
          2: Update the status of an existing ticket
          
          3: Display all tickets or filter by status
          
          4: Exit''')
    
    option = int(input("which of the above operations would you like to preform? pleace choose (1, 2, 3 or 4): "))

    if option == 1:
        pass
    if option == 2:
        update_status()
    if option == 3:
        display_tickets()
    if option == 4:
         print('now exiting')
         break

