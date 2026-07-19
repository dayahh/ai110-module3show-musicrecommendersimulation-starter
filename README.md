# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend
In a real world system, data can be pulled from a user or data can be pulled from a user and their com,unity to determine what to reccomend next.

You can include a simple diagram or bullet list if helpful.
Song will have these values:
  - what's in the data: id,title,artist,genre,mood,energy,tempo_bpm,valence,danceability,acousticness
 - what's being scored id,title,artist,genre,mood,energy,
The info the UserProfile stores is 
 - favorite: genre, mood, and target energy
 - likes_acoustic is stored but not used because I don't think it's important
The Recommender computes a score for each song by
It adds up points for how well a song matches the user:
 - +points if the song's genre matches favorite_genre
 - +2 points if the song's mood matches favorite_mood
 - +points the CLOSER the song's energy is to target_energy
       (score = 1 − |target_energy − song.energy|, so closer = higher)
Each part can be weighted so some features matter more than others.

Every song gets a score, then the list is sorted from highest to lowest,
and the top 5 are shared as the recommendations.

My Algorithm Recipe: For each song, the recommender starts at a score of 0 and adds points for how well the song matches the user. It adds 2 points if the mood matches the user's favorite mood, 1 point if the genre matches the user's favorite genre, and up to 1 point for energy based on how close the song's energy is to the user's target (using 1 − |target_energy − song.energy|, so a closer match scores higher). I weight mood above genre because matching how the listener currently feels matters more to me than matching a genre label, so genre acts as a secondary tie-breaker. Once every song has a score, the recommender sorts them from highest to lowest and returns the top 5. This means a chill lofi song can rank above an intense pop song for a chill-mood user, even when pop is the user's favorite genre.

Quick map of the data flow to plan your logic: Input (User Prefs) → Process (The Loop: Judging every individual song in the CSV using your scoring logic) → Output (The Ranking: Top K Recommendations).
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```
Top recommendations:

Sunrise City - Score: 3.98
Because: genre match (+2.0), mood match (+1.0), energy close (+0.98)

Gym Hero - Score: 2.87
Because: genre match (+2.0), energy close (+0.87)

Rooftop Lights - Score: 1.96
Because: mood match (+1.0), energy close (+0.96)

Concrete Sunrise - Score: 1.00
Because: energy close (+1.00)

Night Drive Loop - Score: 0.95
Because: energy close (+0.95)

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this
At the start of the project, when testing a user profile for super pop and happy, the scorer ranked intense rock above chill lofi for a happy-pop user because energy was the only tiebreaker.


