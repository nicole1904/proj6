import pandas as pd

class Recommender:

    def __init__(self):
        self.data = None

    def load_data(self, file_location):
        print("Loading data from file %s" % file_location)

        data = {"movie": [], "user": [], "rating": []}

        with open(file_location, "r") as f:
            current_movie_id = None
            while True:
                line = f.readline()
                if not line:
                    break
                line = line.strip()

                if line.endswith(":"):
                    # movie section start
                    # save movie ID for further use
                    current_movie_id = line[:-1]
                else:
                    if current_movie_id is None:
                        raise ValueError("Invalid CSV file. Movie ID is missing.")
                    user_id, rating, rating_data = line.split(",")
                    data["movie"].append(current_movie_id)
                    data["user"].append(user_id)
                    data["rating"].append(int(rating))

        dataframe = pd.DataFrame(data)
        self.data = dataframe.pivot_table(index='user', columns='movie', values='rating').fillna(0)
        print("Loading succesful")
