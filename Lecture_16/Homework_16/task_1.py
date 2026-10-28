class MovieTicket:
    cinema_name = "Rustaveli Cinema"
    total_tickets_sold = 0

    def __init__(self, movie_title, seat_number, price):
        self.movie_title = movie_title
        self.seat_number = seat_number
        self.price = price

        MovieTicket.total_tickets_sold += 1
        
    def display(self):
        print("=" * 40)
        print(f"Movie: {self.movie_title}")
        print(f"Seats: {self.seat_number}")
        print(f"Price: {self.price}")

movie_ticket1 = MovieTicket("Once in Vegas", 40, 18)
movie_ticket1.display()

movie_ticket2 = MovieTicket("Matilda", 20, 15)
movie_ticket2.display()

movie_ticket3 = MovieTicket("Graviti", 30, 17)
movie_ticket3.display()

print(f"Total number of sold tickets: {MovieTicket.total_tickets_sold}")
