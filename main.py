from movies import movies, display_movies
from booking import book_ticket, display_bookings
from display import show_menu
while True:
    show_menu()
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        display_movies()
    elif (choice == 2):
        book_ticket(movies)
    elif (choice == 3):
        display_bookings()
    elif (choice == 4):
        print("Exiting the program. Thank you for using the Movie Reservation System!")
        break
    else:
        print("Invalid choice. Please try again.")
