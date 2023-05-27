class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        self.max_seats =seats

    
    def getStatus(self):
        print(f'The name of the  train is: {self.name}')
        # print(f'The seats available in the train are: {", ".join(map(str, range(1, self.seats+1)))}')
        print(f'(The seats available in the train are:{", ".join(map(str,(range(1,self.seats+1))))})')
    
    def fareInfo(self):
        print(f"The price of the ticket is: {self.fare} Taka")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats -1
        else:
            print("Sorry, we're full. Please try agin Later")

    def cancelTicket(self, seat_number):
        if seat_number <1 or seat_number>self.max_seats:
            print("Invalid sit number")
        else:
            print(f"Ticket for seat number {seat_number} has been cancelled!")
            self.seats += 1

    def buyCancelTicket(self,seat_number):
        if seat_number <1 or seat_number>self.max_seats:
            print("Invalid seat number")
        elif self.seats<self.max_seats:
             print(f"Ticket for seat number {seat_number} has been rebooked!")
             self.seats -= 1
        else:
            print("No available seats to rebook")
           

intercity = Train('Nilsagor Express: 765/766', 465, 10)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
intercity.fareInfo()
intercity.cancelTicket(298)
intercity.getStatus()
intercity.buyCancelTicket(298)
intercity.getStatus()



# class Train:
#     def __init__(self, name, fare, seats):
#         self.name = name
#         self.fare = fare
#         self.seats = seats
#         self.max_seats = seats
    
#     def getStatus(self):
#         print(f'The name of the train is: {self.name}')
#         print(f"The seats available in the train are: {self.seats}")
    
#     def fareInfo(self):
#         print(f"The price of the ticket is: {self.fare} Taka")

#     def bookTicket(self):
#         if self.seats > 0:
#             print(f"Your ticket has been booked! Your seat number is {self.seats}")
#             self.seats -= 1
#         else:
#             print("Sorry, we're full. Please try again later")

#     def cancelTicket(self, seat_number):
#         if seat_number < 1 or seat_number > self.max_seats:
#             print("Invalid seat number")
#         else:
#             print(f"Ticket for seat number {seat_number} has been cancelled!")
#             self.seats += 1

#     def buyCancelTicket(self, seat_number):
#         if seat_number < 1 or seat_number > self.max_seats:
#             print("Invalid seat number")
#         elif self.seats < self.max_seats:
#             print(f"Ticket for seat number {seat_number} has been rebooked!")
#             self.seats += 1
#         else:
#             print("No available seats to rebook.")


# intercity = Train('Nilsagor Express: 765/766', 465, 300)
# intercity.getStatus()
# intercity.bookTicket()
# intercity.bookTicket()
# intercity.bookTicket()
# intercity.getStatus()
# intercity.fareInfo()
# intercity.cancelTicket(298)
# intercity.getStatus()
# intercity.buyCancelTicket(298)
# intercity.getStatus()






