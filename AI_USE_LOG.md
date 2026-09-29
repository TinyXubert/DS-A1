# AI use and independent verification
 Codex read the assignment PDF and the
variant-specific source documentation, wrote and tested the audit code, and revised the
structure after the supplied ChatGPT review. These are actions by the assistant.

| Suggestion | Decision in this draft | Reason or evidence |
|---|---|---|
| Use Bank Marketing and ask about information available before a call | Accepted | The additional-variant documentation identifies a post-call variable. |
| Separate `unknown` from parser nulls and `pdays=999` from elapsed days | Accepted | Attribute 13 and section 8 of the local names file document these encodings. |
| Shorten the notebook and maintain the Data Card separately | Accepted | The same required audits fit into seven report sections. |
| Replace the estimand with a proportion/probability without conditioning | Modified | Plain language is clearer, but the sample fraction and conditional probability are different quantities. |
| Define population as whatever the dataset claims to represent | Modified | The source setting is stated explicitly; actual coverage and selection remain uncertain. |
| Use `Path.cwd()` as the project root | Accepted with a directory check | Execution now requires starting in DS-A1, as documented in README. |
| Treat extreme values as errors | Not adopted | The review thresholds are exploratory; they do not establish recording errors. |

## Student verification and reflection (complete personally)

- Name and date: Hongbo Xu  202618018629048 2026/9/28
Source definition I checked, including file/section and finding

I independently checked the variant-specific documentation:

data/raw/bank-additional-names.txt, attribute descriptions for duration and pdays.

I verified that:

duration represents the duration of the last contact and is only observed after the call has occurred.
pdays=999 is a special encoding indicating that the client was not previously contacted, rather than a numerical value of 999 elapsed days.

These definitions support the audit conclusion that raw numerical values cannot always be interpreted as ordinary measurements.


Numerical finding I checked independently, including method and result

I independently recomputed the number of pdays=999 records using a separate calculation:

(df["pdays"] == 999).sum()

The result was:

39,673 records

which matches the notebook output.

I also checked the total number of rows:

len(df)

and obtained:

41,188 records

This confirmed that the reported sentinel frequency was calculated from the frozen dataset.


AI advice I accepted or rejected and my reason

I accepted the suggestion to focus the audit question on information availability before the marketing call.

This was accepted because the dataset documentation contains a clear post-call variable (duration), allowing a concrete audit question rather than a model performance comparison.

I rejected the idea that extreme values should automatically be treated as errors.

Although values such as long call duration or high campaign counts may appear unusual, the available documentation does not prove that they are recording mistakes. Therefore, I kept them as review flags rather than deleting them.


Unexpected or negative evidence and its effect on my conclusion

A surprising finding was that the dataset contained no parser-level missing values but contained 12,718 unknown-coded entries across 10,700 records.

This changed my interpretation of missingness: the absence of NaN values does not imply complete measurement.

Another unexpected finding was that 4,110 records had previous > 0 and pdays = 999. The documentation does not resolve whether this represents an inconsistency or a difference in field definitions. Therefore, I report it as a limitation instead of correcting or removing these records.


My answer to the audit question and its limits

The audit question was whether all 20 recorded inputs can be treated as information available immediately before the recorded last marketing call.

My conclusion is no: duration provides a documented counterexample because it is observed after the call.

However, removing duration alone is insufficient to establish that all remaining variables are valid pre-call information. Historical availability, publication timing of macroeconomic variables, customer identity, and campaign selection mechanisms remain partially unresolved.

Therefore, this audit supports careful interpretation of the dataset but does not establish predictive performance, causal effects, or deployment readiness.

Read the original documentation and use a separate calculation, spreadsheet, or manual raw-row
check for at least one numerical result. Record what you actually did. Then rerun the notebook's
last cell so the saved output and PDF include the revised log.
