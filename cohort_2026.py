import time


def type_text(text, delay=0.025):
    """Print text slowly to make the message feel alive."""
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()


def pause(seconds=1):
    time.sleep(seconds)


def divider():
    print("\n" + "=" * 58 + "\n")


# --------------------------------------------------
# WeThinkCode_ Cohort of 2026
# 365 Days Later ❤️
# --------------------------------------------------

DAYS_SURVIVED = 365
MONTHS_REMAINING = 4

status = "STILL RUNNING"
give_up = False

values = [
    "Ubuntu",
    "Resilience",
    "Humanity",
    "Unity",
    "Grit"
]


divider()

type_text("INITIALIZING COHORT_2026...")
pause()

type_text("Loading memories...")
pause()

type_text("Loading friendships...")
pause()

type_text("Loading resilience...")
pause()

type_text("Checking system status...")
pause(1.5)

print(
    f"""
╔════════════════════════════════════════════════════════╗
║            WeThinkCode_ COHORT OF 2026                ║
║                                                        ║
║              365 DAYS COMPLETE ✅                      ║
║                                                        ║
║              STATUS: {status:<20}          ║
║                                                        ║
║          FINAL SPRINT: IN PROGRESS...                  ║
╚════════════════════════════════════════════════════════╝
"""
)

pause(2)

type_text("365 days ago...")
pause()

print("""
We walked into WeThinkCode_ not knowing
exactly what was waiting for us.

We didn't know about the sleepless nights.

The assessments.

The deadlines.

The debugging.

The failed tests.

The merge conflicts.

The projects that worked perfectly...

until it was time to demo them. 😭

And we definitely didn't know how many times
life itself would throw exceptions that no
try/except could handle.
""")

pause(2)

type_text("But look at the system now...")
pause()

type_text("STATUS: STILL RUNNING. ❤️‍🔥", 0.06)

divider()

# --------------------------------------------------
# CHECK OUR HISTORY
# --------------------------------------------------

print("Checking Git history...\n")
pause()

version_1 = "The person who walked in 365 days ago"
version_now = "The person standing here today"

print(f"OLD VERSION : {version_1}")
print(f"NEW VERSION : {version_now}")

pause(2)

if version_now != version_1:
    print("""
CHANGE DETECTED ✅

Sometimes we are so focused on the next sprint,
the next assessment and the next deadline that
we forget to check our own Git history.

Go back a few commits.

Look at the person who walked through those
doors 365 days ago.

Now look at yourself.

That's growth no `git diff` could ever
fully capture.
""")


divider()

# --------------------------------------------------
# THE BUGS NOBODY SAW
# --------------------------------------------------

challenges = [
    "Sleepless nights",
    "Failed tests",
    "Broken builds",
    "Merge conflicts",
    "Deadlines",
    "Assessments",
    "Self-doubt",
    "Life outside the code"
]

print("Running challenge history...\n")

for challenge in challenges:
    pause(0.3)
    print(f"[PASSED] {challenge}")

pause()

print("""
There are people in this cohort who fought battles
none of us ever knew about...

and still showed up the next morning.

Some came to campus carrying things much heavier
than the laptops on their backs.

Yet they still found a way to laugh with us,
help somebody debug,
review someone's code,
explain something for the tenth time,

or simply ask:

"Are you okay?"

Nobody knows every bug life threw into your system
this year except YOU.

Nobody knows how many times you almost crashed.

Nobody knows how many times you had to restart,
refactor and rebuild yourself just to show up again.

So before anything else...

BE PROUD OF YOURSELF. ❤️
""")


divider()

# --------------------------------------------------
# UBUNTU
# --------------------------------------------------

type_text("Loading strongest dependency...")
pause()

print("\nDependency found: UBUNTU ❤️\n")

pause()

print("""
Somewhere between Hello World
and building actual systems...

strangers became friends.

And friends became sisters and brothers.

We learned something that isn't written
in any documentation:

Sometimes the person sitting next to you
believing in you is enough to make you
run the program one more time.
""")

pause()

