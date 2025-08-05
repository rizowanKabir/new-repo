import random

# Lists of phrases
weather = [
    "a rainy day",
    "a cloudy morning",
    "a calm drizzle",
    "a sky full of silence",
    "a foggy walk",
    "a thunderstorm brewing"
]

mood = [
    "to find myself",
    "to discover a new path",
    "to spend some time alone",
    "to stay away from the noise",
    "to write my thoughts",
    "to simply breathe"
]

style = [
    "white tee mood on",
    "minimal look, maximum vibe",
    "rain-ready, mind steady",
    "simple look, deep thoughts",
    "layers and reflections",
    "walking with style, thinking with depth"
]

# Generate the caption
caption = f"Today feels like {random.choice(weather)}... the perfect time {random.choice(mood)}.\n{random.choice(style)} ☁️"

# Output the result
print(caption)
