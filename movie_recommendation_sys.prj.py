movies = {
    "Inception": "sci-fi thriller dream mind-bending",
    "Interstellar": "sci-fi space adventure time",
    "Titanic": "romance drama ship tragedy",
    "The Notebook": "romance drama love story",
    "Baahubali 2": "epic historical action drama war kingdom revenge",
    "Dangal": "sports wrestling drama family inspirational biopic",
    "Tumbbad": "horror thriller mythology fantasy greed curse",
    "Kantara": "action thriller folklore divine spirit culture",
}

def recommend_movie(movie_name):
    if movie_name not in movies:
        print("❌ Movie not found in database.")
        print("Available movies are:")
        for m in movies.keys():
            print("-", m)
        return
    
    base_tags = set(movies[movie_name].split())
    scores = {}
    
    for m, tags in movies.items():
        if m != movie_name:
            score = len(base_tags.intersection(set(tags.split())))
            scores[m] = score
    
    sorted_movies = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    print(f"\n🎬 Movies similar to '{movie_name}':")
    for m, s in sorted_movies[:3]:
        print(f"- {m} (Similarity Score: {s})")

# --- Ask user for input ---
print("Available movies:")
for m in movies.keys():
    print("-", m)

user_movie = input("\nEnter a movie name from above: ")
recommend_movie(user_movie)
