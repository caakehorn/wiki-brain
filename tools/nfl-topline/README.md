# NFL Topline

A single-file worksheet for producing a quick, structured betting read on one NFL game.
Built for someone who has never used an AI tool before: there is nothing to install, nothing
to configure, and no prompt to write.

Open `index.html` in any browser. It works offline and stores nothing.

## Why it is split in two

The page deliberately does not ask a language model to do arithmetic, because models are
unreliable at it and the arithmetic here is the part that decides whether a bet is worth
making. The work is divided along that line:

| Done by the page, in your browser | Done by Claude |
| --- | --- |
| Converting American odds to probability | Reading current efficiency numbers |
| Stripping the sportsbook's cut (de-vigging) | Checking injuries and practice reports |
| Turning a projected margin into a win probability | Weather, rest, travel, pace |
| Edge, expected value, Kelly stake sizing | Producing a projected margin and total |
| The bet / lean / pass call | — |

Claude never sees the odds math, and the page never guesses at a football fact.

## How it is used

1. Type the matchup and copy the current lines off a sportsbook.
2. Press **Copy prompt** and paste it into Claude. The prompt instructs Claude to search for
   current-season numbers rather than answer from memory, to cite an as-of date for every
   figure, and to finish with a fixed block of labelled outputs.
3. Type the two numbers from the bottom of Claude's answer — projected margin and projected
   total — back into the page.
4. Read the verdict table.

## The model behind the numbers

Game results are treated as normally distributed around the projection: margins with a
standard deviation of 13.2 points, totals with 10.5. Those figures are the conventional
approximations for NFL scoring. Probability is the common currency, so spreads, totals and
moneylines are all compared on one scale.

Thresholds are set from the noise floor stated on the page — roughly two points of spread
disagreement, which is about six points of win probability:

- **Bet** at 7% edge or better (about 2.3 points)
- **Lean** between 4% and 7%
- **Pass** below 4%

The normal approximation treats every margin as equally likely, which is not quite true:
3 and 7 occur much more often than their neighbours. Spread probabilities sitting exactly on
a key number are therefore the weakest output on the page, and it says so.

## What this is not

It is not an edge. Sportsbooks price NFL games very well, and most honest reads come back
`Pass` by design. The verdicts are a discipline aid — a way of noticing when a strong opinion
is not actually strong enough to bet — not a signal to follow.