print("if unity.has_definition():")
print('    return "WeThinkCode_ Cohort of 2026"')

pause(2)

print("""
Because what I witnessed in this cohort was
Ubuntu in its purest form:

        I AM BECAUSE WE ARE.

We debugged together.
We failed together.
We learned together.
We celebrated together.

And yes...

sometimes we broke the build together. 😂

But whenever somebody started falling behind,
someone reached back and pulled them forward.

No framework taught us that.

No documentation explained it.

That was us.
""")


divider()

# --------------------------------------------------
# FINAL SPRINT
# --------------------------------------------------

print("Checking remaining runtime...\n")
pause()

print(f"DAYS COMPLETED   : {DAYS_SURVIVED}")
print(f"MONTHS REMAINING : LESS THAN {MONTHS_REMAINING}")
print("MISSION STATUS   : ALMOST THERE")

pause(2)

print("""
████████████████████████████████████████░░░░

                 ALMOST THERE.

████████████████████████████████████████░░░░
""")

pause()

print("""
When these final months become difficult...

don't `git reset --hard` everything
you've worked for. 😂

Check your history.

Remember your first assessment.

Remember the things that once looked impossible.

Remember every failed test that eventually
turned GREEN.

Failure was never the end of the program.

Sometimes...

it was simply feedback from the compiler.

Fix the bug.

Push the commit.

KEEP GOING.
""")


divider()

# --------------------------------------------------
# ONE DAY...
# --------------------------------------------------

type_text("Preparing final deployment...")
pause(2)

print("""
One day, sooner than we realise...

there will be no next stand-up.

No next assessment.

No next sprint.

No next reviewer.

No next deadline.

We will close our laptops,
walk out of WeThinkCode_,

and realise that the biggest project
we built here was never inside
a Git repository.

                    IT WAS US.

Version 1.0 walked in 365 days ago.

The version walking out will carry:

    + skills
    + scars
    + friendships
    + memories
    + resilience
    + Ubuntu
    + proof that we didn't give up
""")


divider()

# --------------------------------------------------
# FINAL COMMIT
# --------------------------------------------------

print("$ git status")
pause()

print("""
Changes to be committed:

    modified:   ourselves
    added:      resilience
    added:      friendships
    added:      memories
    added:      ubuntu
    added:      growth
""")

pause()

print('$ git commit -m "We made it this far together."')

pause(2)

print("""
[cohort-2026 final-sprint]

We came.
We coded.
We crashed.
We debugged.
We rebuilt.
We grew.

And together...

WE KEPT GOING. ❤️‍🔥
""")

pause(2)

print("$ git push origin finish-line")

pause()

type_text("Pushing 365 days of memories...", 0.04)
type_text("Pushing friendships...", 0.04)
type_text("Pushing resilience...", 0.04)
type_text("Pushing Ubuntu...", 0.04)

pause()

type_text("Deployment successful. 🚀", 0.08)


divider()

print(
    """
╔════════════════════════════════════════════════════════╗
║                                                        ║
║            WeThinkCode_ COHORT OF 2026                ║
║                                                        ║
║                 365 DAYS COMPLETE                     ║
║                        ✅                              ║
║                                                        ║
║              FINAL SPRINT LOADING...                  ║
║                                                        ║
║        ████████████████████████░░░░░░░░               ║
║                                                        ║
║                   ALMOST THERE                        ║
║                                                        ║
╚════════════════════════════════════════════════════════╝


Tests failed.          We tried again.

Builds broke.          We rebuilt.

Life happened.         We kept showing up.

Strangers arrived.     Family was created.


Our repositories may one day be archived.

Our classrooms will welcome another cohort.

Our commits will disappear beneath thousands
of new ones.

But the impact we made on each other
cannot be deleted with a command.


        Our footsteps may fade,

        but our legacy will remain
        in the system. ❤️‍🔥


        Happy 365 Days,
        WeThinkCode_ Cohort of 2026.


        Almost there, soldiers. 🫂

        ONE FINAL SPRINT.

        LET'S SHIP THIS THING. 🚀
"""
)