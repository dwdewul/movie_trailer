import fresh_tomatoes
from media import Movie


def main():

    fight_club = Movie("Fight Club",
                       "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                       "https://www.youtube.com/watch?v=SUXWAEX2jlg")

    martian = Movie("The Martian",
                    "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                    "https://www.youtube.com/watch?v=lQqhfq87FgY")

    toy_story3 = Movie("Toy Story 3",
                       "https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg",
                       "https://www.youtube.com/watch?v=JcpWXaA2qeg")

    matrix = Movie("The Matrix",
                   "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                   "https://www.youtube.com/watch?v=vKQi3bBA1y8")

    no_country = Movie("No Country For Old Men",
                       "https://upload.wikimedia.org/wikipedia/en/8/8b/No_Country_for_Old_Men_poster.jpg",
                       "https://www.youtube.com/watch?v=YBqmKSAHc6w")

    movies = [fight_club, martian, toy_story3, matrix, no_country]

    fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
    main()
