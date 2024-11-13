timing = """
bloom: 5:00
me 2:45
# normal classroom  3:50
mbl-> master teaching  1:00
filling of a pail: 4:30  
# growth mindset: 5:00
framework: 3:30
assess 7:00
# protege effect 1:38
guild 3:27
homework
"""

import re


def get_timing():
    lines = timing.split("\n")
    total_seconds = 0
    for line in lines:
        if not line:
            continue
        if line.startswith("#"):
            continue
        found = re.search(r"(\d+):(\d+)", line)
        if found:
            minutes, seconds = found.groups()
            total_seconds += int(minutes) * 60 + int(seconds)
    minutes, seconds = divmod(total_seconds, 60)
    print(f"Total time: {minutes}:{seconds}")


get_timing()
