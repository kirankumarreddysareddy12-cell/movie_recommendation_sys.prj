---

# 🎬 Movie Recommendation System

A beginner-friendly "Python project" that recommends movies based on "tag similarity".
This project uses only "core Python" (no external libraries).

---

## 🚀 Features

* Stores movies and their "descriptive tags" in a dictionary.
* Uses "set intersection" to calculate similarity between movies.
* Recommends the "top 3 similar movies" to the one chosen by the user.
* Handles invalid input and shows all available movies.
* Beginner-friendly project to learn "dictionaries, sets, loops, conditionals, and functions".

---

## 🛠️ Technologies Used

* "Python 3" (no external libraries required)

---

## ▶️ How to Run

### pthon idel

```python idel
python movie_recommendation.py
```

### Windows (Command Prompt / PowerShell)

```cmd
python movie_recommendation.py
```

---

## 📖 Example Usage

```
Available movies:
- Inception
- Interstellar
- Titanic
- The Notebook
- Baahubali 2
- Dangal
- Tumbbad
- Kantara

Enter a movie name from above: Baahubali 2

🎬 Movies similar to 'Baahubali 2':
- Tumbbad (Similarity Score: 1)
- Dangal (Similarity Score: 1)
- Inception (Similarity Score: 0)
```

---

## 📂 Project Structure

```
movie-recommendation/
   ├── movie_recommendation.py   # main Python file
   └── README.md                 # project documentation
```

---

## 📝 Future Enhancements

* Add more movies with richer tags.
* Use "string similarity" for better matching.
* Upgrade with libraries like:

  * `sklearn` → cosine similarity for real ML-based recommendations.
  * `pandas` → handle large datasets.
  * Create a "GUI (Tkinter / PyQt)" for user-friendly interaction.

---

