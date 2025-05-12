class Movies:

    def __init__(self, movie_name, hero, director):

        self.movie_name=movie_name 
        self.hero = hero
        self.director=  director

    def movies_list(self):  

        print({"movie name ": self.movie_name, 
               "hero name ": self.hero, 
               "Director name ": self.director})
 
list=[]

while True:

    movie = input("Enter a movie name:")

    hero = input("enter a hero name:")

    director = input("enter a director name:")

    movie_object =  Movies(movie, hero, director)


    list.append(movie_object) 
    print('movie uploaded succesfully.........1')

    option= input('Do you want to add more movie??')

    if option.lower() == 'no':
        break

print('-'*7)
for Movies in list:
    Movies.movies_list()