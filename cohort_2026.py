import time


# ============================================================
# WeThinkCode_ Cohort of 2026
# 365 Days Later
# ============================================================


def type_text(text, delay=0.02):
    """Print text slowly to create a terminal-story effect."""
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()


def pause(seconds=1):
    time.sleep(seconds)


def divider():
    print("\n" + "=" * 60 + "\n")


# ============================================================
# SYSTEM BOOT
# ============================================================

def boot_system():

    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║             WeThinkCode_ COHORT OF 2026                 ║
║                                                          ║
║                   SYSTEM BOOTING...                      ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""")

    pause(1)

    type_text("Initializing Cohort_2026...")
    type_text("Loading 365 days of memories...")
    type_text("Loading friendships...")
    type_text("Loading resilience...")
    type_text("Loading Ubuntu...")
    type_text("Checking developer status...")

    pause(1)

    print()

    name = input("Developer identified. What's your name? > ").strip()

    if not name:
        name = "Developer"

    divider()

    type_text(f"Welcome back, {name}. ❤️‍🔥", 0.05)

    pause(1)

    print("\nChecking cohort status...\n")

    pause(1)

    print("[████████████████████████████████] 365 DAYS COMPLETE ✅")

    pause(1)

    print("""
SYSTEM REPORT

✓ Assessments survived
✓ Failed tests survived
✓ Merge conflicts survived
✓ Deadlines survived
✓ Broken builds survived
✓ Debugging at unreasonable hours survived 😭
✓ "But it works on my machine" survived
✓ Life outside the code survived

SYSTEM STATUS : STILL RUNNING ✅
GIVE_UP       : False
FINAL_SPRINT  : IN PROGRESS 🚀
""")

    pause(1)

    type_text(f"{name}...", 0.08)

    print("""
You didn't come this far
just to stop a few commits before production.
""")

    input("Press ENTER to continue our story...")

    return name


# ============================================================
# 365 DAYS
# ============================================================

def our_story():

    divider()

    type_text("365 DAYS AGO...", 0.08)

    pause(1)

    print("""
365 days ago, we walked into WeThinkCode_
not knowing exactly what was waiting for us.

We came with our laptops.

Our dreams.

Our goals.

And probably enough confidence to believe
that `git push` couldn't possibly ruin an entire day.

Little did we know. 😭


We didn't know about the sleepless nights.

The assessments.

The deadlines.

The debugging.

The failed tests.

The merge conflicts.

The projects that worked perfectly...

until it was time to demo them.


And we definitely didn't know how many times
life itself would throw exceptions that no

try:
    survive()

except Exception:

could completely handle.
""")

    pause(2)

    type_text("But look at us now...", 0.06)

    pause(1)

    type_text("365 DAYS LATER.", 0.08)

    pause(1)

    type_text("STATUS: STILL RUNNING. ❤️‍🔥", 0.07)

    print("""
Not because this journey had clean code.

Not because everything went according to
the documentation.

Not because every test passed the first time.

But because somewhere along the way...

we decided that giving up was NOT going
to be part of our source code.
""")


# ============================================================
# GIT HISTORY
# ============================================================

def check_history():

    divider()

    print("$ git log --cohort\n")

    pause(1)

    print("""
commit 001

    Walked into WeThinkCode_.

    Started as strangers.


commit 050

    First serious challenges detected.

    Confidence status: questionable 😭


commit 100

    Failed some tests.

    Debugged.

    Learned.

    Tried again.


commit 180

    Strangers became friends.


commit 250

    Friends became sisters and brothers.


commit 300

    Ubuntu dependency successfully installed.


commit 365

    Still here. ❤️‍🔥
""")

    pause(2)

    print("""
Sometimes we are so focused on:

    the next sprint,
    the next assessment,
    the next deadline,
    the next project,

that we forget to check our own Git history.

Go back a few commits.

Look at the version of yourself
who walked through those doors 365 days ago.

Now look at yourself today.

