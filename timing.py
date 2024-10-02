timing = """
me 2:45
everyone is an expert 5:00
normal classroom  3:50
bloom: 6:40
mbl-> master teaching  1:00
filling of a pail: 4:30
growth mindset
framework 
fundamental code concepts
protege effect 
guild 
homework
end 
"""

import re


def get_timing(timing):
    timing = timing.split("\n")
    timing = [re.sub(r"\d+:\d+", "", t) for t in timing]
    timing = [t for t in timing if t]
    return timing


timing = """
me 2:45
normal classroom  3:50
bloom: 6:40
mbl-> master teaching  1:00
filling of a pail: 4:30
growth mindset: 5:00
framework: 3:30
assess 7:00
protege effect 1:38
guild 3:27
homework
end 
"""

import re


def get_timing():
    lines = timing.split("\n")
    total_seconds = 0
    for line in lines:
        if not line:
            continue
        found = re.search(r"(\d+):(\d+)", line)
        if found:
            minutes, seconds = found.groups()
            total_seconds += int(minutes) * 60 + int(seconds)
    minutes, seconds = divmod(total_seconds, 60)
    print(f"Total time: {minutes}:{seconds}")


get_timing()
