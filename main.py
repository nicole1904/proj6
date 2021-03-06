import csv
import PySimpleGUI as sg
from recommender import Recommender, Recommendation

class Movie:
    def __init__(self, movie_id, year, name):
        self.movie_id = movie_id
        self.year = int(year)
        self.name = name

    def __str__(self):
        return "[MovieID %s] %s (%s)" % (self.movie_id, self.name, self.year)

class Movies:
    def __init__(self):
        self.movies = {}

    def load_movies(self, file_location):
        with open(file_location, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                movie_id = row[0]
                self.movies[movie_id] = Movie(movie_id, *row[1:])

    def get_movie(self, movie_id):
        if movie_id in self.movies:
            return self.movies[movie_id]
        return None

class Application:

    MOVIE_RATINGS_FILE = "data.csv"
    MOVIE_LIST_FILE = "movie_titles.csv"

    def __init__(self):
        self.window = None
        self.recommender = None
        self.movies = None

    def _load_data(self):
         self.recommender = Recommender()
         self.recommender.load_data(self.MOVIE_RATINGS_FILE)

         self.movies = Movies()
         self.movies.load_movies(self.MOVIE_LIST_FILE)

    def _show_result(self, user_id):
        self.window["-OUTPUT-"].update("")
        try:
            r = Recommendation(self.recommender, user_id)
            recommended_movies = r.recommend()
            rows = ["Recommended movies for user %s:" % user_id, "=" * 40]
            for movie_id, _ in recommended_movies:
                movie = self.movies.get_movie(movie_id)
                if movie is None:
                    rows.append("[MovieID %s] (movie not found in movie list)" % movie_id)
                else:
                    rows.append(str(movie))
            self.window["-OUTPUT-"].update("\n".join(rows))

        except AttributeError as e:
            print(e)
            sg.popup("ERROR", "User %s not found in review list" % user_id)
        except Exception as e:
            print("ERROR: %s" % e)
            sg.popup("Recommendation failed. Invalid data format.")
            raise e

    def run(self):
        layout = [
            [sg.Text("Enter user_id: "), sg.InputText(), sg.Button('OK')],
            [sg.MLine(size=(60, 10), key="-OUTPUT-")],
        ]
        self.window = sg.Window("Recommender", layout)

        try:
            self._load_data()
        except FileNotFoundError:
            sg.popup("ERROR", "Movie titles file '%s' or movie ratings file '%s' not found!" % (
            self.MOVIE_LIST_FILE, self.MOVIE_RATINGS_FILE))
            self.window.close()
            exit(1)
        except Exception:
            sg.popup("ERROR", "Loading failed. Please check input files.")
            self.window.close()
            exit(1)

        while True:
            event, values = self.window.read()
            if event is None:
                break

            if event == "OK":
                self._show_result(values[0])

        self.window.close()


def main():
    Application().run()


if __name__ == '__main__':
    main()
else:
    print("ERROR: Try running from main")