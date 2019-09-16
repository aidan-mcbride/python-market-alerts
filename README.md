# Silver Market Desktop Alerts

Command line python application to get notifications on the desktop when the spot price of silver reaches a given amount.

> NOTE: if you actually want to get notifications about silver's spot price, I would not recommend this program. Most precious metal dealers on the internet offer some kind of email-based notification system, so I would suggest that you sign up with whichever dealer you like the most to get their notifications.

## About

I wanted to learn how to push ubuntu notifications from a python program for some other projects I have in mind(e.g. it would be cool if I got a notification if my travis-ci build failed). I also wanted to build something entirely with TDD, since everyone says TDD is really neat. I decided to try both of those on a project I wanted to build to track the price of silver, so I wouldn't need to check it all the time.

Originally I had these mega-ambitious ideas of building a CLI that would run as a daemon, and would track multiple commodities from multiple different sources, and that the whole thing would have this crazy level of documentation and type-checking, and 100% test coverage, and that every single function would be developed using TDD.

One thing I learned early was that this project was not well suited for learning TDD. It seems to me that TDD is well suited for programs that are 'business logic' heavy, built on familiar technologies, and have well-defined requirements. I had a hard time getting TDD to work here, since a lot of this project was basically gluing various packages together - many of which I didn't know about until I needed to install them. I'm going to take a step back and learn TDD with something simpler and easier to test.

I also had to reduce the scope of the project so that I would be able to finish it before losing interest entirely and abandoning it. As such, right now you can only track the spot price of silver from JMBullion, and the program does not run in the background. Despite this, I have personally declared victory over this project, as I accomplished all my personal goals for this project.

### Personal Project Goals

1. Learn how to push desktop notifications from python.
2. Become acquainted with different code formatting tools and development helpers for python projects, e.g. black, flake8, etc.
3. Become acquainted with building a real CLI.
4. Attempt test-driven development.

---

## How To Use

### To Install:

```python
pipenv install
```

### To Run

```python
pipenv run python3 cli.py [options]

## --help flag output:
Usage: cli.py [OPTIONS]

  Start program with given options

Options:
  -i, --interval INTEGER  Number of seconds to wait between checking price.
                          Default is 15 minutes(900 seconds)
  -l, --limit FLOAT       Spot price of silver at which to be notified
                          [required]
  -s, --side TEXT         either 'above' or 'below' - check that current price
                          is above or below the given limit  [required]
  --help                  Show this message and exit.

```

### To Run Tests

```python
pipenv run pytest
```

---

## TO-DO:

**CORE**

- [ ] ~~Get silver spot price from some public API~~ Scrape silver spot price from a website.

  *(I couldn't find a free, public API with commodity prices)*

- [x] Set up some sort of scheduler to get spot price periodically.

- [x] Check spot price against some threshold

- [x] Push notifications to Ubuntu desktop when threshold is crossed.

- [x] Create some command-line interface to set threshold.


**OPTIONAL EXTENSIONS**

- [ ] Run application as a daemon? In background without leaving a terminal window open.
- [ ] Set period dynamically based on when any given API updates.
- [ ] Configuration option to start program when computer boots.
- [ ] Choose what type of market to track.
- [ ] Track multiple websites/apis to get aggregate spot price.

## Dependencies

* requests
* beautifulsoup4

### Development Dependencies

**Linting & Formatting**

* black
* flake8
* isort

**Type Checking**

* mypy

**Testing**

* pytest
* pytest-cov

**Continuous Integration**

* pre-commit

*I set up my tooling based on [this article](https://sourcery.ai/blog/python-best-practices/).*

### OS Dependencies

* [notify-send](https://manpages.ubuntu.com/manpages/disco/en/man1/notify-send.1.html) must be installed for sending desktop notifications
