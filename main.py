'''
What does main.py do?

It creates movie objects using data structures. Once done, they are processed by open_movies_page function.
The function returns html file for view.
'''

import media
import fresh_tomatoes as ft

toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys',
                        'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc',
                        '130 Minutes')

avartar = media.Movie('Avartar',
                      'A story of a marine on another planet',
                      'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
                      'https://www.youtube.com/watch?v=d1_JBMrrYw8',
                      '120 Minutes')


spirited_away = media.Movie("Spirited Away",
                            "A story of a girl entering into the world of spirits",
                            "https://upload.wikimedia.org/wikipedia/en/3/30/Spirited_Away_poster.JPG",
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk",
                            "140 Minutes")

movies = [toy_story,avartar,spirited_away]


ft.open_movies_page(movies)

