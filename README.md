# Market Alerts

> ***THIS IS A LEARNING PROJECT*** - use at your own peril.

Get ubuntu desktop alerts when silver's spot price reaches given thresholds.

## TODO:

**CORE**

- [ ] ~~Get silver spot price from some public API~~ Scrape silver spot price from a website.

  *(I couldn't find a free, public API with commodity prices)*

- [ ] Set up some sort of scheduler to get spot price periodically.

- [ ] Check spot price against some threshold

- [ ] Push notifications to Ubuntu desktop when threshold is crossed.

- [ ] Create some command-line interface to set threshold.

- [ ] Run application as a daemon? In background without leaving a terminal window open.

**META** - requirements for *how* the project is built:

* Test-Driven Development - no code will be committed without a corresponding test.
* Docstring documentation for every function.

**OPTIONAL EXTENSIONS**

- [ ] Set period dynamically based on when any given API updates.
- [ ] Configuration option to start program when computer boots.
- [ ] Choose what type of market to track.

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

---

### Tests

**Note on test sparseness:**

Many sources advise against writing unit tests that simply test that an imported package is working - e.g. one shouldn't write a test to confirm that requests can get a response from a website. Since a lot of this particular application is simply gluing together various packages, there aren't a lot of tests.

---

To run pre-commit script without actually committing:

```bash
pipenv run pre-commit run --all-files
```