That's growth no `git diff`
could ever fully capture.
""")


# ============================================================
# THE BATTLES NOBODY SAW
# ============================================================

def hidden_challenges():

    divider()

    type_text("Scanning challenge history...")

    challenges = [
        "Sleepless nights",
        "Failed tests",
        "Broken builds",
        "Merge conflicts",
        "Assessments",
        "Deadlines",
        "Self-doubt",
        "Life outside the code"
    ]

    print()

    for challenge in challenges:
        pause(0.3)
        print(f"[SURVIVED] {challenge}")

    pause(1)

    print("""
But some challenges were never pushed
to the repository.

There are people in this cohort
who fought battles none of us ever knew about...

and still showed up the next morning.

People came to campus carrying things
much heavier than the laptops on their backs.

And somehow...

they still found a way to laugh with us.

Help somebody debug.

Review someone's code.

Explain something for the tenth time.

Celebrate somebody else's win.

Or simply ask:

"Are you okay?"


Nobody knows every bug life threw
into your system this year except YOU.

Nobody knows how many times
you almost crashed.

Nobody knows how many times
you had to restart...

refactor...

and rebuild yourself...

just to show up again.


So before anything else...

BE PROUD OF YOURSELF. ❤️
""")


# ============================================================
# FRIENDSHIP
# ============================================================

def friendship():

    divider()

    type_text("Analyzing network connections...")

    pause(1)

    print("""
Initial state:

    strangers = True

After 365 days:

    strangers = False
    friends = True
    family = True
""")

    pause(1)

    print("""
Somewhere between `Hello World`
and building actual systems...

strangers became friends.

And friends became sisters and brothers.

We made connections no API could create.

We built relationships no database
could fully store.

And we created memories
no cloud backup could ever truly capture.
""")


# ============================================================
# UBUNTU
# ============================================================

def ubuntu():

    divider()

    type_text("Loading strongest dependency...")

    pause(1)

    print("""
Dependency found:

        UBUNTU ❤️

Definition:

        "I am because we are."
""")

    pause(1)

    print("""
If unity ever needed a definition...

I would simply say:

        WeThinkCode_ Cohort of 2026.
""")

    pause(1)

    print("""
def ubuntu():

    if someone_is_struggling:
        reach_back()

    if someone_is_falling:
        pull_them_forward()

    if someone_wins:
        celebrate_together()

    return "Nobody finishes alone."
""")

    pause(2)

    print("""
We debugged together.

We failed together.

We learned together.

We celebrated together.

We sometimes broke the build together. 😂


But whenever somebody started falling behind...

someone reached back
and pulled them forward.


No framework taught us that.

No documentation explained it.

No tutorial showed us how.


That was Ubuntu.

That was resilience.

That was humanity.

That was US.
""")


# ============================================================
# FINAL SPRINT
# ============================================================

def final_sprint():

    divider()

    type_text("Checking remaining runtime...")

    pause(1)

    print("""
DAYS COMPLETED   : 365
MONTHS REMAINING : LESS THAN 4
SYSTEM STATUS    : STILL RUNNING
MISSION STATUS   : ALMOST THERE
""")

    pause(1)

    print("""
██████████████████████████████████████████░░░░

                     ALMOST THERE.

██████████████████████████████████████████░░░░
""")

    pause(1)

    print("""
After everything we've already survived...

we are just a few commits away
from the finish line.


So when these final months become difficult...

because they probably will...

DO NOT:

    git reset --hard


everything you've worked for. 😂


Check your history.

Remember your first assessment.

Remember your first project.

Remember the things
that once looked impossible.

Remember the code you once couldn't understand
that you can now explain to somebody else.

Remember every failed test
that eventually turned GREEN. ✅


Failure was never the end of the program.

Sometimes...

it was simply feedback from the compiler.


Fix the bug.

Push the commit.

KEEP GOING.
""")


# ============================================================
# FINAL DAY
# ============================================================

def final_day():

    divider()

    type_text("Preparing final deployment...", 0.05)

    pause(2)

    print("""
One day...

sooner than we realise...

there will be no next stand-up.

No next assessment.

No next sprint.

No next reviewer.

No next project deadline.


We will close our laptops...

