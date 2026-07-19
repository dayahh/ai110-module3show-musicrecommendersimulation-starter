# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  
The Mood Matcher
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  


My recommender tries to predict which songs a listener will most enjoy based on
their stated taste. The user gives a simple profile — a favorite genre, a
favorite mood, and a target energy level — and the system suggests the songs
from the catalog that best match those preferences. It does this by scoring
every song for how well it fits the profile (genre match, mood match, and how
close the song's energy is to the target), then ranking them and returning the
top few as recommendations, each with a short reason explaining why it was
suggested.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.


Think of it like a matchmaker between a listener and songs.

**What features of each song are used**
Just three: its genre (like pop or lofi), its mood (like happy or chill), and
its energy (how hyped or mellow it is).

**What user preferences are considered**
The listener says their favorite genre, their favorite mood, and the energy
level they're in the mood for.

**How the model turns those into a score**
Every song earns points for matching the listener. It gets points if the genre
matches, more points if the mood matches (I made mood count the most), and
points for having an energy level close to what the listener wants — the closer
the energy, the more points. Add it all up and each song has a score. The songs
with the highest scores are the recommendations, and each comes with a short
reason like "mood match" so you know why it was picked.

**What changes I made from the starter logic**
The starter just returned the first few songs without really scoring them. I
added the real scoring rules, made energy reward closeness (not just "higher is
better"), gave mood the most weight, and added the plain-English reasons.


---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  
**How many songs are in the catalog**
19 songs total.

**What genres or moods are represented**
Genres include pop, lofi, rock, ambient, jazz, synthwave, indie pop, hip hop,
classical, reggae, metal, folk, edm, r&b, country, and blues.
Moods include happy, chill, intense, relaxed, moody, focused, energetic,
melancholy, uplifting, angry, nostalgic, euphoric, romantic, hopeful, and tense.

**Did you add or remove data**
I started with 10 songs and added 9 more to cover genres and moods that weren't
in the starter file (like hip hop, classical, metal, and blues), so the catalog
is more diverse. I didn't remove any.

**Are there parts of musical taste missing in the dataset**
Yes. It's still a tiny catalog, so most genres only have one song. It has no
lyrics or language info, no artist popularity, and each song only carries a few
features, so subtle differences in taste aren't captured. Some genres (lofi,
pop) are more represented than others, so niche tastes have fewer options.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

**User types for which it gives reasonable results**
It works best for users with a clear, common taste. The Chill Lofi profile was
the strongest — it returned Library Rain, Midnight Coding, and other calm,
low-energy songs, all a great fit. Pop and Rock profiles also gave sensible
top picks (Sunrise City for pop, Storm Runner for rock).

**Patterns the scoring captures correctly**
It correctly rewards closeness in energy instead of just picking the highest-
energy song, so a mellow user gets mellow songs and a hyped user gets hyped
ones. It also respects mood weighting — a "happy" user gets happy songs pushed
to the top even across different genres.

**Cases where recommendations matched my intuition**
When a song matched all three preferences (genre, mood, and energy), it clearly
rose to the top — like Sunrise City for the happy pop user. And opposite
profiles produced clearly different lists (chill lofi vs. intense rock had no
overlap), which is exactly what I'd expect.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---
**Features it does not consider**
The scorer only uses genre, mood, and energy. It ignores tempo_bpm, valence,
danceability, and acousticness, so two songs that feel very different can look
identical to the system. It also has no lyrics, language, or artist awareness.

**Genres or moods that are underrepresented**
The catalog is unbalanced: lofi (3) and pop (2) appear multiple times, while
most genres (classical, blues, metal, reggae, etc.) appear only once. A user
who likes a niche genre gets at most one genre match, so the rest of their
top-5 is filled with off-genre songs that only matched on energy.

**Cases where the system overfits to one preference**
Because genre and mood are exact-match only, the system reinforces exactly what
the user already picked and never explores near matches ("indie pop" gets no
credit toward "pop"; "euphoric" gets none toward "happy"). This creates a
filter bubble with no serendipity.

**Ways the scoring might unintentionally favor some users**
Energy is scored as closeness to the catalog's values, which cluster in the
middle. Users wanting average energy match many songs and get strong lists,
while users wanting very low or very high energy match almost nothing and get
near-random results. Also, when genre/mood don't match, energy becomes the only
signal, and tied scores are broken by CSV order — quietly favoring songs listed
earlier.

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---
**Which user profiles I tested**
- High-Energy Pop  -> {genre: pop,  mood: happy,   energy: 0.9}
- Chill Lofi       -> {genre: lofi, mood: chill,   energy: 0.35}
- Deep Intense Rock-> {genre: rock, mood: intense, energy: 0.9}

**What I looked for**
Whether each profile's top songs actually matched its genre/mood/energy, and
whether changing the profile visibly changed the ranking.

**Top 3 results per profile**
- High-Energy Pop:   Sunrise City (3.92), Rooftop Lights (2.86), Gym Hero (1.97)
- Chill Lofi:        Library Rain (4.00), Midnight Coding (3.93), Spacewalk Thoughts (2.93)
- Deep Intense Rock: Storm Runner (3.99), Gym Hero (2.97), Neon Overdrive (0.95)

**Pairwise comparisons (what changed and why it makes sense)**
- Pop vs. Lofi: The Pop profile surfaces bright, high-energy happy songs
  (Sunrise City, e=0.82), while the Lofi profile shifts entirely to low-energy
  chill tracks (Library Rain, e=0.35). This makes sense because their target
  energies (0.9 vs 0.35) pull toward opposite ends of the catalog.
- Pop vs. Rock: Both want high energy (0.9), so both reach for energetic songs,
  but mood splits them: Pop pulls "happy" songs and Rock pulls "intense" ones.
  Gym Hero (pop, intense) appears in BOTH top-3 — high in Rock (mood match) and
  lower in Pop (mood miss) — which shows mood weighting working correctly.
- Lofi vs. Rock: These are near-opposites and the output reflects it — Lofi's
  list is calm/acoustic and low-energy, Rock's is loud and high-energy, with no
  overlap. Good sign the profiles are testing distinct things.

**What surprised me**
For Deep Intense Rock, only Storm Runner truly fits; after that the list falls
off fast (Neon Overdrive at 0.95 is an off-genre EDM song kept only for energy).
This showed how a niche genre with few catalog songs forces energy-only filler.

**Simple tests I ran**
Ran all three profiles through recommend_songs() and compared their top-3 lists
side by side (output above).


## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---
An additional feature could be a back and forth conversation between the tool and the user. Maybe the user could provide feedback based off the results and the AI tool can tweak itself!

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I think this practice helped me understand why my favorite music app YOutube Music works the way it does. It's own AI can judge a user based on interactions with mood and genre. for me perosnally I wanted to really judge a song and reccomend to my users about the moods they seem to be setting. I think mood defines everything about what you want to listen to so it's rated the hardest.

AI tools helped me understand the big and littlest pictures about how reccomendation tools worked. It overviewed how the Youtube music app operates and then I wrapped my project around those basics. AI also created test profiles and tested them against the algorithm I wanted to make sure the results I wanted to get were really happening


