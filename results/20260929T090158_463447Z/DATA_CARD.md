# Data card: UCI Bank Marketing

This card describes the `bank-additional-full.csv` variant. It is maintained as report text;
executing the notebook does not rewrite it. Numerical audit findings are in the saved notebook
and its `results` directory.

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


## Data Dictionary
field,meaning,unit,expected_type,documented_domain,special_encoding,availability,timing_reason,definition_source
age,Client age,years,integer,numeric; see range audit,none specified,conditional,Client attribute; historical snapshot unverified,bank-additional-names.txt
job,Job category,category,categorical,admin. | blue-collar | entrepreneur | housemaid | management | retired | self-employed | services | student | technician | unemployed | unknown,unknown = unrecorded/unknown,conditional,Client attribute; historical snapshot unverified,bank-additional-names.txt
marital,Marital status; divorced includes widowed,category,categorical,divorced | married | single | unknown,unknown = unrecorded/unknown,conditional,Client attribute; historical snapshot unverified,bank-additional-names.txt
education,Education category,category,categorical,basic.4y | basic.6y | basic.9y | high.school | illiterate | professional.course | university.degree | unknown,unknown = unrecorded/unknown,conditional,Client attribute; historical snapshot unverified,bank-additional-names.txt
default,Credit in default,category,categorical,no | yes | unknown,unknown = unrecorded/unknown,conditional,Client attribute; historical snapshot unverified,bank-additional-names.txt
housing,Housing loan,category,categorical,no | yes | unknown,unknown = unrecorded/unknown,conditional,Client attribute; historical snapshot unverified,bank-additional-names.txt
loan,Personal loan,category,categorical,no | yes | unknown,unknown = unrecorded/unknown,conditional,Client attribute; historical snapshot unverified,bank-additional-names.txt
contact,Last contact channel,category,categorical,cellular | telephone,none specified,conditional,Must be planned and available before this call,bank-additional-names.txt
month,Month of last contact,month category,categorical,jan | feb | mar | apr | may | jun | jul | aug | sep | oct | nov | dec,none specified,conditional,Calendar is known; last-call selection is retrospective,bank-additional-names.txt
day_of_week,Weekday of last contact,weekday category,categorical,mon | tue | wed | thu | fri,none specified,conditional,Calendar is known; last-call selection is retrospective,bank-additional-names.txt
duration,Last call duration,seconds,integer,numeric; see range audit,none specified,exclude,Post-call: unavailable at t0,bank-additional-names.txt
campaign,"Contacts in current campaign, including last",count,integer,numeric; see range audit,none specified,conditional,Requires decision-time count; final total may contain future contacts,bank-additional-names.txt
pdays,Days since prior-campaign contact; 999 denotes no prior contact,days or sentinel,integer,numeric; see range audit,999 = no prior contact,conditional,History candidate; validate snapshot and sentinel semantics,bank-additional-names.txt
previous,Contacts before current campaign,count,integer,numeric; see range audit,none specified,conditional,History candidate; validate snapshot,bank-additional-names.txt
poutcome,Previous campaign outcome,category,categorical,failure | nonexistent | success,none specified,conditional,History candidate; validate snapshot,bank-additional-names.txt
emp.var.rate,"Employment variation rate, quarterly",rate (scale not fully specified),numeric,numeric; see range audit,none specified,conditional,Publication lag and revisions require as-of release data,bank-additional-names.txt
cons.price.idx,"Consumer price index, monthly",index,numeric,numeric; see range audit,none specified,conditional,Publication lag and revisions require as-of release data,bank-additional-names.txt
cons.conf.idx,"Consumer confidence index, monthly",index,numeric,numeric; see range audit,none specified,conditional,Publication lag and revisions require as-of release data,bank-additional-names.txt
euribor3m,"Three-month Euribor, daily",rate,numeric,numeric; see range audit,none specified,conditional,Daily value must be published before t0,bank-additional-names.txt
nr.employed,"Number employed, quarterly",scale not specified in local readme,numeric,numeric; see range audit,none specified,conditional,Publication lag and revisions require as-of release data,bank-additional-names.txt
y,Term deposit subscribed,yes/no,categorical,no | yes,none specified,target,Outcome only; never a predictor,bank-additional-names.txt


The dataset contains 21 fields: 20 input variables and one target variable (y).

The fields describe client characteristics, previous campaign history, contact information, economic indicators, and the final subscription outcome.

Field group	Variables	Description
Client attributes	age, job, marital, education, default, housing, loan	Demographic and credit-related attributes of the client
Contact information	contact, month, day_of_week, duration	Information about the last marketing contact; duration is observed after the call and is therefore excluded from pre-call prediction
Campaign history	campaign, pdays, previous, poutcome	Information about current and previous marketing campaigns
Economic indicators	emp.var.rate, cons.price.idx, cons.conf.idx, euribor3m, nr.employed	Macroeconomic indicators associated with the campaign period
Target	y	Whether the client subscribed to a term deposit


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



