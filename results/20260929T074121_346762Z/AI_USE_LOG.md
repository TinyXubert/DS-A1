# AI use and independent verification

This draft was prepared with ChatGPT and Codex. Codex read the assignment PDF and the
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

- Name and date: TODO
- Source definition I checked, including file/section and finding: TODO
- Numerical finding I checked independently, including method and result: TODO
- AI advice I accepted or rejected and my reason: TODO
- Unexpected or negative evidence and its effect on my conclusion: TODO
- My answer to the audit question and its limits: TODO

Read the original documentation and use a separate calculation, spreadsheet, or manual raw-row
check for at least one numerical result. Record what you actually did. Then rerun the notebook's
last cell so the saved output and PDF include the revised log.
