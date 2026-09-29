movies = {
    1: ("Ramayana", 200),
    2: ("Godzilla Minus Zero",180),
    3: ("Varanasi", 200),
    4: ("Spirit",200),
    5: ("The Angry Birds Movie 3",180)
 }

def display_movies():
    print("\n-------------Available Movies-------------")
    for number, details in movies.items():
        print(f"{number}. {details[0]} - {details[1]}")