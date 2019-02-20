from nltk .corpus import movie_reviews
documents = [(list(movie_reviews.words(feild)),category)
               for category in movie_reviews.categories()
               for field in movie_reviews.fields(category)]
random.shuffle(documents)  