# King — Super Math Saga A/B Test: Analysis Plan

## 1. Data quality check

Verify the data before anything else.

- NULL checks (both tables)
- Extreme values — rounds, purchases, date ranges
- One player = one install date, one conversion date, one AB test group
- `install_date <= assignment_date` and `install_date <= conversion_date`
- Grain: one row per player per day in `activity`

## 2. Explore the data (no statistical tests)

Explore as much as possible to build assumptions about what the test actually was. Output of this step is the **context foundation** for everything after it:

- Hypothesis — what was the test trying to move?
- Treatment — what change was made? (candidates, with evidence for/against)
- Primary metric
- Guardrail metrics
- Randomization unit (user level as stated in the assignment)


**State the data limitations that constrain the test context**, e.g. only *number* of purchases, no transaction value.

## 3. Sanity check

- SRM
- Whether the randomisation logic looks correct
- Any bug during the test
- Novelty effect
- Data skewness
- Segmentation → Simpson's paradox
- Weekend effect

## 4. Insights

- **Engagement** — frustration? retention signal?
- **Conversion** — purchase behaviour, short term to long term
- **User segementation** - new vs existing one, non-paying users vs spenders. Any move from non-paying to spending?

## 5. Statistical test

Conclude whether there is a difference between treatment and control.

## 6. Recommendation

Ship or not? If not what should be done next?
Any other interesting insights that can be taken to convert to actions for product team?


---

## Key notes

**Primary metric should be revenue per user.** Otherwise a change can lift conversion without lifting total revenue.

**Cannibalization.** If the test was a new offer to buy hints, we have no data on possible offer cannibalization — only purchase counts, no transaction value or SKU.

**Confirmation bias.** A treatment story has been built during exploration. Write the decision rule *before* running the statistical tests — what result recommends A, what recommends B, what says inconclusive.

---

## Status

**Step 1 — done.** Data is clean. Grain confirmed, no nulls of concern, no logical date violations, no duplicate player-days.

**Step 2 — in progress.** Population: 82% existing / 18% new players. Split holds at 80/20 in both. Established that conversion is unchanged (bucket 0 identical at 97.31%), the effect is intensity among existing payers, and it scales with spend level (+3.4% / +5.3% / +6.6% across the 6-10, 11-20, 21+ buckets).

**Step 3 — largely done via exploration.** SRM passed (χ² = 0.35, p ≈ 0.55). DAU series continuous in both arms, no logging break. Pre-period lines overlap on every metric. Control arm stable throughout, which rules out external events, shared release changes, and contamination. Novelty identified: monetization effect decays over the window, engagement effect does not.

**Still to do:** event-time view, new-vs-existing split, weekend effect, fixed-window robustness check, MDE, statistical tests, recommendation.
