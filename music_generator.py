import random
import time

notes = ["C", "D", "E", "F", "G", "A", "B"]
durations = [0.25, 0.5, 1.0]

print("🎵 AI Music Generator 🎵\n")
melody = []

for i in range(10):
    note = random.choice(notes)
    duration = random.choice(durations)
    melody.append((note, duration))
    print(f"Playing note {note} for {duration} seconds...")
    time.sleep(duration)

print("\nGenerated melody pattern:")
for note, duration in melody:
    print(f"{note} ({duration}s)")