walk out of WeThinkCode_...

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
    + confidence
    + resilience
    + Ubuntu
    + proof that we kept going
""")

    pause(2)

    print("""
And when that day comes...

I hope we don't only remember
the code we wrote.

I hope we remember EACH OTHER.


The people who helped debug our code...

and sometimes our lives. 😭


The people who stayed
during the failed builds.

The people who celebrated
when our tests finally passed.

The people who became
our home away from home.
""")


# ============================================================
# FINAL COMMIT
# ============================================================

def final_commit():

    divider()

    print("$ git status")

    pause(1)

    print("""
Changes to be committed:

    modified:   ourselves

    added:      growth
    added:      resilience
    added:      friendships
    added:      memories
    added:      ubuntu
    added:      courage
""")

    pause(1)

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

We stayed.

And together...

WE KEPT GOING. ❤️‍🔥
""")

    pause(2)

    print("$ git push origin finish-line")

    pause(1)

    type_text("Pushing 365 days of memories...", 0.03)
    type_text("Pushing friendships...", 0.03)
    type_text("Pushing resilience...", 0.03)
    type_text("Pushing Ubuntu...", 0.03)
    type_text("Pushing one unforgettable year...", 0.03)

    pause(1)

    type_text("Deployment successful. 🚀", 0.07)


# ============================================================
# PERSONAL LEGACY COMMIT
# ============================================================

def legacy_commit(name):

    divider()

    print("""
Before you leave...

Every developer leaves commits behind.

But every person also leaves something
inside the people they shared the journey with.

So leave one final commit for Cohort 2026.
""")

    message = input(
        "What would you like Cohort 2026 to remember?\n\n> "
    ).strip()

    if not message:
        message = "We made it this far together."

    pause(1)

    print("\nCreating legacy commit...")

    pause(1)

    print(f"""
[cohort-2026 365days]

Author: {name}

Commit message:

"{message}"

Commit successful. ✅
""")

    pause(2)

    print(f"""
------------------------------------------------------------

Dear {name},

One day this will all be a memory.

But remember:

You were here.

You contributed.

You struggled.

You learned.

You grew.

You helped build this cohort.

And most importantly...

YOU KEPT GOING. ❤️‍🔥

------------------------------------------------------------
""")


# ============================================================
# END SCREEN
# ============================================================

def end_screen(name):

    print("""
$ git status

COHORT STATUS : ALMOST THERE
FINAL SPRINT  : RUNNING
GIVE_UP       : False


$ git push origin finish-line


██████████████████████████████████████████░░░░

                     ALMOST THERE.


Tests failed.          We tried again.

Builds broke.          We rebuilt.

Life happened.         We kept showing up.

Strangers arrived.     Family was created.
""")

    pause(2)

    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║             WeThinkCode_ COHORT OF 2026                 ║
║                                                          ║
║                  365 DAYS COMPLETE                      ║
║                         ✅                               ║
║                                                          ║
║                FINAL SPRINT RUNNING                     ║
║                                                          ║
║           ████████████████████████░░░░                  ║
║                                                          ║
║                     ALMOST THERE                        ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""")

    pause(1)

    type_text("""
Our repositories may one day be archived.

Our classrooms will welcome another cohort.

Our commits may disappear beneath
thousands of new ones.

But the impact we made on each other
cannot be deleted with a command.
""", 0.025)

    pause(1)

    type_text(
        "Our footsteps may fade, "
        "but our legacy will remain in the system. ❤️‍🔥",
        0.04
    )

    pause(1)

    print(f"""

Happy 365 Days, {name}. ❤️

Happy 365 Days,
WeThinkCode_ Cohort of 2026. 🫂


Almost there, soldiers.


ONE FINAL SPRINT.


LET'S SHIP THIS THING. 🚀💻❤️‍🔥
""")


# ============================================================
# MAIN
# ============================================================

def main():

    name = boot_system()

    our_story()

    check_history()

    hidden_challenges()

    friendship()

    ubuntu()

    final_sprint()

    final_day()

    final_commit()

    legacy_commit(name)

    end_screen(name)


if __name__ == "__main__":
    main()
