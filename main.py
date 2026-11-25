"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

The entry is a 100-word monologue spoken by a fantasy villain who is
secretly just very tired. The tiredness lives in the rhythm, the pauses
and the small deflections — the biting step he never fixed, the
prophecy heard three times already this week, the throne buried under
laundry, the goblin union's paperwork — never in a plain statement
that he is weary. The sting lands in the last line: the hero is
offered tea, not a duel.

How it runs
-----------
``python3 main.py`` writes the TEXT constant verbatim to
``/output/entry.txt`` (creating ``/output`` if needed) and exits 0.
There is no input, no network, and no templating: the file's bytes are
exactly the string above, so the judged text cannot drift between runs.

Verification
------------
The competition gate requires ``/output/entry.txt`` to be UTF-8 text of
1-600 characters, not only whitespace. This entry is exactly 100 words
and 554 characters, so it passes with room to spare. Re-verify with::

    python3 main.py
    sha256sum /output/entry.txt   # expect 3d9af217a667c03af88ebd68edf38c123fb879a155ec1f4761839517d9227104
    wc -w /output/entry.txt      # 100

Em dashes
---------
The two em dashes in the monologue are written in the source as the
``\u2014`` escape rather than a literal U+2014 character. This keeps the
source file plain ASCII, so no editor or tool can silently re-encode
them (e.g. as an en dash or a hyphen) and change the judged text.
"""

import os

TEXT = (
    "Come in, hero. Mind the step \u2014 the third one bites; I never did fix it. "
    "Yes, the sword, the prophecy. I've heard it three times this week, and it's "
    "only Thursday. The crown's on the table. The throne's... somewhere under the "
    "laundry. Take the crown. The kingdom comes with it: six provinces, two "
    "famines, and a goblin union that files grievances in triplicate. I conquered "
    "the world at twenty-three and I've been doing the paperwork ever since. Go "
    "on, strike me down. Or \u2014 better \u2014 sit. There's tea, and you're the "
    "first guest this castle's had in years."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: exactly 100 words, 554 characters (gate: 1-600 UTF-8
# characters). No use of "tired", "weary" or "exhausted": the fatigue is
# shown through repetition, clutter and paperwork, not announced.
