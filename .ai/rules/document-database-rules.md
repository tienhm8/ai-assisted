# Document Database Rules

> Status: **Approved**. Mandatory Rule when the project uses a document database (MongoDB, NoSQL); applies together with Database Rules. "Table" means collection, "column" means field.

1. The document model (embed or reference) is derived from recorded access patterns; no unboundedly growing embedded arrays.
2. Every collection has schema validation declared by migration; validators, indexes, and data migrations all go through migrations in source code.
3. Invariants that DB constraints cannot hold (cross-document references, rules spanning multiple documents) must record how they are held: consolidate into one document, multi-document transaction, or application check plus reconciliation.
4. Do not put input objects into query conditions as-is; cast each field, reject keys starting with `$`; do not run server-side JavaScript with user input.
5. Write business data with majority replica acknowledgment (write concern `majority`); lower it only with an approved ADR.
