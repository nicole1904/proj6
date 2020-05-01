import pandas as pd
import numpy as np

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

class Recommendation:

    def __init__(self, recommender, user_id, top_similar_users=15): #top_similar_users = max number of matches
        self.recomm = recommender
        self.user_id = user_id
        self.similar_users = None
        self.top_similar_users = top_similar_users

        # validate that user exists in data
        try:
            self.selected_user = self.recomm.data.loc[self.user_id]
        except KeyError:
            raise AttributeError("User %s not found in data" % self.user_id)

    def _find_similar_users(self):
        denominator_selected_user = np.sqrt(sum([np.square(x) for x in self.selected_user]))
        similar_users = []
        i = 0
        for user in self.recomm.data.values:
            if self.recomm.data.index[i] == self.selected_user.name:
                #skip selected user
                i += 1
                continue
            numerator = [x*y for x, y in zip(self.selected_user, user)]
            denominator_user = np.sqrt(sum([np.square(x) for x in user]))
            similarity = sum(numerator) / (denominator_selected_user * denominator_user)
            similar_users.append((self.recomm.data.index[i], similarity))
            i += 1

        similar_users.sort(key=lambda r: r[1], reverse=True)

        self.similar_users = similar_users[:self.top_similar_users]

        #debug
        print("Similar users:")
        print(self.similar_users)

    def _recommend_movies(self): #movie recommender
        pass

    def recommend(self):
        #debug
        print("Recommending movies for user: %s" % self.user_id)
        self._find_similar_users()
        self._recommend_movies()
