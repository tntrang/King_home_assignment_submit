# Super Math Saga — A/B Test Analysis

Code and notebooks for the King home assignment: an analysis of a 2017 A/B test on
*Super Math Saga*, a fictional free-to-play mobile game.

Data lives in BigQuery — project `king-ds-recruit-candidate-1114`, dataset `abtest`,
tables `assignment` and `activity`. The brief and the table schemas are in
[context/](context/).

## Repo layout

| Path | What it is |
|---|---|
| [analysis/data_quality_check.ipynb](analysis/data_quality_check.ipynb) | NULLs, extreme values, grain, date logic. |
| [analysis/exploration.ipynb](analysis/exploration.ipynb) | Descriptive exploration, no statistical tests. Sets up the hypothesis, metrics and decision rule. |
| [analysis/abtest_analysis.ipynb](analysis/abtest_analysis.ipynb) | Sanity checks, statistical tests, segment deep dives, recommendation. |
| [bigquery.py](bigquery.py) | `run_query(sql, save_as=...)` — runs a query, optionally caches the result to `data/<name>.parquet`. |
| [config.py](config.py) | `PROJECT_ID` and `DATA_DIR`. |
| [context/](context/) | Assignment brief, data schema, analysis plan. |
| `data/` | Local parquet cache. Gitignored, rebuilt by running the notebooks. |

## Reading it

Notebooks run in order: data quality → exploration → analysis. Each of the latter two
opens with a pointer to its own summary section, so for conclusions only:

- **exploration.ipynb** → *Conclusion*
- **abtest_analysis.ipynb** → *Recommendations*

## Setup

Requires Python ≥ 3.14 and a Google Cloud account with read access to the dataset.

```bash
uv sync
gcloud auth application-default login
uv run jupyter lab
```

Select the `.venv` kernel when opening a notebook.

Queries hit BigQuery directly. The three heaviest results (`ab_user_level`,
`retention`, `repeat_buy`) are written to `data/` on first run via `save_as=`, so later
cells read parquet instead of re-querying. Delete a file there to force a refresh.