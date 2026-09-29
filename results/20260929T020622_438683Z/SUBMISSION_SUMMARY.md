# Submission summary draft

This audit asks whether users of the UCI Bank Marketing additional-full dataset can treat all 20 recorded inputs as information available before the last marketing call. It examines 41,188 records and preserves the source attribution, license, retrieval date, and SHA-256 hashes. The intended quantity is subscription probability conditional on information available before a call, within the recorded campaigns. No model is trained.

The checks cover schema, ranges, missingness, duplicates, anomalies, and information availability. Although the table has no parser-null cells, it contains 12,718 unknown-coded entries across 10,700 records. The pdays sentinel occurs in 39,673 rows and cannot be interpreted as elapsed days. There are 12 excess identical rows. They remain in the primary analysis because identical values do not establish customer identity. The observed subscription fraction is about 11.27%, which describes this sample.

The main counterexample is duration, which the documentation places after the call. Its association with subscription cannot justify prediction before calling. Removing duration is necessary but does not verify the availability of campaign totals, historical customer attributes, or macroeconomic releases. Campaign selection, missing customer identifiers, and unspecified outcome timing also limit interpretation. The audit therefore rejects an all-input pre-call interpretation while making no claim about predictive accuracy, causality, or deployment readiness.

Repository URL and commit/tag: TODO

Student review and independent verification: complete AI_USE_LOG.md before submission.
