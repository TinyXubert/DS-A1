# Data card: UCI Bank Marketing

This card describes the `bank-additional-full.csv` variant. It is maintained as report text;
executing the notebook does not rewrite it. Numerical audit findings are in the saved notebook
and its `results` directory. Student review is pending.

## Source and permitted use

Moro, S., Rita, P., & Cortez, P. (2014). *Bank Marketing*. UCI Machine Learning Repository.
[Dataset DOI](https://doi.org/10.24432/C5K306).
The [UCI page](https://archive.ics.uci.edu/dataset/222/bank+marketing) lists
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), which requires attribution.
Audit tables and plots are derived artifacts; the raw CSV has not been modified.

- Download: https://archive.ics.uci.edu/static/public/222/bank+marketing.zip
- Retrieved UTC: 2026-09-28T08:32:02.794284+00:00
- CSV SHA-256: `74adfc578bf77a7ff4bb1ba4a9f8709d9e3c6907342959c2c8416847e0afb4d8`
- Full archive and documentation hashes: `data/raw/manifest.json`.
- Variant definitions: `data/raw/bank-additional-names.txt`.
- Related paper: Moro, Cortez & Rita (2014), DOI 10.1016/j.dss.2014.03.001. This audit does not replicate the paper.

## Records and question

The documentation describes 41,188 records with 20 inputs and the target `y`, ordered by date
from May 2008 to November 2010. A published row summarizes a client/campaign record, including
the last contact and earlier contacts. The file has no customer identifier, so a row is not
assumed to be a unique person or a record of every call.

The audit asks whether every input was available immediately before the recorded last call.
Its main stakeholders are researchers reusing the table. Providers, maintainers, bank decision
makers, and affected customers also have an interest in valid interpretation.
The intended population is records from the source bank's telephone marketing campaigns in
this period; its coverage and selection mechanism are incompletely documented.
The quantity of interest is subscription probability conditional on information available
before the call, among recorded campaigns. This audit checks support for that quantity;
it does not estimate the conditional function or train a model.

## Measurement and handling

`y` records term-deposit subscription; the exact follow-up window is unspecified.
`unknown` marks unrecorded/unknown categories. `pdays=999` is a status code for no previous
contact, not 999 elapsed days. The main analysis preserves all rows and original values.
Duplicate and extreme-value flags prompt review, not automatic deletion.
A separate exact-deduplication comparison shows sensitivity without changing the main table.
Field definitions, units, domains, and timing judgments are in `DATA_DICTIONARY.csv`.

## Limits

`duration` is observed after the call and cannot support prediction before it.
The remaining inputs require historical snapshot or publication-time evidence, especially
campaign totals and macroeconomic indicators. Removing `duration` alone does not establish
that the predictors are valid at the decision time.
Missing customer IDs prevent reliable customer-level deduplication and split checks.
The public table does not establish representativeness beyond the recorded campaigns.
It supports descriptive auditing, not claims of deployment accuracy or causal effects of calling.
No identifiers are added and no person-level linkage is performed.

## Reproduction and review

Run `A1.ipynb` from the repository directory using the dependencies in `requirements.txt`.
Each run records its environment and data hashes. The notebook displays this card in its PDF
output; update this file and rerun that display cell if its text changes.
AI assistance and the student's separate verification record are in `AI_USE_LOG.md`.
