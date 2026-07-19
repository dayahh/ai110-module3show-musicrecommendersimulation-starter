# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

- Users create a test profile
- Profile is judged based off my algo
- Mood is heavily weighed, so reccs are based off that mostly

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

Different types of users:
A. Chill-but-hyped
- genre=lofi, mood=chill, energy=0.95
OUTPUT
USER WANTS: high energy (0.95), but mood=chill + genre=lofi (both low-energy)
------------------------------------------------------------------------
 3.47  Midnight Coding      energy=0.42  [genre match (+1.0), mood match (+2.0), energy close (+0.47)]
 3.40  Library Rain         energy=0.35  [genre match (+1.0), mood match (+2.0), energy close (+0.40)]
 2.33  Spacewalk Thoughts   energy=0.28  [mood match (+2.0), energy close (+0.33)]
 1.45  Focus Flow           energy=0.40  [genre match (+1.0), energy close (+0.45)]
 1.00  Neon Overdrive       energy=0.95  [energy close (+1.00)]

B. Ghost mood
- genre=pop, mood=triumphant, energy=0.8
PROFILE B - GHOST MOOD: mood=triumphant does not exist in the catalog
------------------------------------------------------------------------
 1.98  Sunrise City         energy=0.82  [genre match (+1.0), energy close (+0.98)]
 1.87  Gym Hero             energy=0.93  [genre match (+1.0), energy close (+0.87)]
 1.00  Concrete Sunrise     energy=0.80  [energy close (+1.00)]
 0.96  Rooftop Lights       energy=0.76  [energy close (+0.96)]
 0.95  Night Drive Loop     energy=0.75  [energy close (+0.95)]

D. Impossible energy
- energy=2.0
PROFILE D - IMPOSSIBLE ENERGY: energy=2.0 (out of valid 0-1 range)
------------------------------------------------------------------------
 2.82  Sunrise City         energy=0.82  [genre match (+1.0), mood match (+2.0), energy close (+-0.18)]
 1.76  Rooftop Lights       energy=0.76  [mood match (+2.0), energy close (+-0.24)]
 0.93  Gym Hero             energy=0.93  [genre match (+1.0), energy close (+-0.07)]
-0.02  Iron Verdict         energy=0.98  [energy close (+-0.02)]
-0.05  Neon Overdrive       energy=0.95  [energy close (+-0.05)]

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

- **Tiny catalog:** Only 19 songs, and most genres have just one song, so niche
  tastes get few real matches.
- **Only three features:** It uses genre, mood, and energy only — it ignores
  tempo, danceability, and acousticness, and has no idea about lyrics or language.
- **Exact matches only:** "indie pop" gets no credit toward "pop," and "euphoric"
  none toward "happy," so it can't recognize similar-but-not-identical taste.
- **Energy favors average tastes:** Users wanting very high or very low energy
  match fewer songs, so their results are weaker than a mid-energy user's.
- **Fills gaps with energy:** When genre and mood don't match, energy alone
  decides, so off-genre songs can sneak into the recommendations.

I explore these more in the model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this
At the start of the project, when testing a user profile for super pop and happy, the scorer ranked intense rock above chill lofi for a happy-pop user because energy was the only tiebreaker.

I think this practice helped me understand why my favorite music app YOutube Music works the way it does. It's own AI can judge a user based on interactions with mood and genre. for me perosnally I wanted to really judge a song and reccomend to my users about the moods they seem to be setting. I think mood defines everything about what you want to listen to so it's rated the hardest.

AI tools helped me understand the big and littlest pictures about how reccomendation tools worked. It overviewed how the Youtube music app operates and then I wrapped my project around those basics. AI also created test profiles and tested them against the algorithm I wanted to make sure the results I wanted to get were really happening


