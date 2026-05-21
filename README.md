# Number Cruncher Kata

## The Premise

Somewhere out in the world there is a library called **Number Cruncher**. It takes a list of numbers, runs them through a proprietary algorithm, and hands back a single integer. Nobody knows how it works. The source is closed, the logic is secret, and no amount of staring at the inputs will let you predict the output.

Your job is to build a function called `crunch_report` that calls this library and interprets whatever it returns.  The function has been started in the `reporter.py` module.

The function `crunch_report` receives a list of numbers, it needs to execute `crunch_the_numbers`, passing it the list of numbers that were recieved. The function `crunch_report` then needs to report report back details about the result of `crunch_the_numbers`.  The return value of `crunch_report` should be one or more messages.  See the [business logic](#the-business-logic) below for details on how to determine which message(s) should be returned.

---

## The Rules

Work **test-first**. Write a failing test, make it pass, then repeat. That's the whole discipline — don't skip it.

Because `crunch_the_numbers` is completely unpredictable, your tests must control what it returns.

You are only allowed to make changes within the `/kata` directory.

---

## The Business Logic

Which messages are returned depends on the result returned by `crunch_the_numbers`:

| Condition | Message to include |
|---|---|
| result < 10 | `The crunch is too small to matter` |
| result >= 10 and < 100 | `The crunch is ok` |
| result >= 10 and < 100, and result is a multiple of 3 | `Fizz` |
| result >= 10 and < 100, and result is a multiple of 5 | `Buzz` |
| result >= 100 and < 1000 | `The crunch is good` |
| result >= 100 and < 1000, and result is a multiple of 3 | `Fizzier` |
| result >= 100 and < 1000, and result is a multiple of 5 | `Buzzier` |
| result >= 1000 | `The crunch is off the charts` |
| `crunch_the_numbers` raises an exception | `The crunch failed` |

Multiple messages can apply in the same call. A result of 30, for example, is `>= 10`, `< 100`, and a multiple of both 3 and 5 — so three messages apply: `"The crunch is ok"`, `"Fizz"`, and `"Buzz"`.

---

## Getting Started

```bash
cd kata
poetry install
make test
```

The test suite will fail immediately — that's intentional. It's the starting line, not a problem to fix.

Open `tests/test_reporter.py`, replace the placeholder with your first real test, and go from there.

Once you think you've completed the implementation, run:

```bash
make smoke_test
```

This will call `crunch_report` with a random set of numbers and print the result so you can see it in action.
