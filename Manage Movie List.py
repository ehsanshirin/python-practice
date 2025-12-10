class MovieList:
    def __init__(self):
        self.movies = []
        
    def add_movie(self, movie):
        self.movies.append(movie)
        print(f'{movie} added to list')
        
    def remove_movie(self, movie):
        if movie not in self.movies:
            print(f'{self.movie} not in list')
            return
        
        self.movies.remove(movie)
        print(f'{movie} remove from list')
        
    def show_list(self):
        print('List Movie: ')
        for i in self.movies:
            print(i)
            
m1 = MovieList()
m1.add_movie('Matrix')
m1.add_movie('Avengers')

m1.remove_movie('X-men')
m1.remove_movie('Matrix')

m1.show_list()