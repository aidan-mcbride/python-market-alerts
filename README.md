# Market Alerts

> ***THIS IS A LEARNING PROJECT*** - use at your own peril.

Get ubuntu desktop alerts when silver's spot price reaches given thresholds.

## TODO:

**CORE**

- [ ] Get silver spot price from some public API
- [ ] Set up some sort of scheduler to get spot price periodically.
- [ ] Check spot price against some threshold
- [ ] Push notifications to Ubuntu desktop when threshold is crossed.
- [ ] Create some command-line interface to set threshold.

**META** - requirements for *how* the project is built:

* Test-Driven Development - no code will be committed without a corresponding test.
* Docstring documentation for every method.

**OPTIONAL EXTENSIONS**

- [ ] Set period dynamically based on when any given API updates.
- [ ] Configuration option to start program when computer boots.
- [ ] Choose what type of market to track.