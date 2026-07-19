import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file and returns a list of dictionaries.

    Numeric columns are converted from strings to numbers so they can be
    used in math later:
      - id          -> int
      - tempo_bpm   -> int
      - energy, valence, danceability, acousticness -> float
    Text columns (title, artist, genre, mood) stay as strings.

    Required by src/main.py
    """
    int_fields = {"id", "tempo_bpm"}
    float_fields = {"energy", "valence", "danceability", "acousticness"}

    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song: Dict = {}
            for key, value in row.items():
                if key in int_fields:
                    song[key] = int(value)
                elif key in float_fields:
                    song[key] = float(value)
                else:
                    song[key] = value
            songs.append(song)
    return songs

# --- Algorithm Recipe weights (tune these to change how the recommender behaves) ---
GENRE_WEIGHT = 1.0   # exact genre match
MOOD_WEIGHT = 2.0    # exact mood match (weighted higher — mood matters most)
ENERGY_WEIGHT = 1.0  # how close the song's energy is to the user's target


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences using the Algorithm Recipe:

      1. GENRE  : +GENRE_WEIGHT if song.genre == user's favorite genre
      2. MOOD   : +MOOD_WEIGHT  if song.mood  == user's favorite mood
      3. ENERGY : + ENERGY_WEIGHT * (1 - |target_energy - song.energy|)
                  (the closer the energy, the more points; max = ENERGY_WEIGHT)

    Returns a tuple of (score, reasons), where reasons is a human-readable list
    like ["genre match (+2.0)", "energy close (+0.90)"] so the user can
    understand WHY a song was recommended.

    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons: List[str] = []

    # 1. Genre: exact match
    if song["genre"] == user_prefs["genre"]:
        score += GENRE_WEIGHT
        reasons.append(f"genre match (+{GENRE_WEIGHT:.1f})")

    # 2. Mood: exact match
    if song["mood"] == user_prefs["mood"]:
        score += MOOD_WEIGHT
        reasons.append(f"mood match (+{MOOD_WEIGHT:.1f})")

    # 3. Energy: reward closeness to the user's target energy
    energy_distance = abs(user_prefs["energy"] - song["energy"])
    energy_points = ENERGY_WEIGHT * (1 - energy_distance)
    score += energy_points
    reasons.append(f"energy close (+{energy_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Ranks the whole catalog and returns the top k recommendations.

    Steps:
      1. SCORE  : run score_song() as the "judge" on every song.
      2. RANK   : sort all songs from highest score to lowest.
      3. TRIM   : keep only the top k.

    Each result is a tuple of (song, score, explanation), where explanation
    is the song's reasons joined into a readable string.

    Required by src/main.py
    """
    # 1. Score every song, packaging each as (song, score, explanation).
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored.append((song, score, explanation))

    # 2. Sort by score, highest first.
    scored.sort(key=lambda item: item[1], reverse=True)

    # 3. Return the top k.
    return scored[:k]
