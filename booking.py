bookings = []
def book_ticket(movies):
    display_movies(movies)
    choice = int(input("Enter the your choice: "))
    if choice in movies:
        movie_name, price = movies[choice]
        tickets = int(input("Enter the number of tickets to be booked: "))
        total = tickets * price
        booking = {
            "movie": movie_name,
            "tickets": tickets,
            "total": total
        }
        bookings.append(booking)
        print("Booking successful!")
        print("Booking Details:")
        print("Movie : ",movie_name)
        print("Tickets : ",tickets)
        print("Total Price : ₹",total)
    else:
        print("Invalid choice.")
def display_bookings():
    print("-------------Your Bookings-------------")
    if len (bookings) == 0:
        print("No bookings found.")
    else:
        for i in range(len(bookings)):
            print("Booking", i + 1)
            print("Movie:", bookings[i]["movie"])
            print("Tickets:", bookings[i]["tickets"])
            print("Total Price: ₹", bookings[i]["total"])
def display_movies(movies):
    print("-------------Available Movies-------------")
    for number, details in movies.items():
        print(f"{number}. {details[0]} - {details[1]}")
