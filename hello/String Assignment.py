
def generate_ticket(airline, source, destination, no_of_passengers):
    ticket_number_list = []
    #counter = 0
    ticket_number = 100

    short_source = source[0:3]
    short_dest = destination[0:3]

    for x in range(no_of_passengers):
        
        ticket_number += 1
        name = input("Please enter name of passanger "+str(x+1)+" =")
        final = airline+":"+short_source+":"+short_dest+":"+str(ticket_number)+":"+name

        ticket_number_list.append(final)

    
    return ticket_number_list



print(generate_ticket("AI", "India", "USA", 4))

