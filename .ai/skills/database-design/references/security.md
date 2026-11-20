# Database Design – Data security

> Level definitions, algorithms, key management and legal requirements come from the project security documents; this file applies them to tables and columns. DBMS syntax: `postgresql.md` or `mysql-mariadb.md`.

## 1. Column classification

For each table, mark `sensitive` and `secret` columns in the table list of database-design. Questions per column:

- Is storing it truly needed? If not, do not collect it.
- Is reading back the original value needed? If not (passwords, OTP codes, tokens), store only a hash.
- Is exact-match search by value needed? If so, add a keyed hash column (HMAC) for lookup, with the original value encrypted separately.
- Who may view it: fully, partially masked, or no one except system processes?
- How long to keep it, then delete or anonymize?

## 2. Storage by data kind

| Data | Storage method |
| --- | --- |
| Password | One-way salted hash with a slow algorithm (argon2id, bcrypt, scrypt) in the application; no reversible encryption |
| Session tokens, password reset tokens, API keys | Store a hash (SHA-256 suffices since tokens are long and random); show the original once |
| Personal data that must be read back (national ID, account number) | Application-level encryption (envelope encryption, keys from KMS/vault) + HMAC column if lookup needed; key version column for rotation |
| `sensitive` data | Per project rules; at minimum encryption at rest at disk/tablespace level |
| Whole database | Disk encryption or DBMS TDE; TLS required for connections |

In-DB encryption with SQL functions puts keys into statements and query logs: encrypt in the application.

## 3. Accounts and permissions

| Account | Permissions | Used by |
| --- | --- | --- |
| Owner | Owns schema; no day-to-day login | Administration |
| Migrator | DDL on the application schema | Migration pipeline |
| App | SELECT/INSERT/UPDATE/DELETE on needed tables; EXECUTE on needed functions; no DDL | Application |
| Read-only | SELECT on permitted views or tables, with `secret` data masked | Reporting, support |

- Audit tables, ledgers: App account only INSERT and SELECT, no UPDATE/DELETE.
- Do not grant permissions to `PUBLIC` or default accounts; revoke default object-creation permissions if the DBMS grants them.
- Each module (if schemas are split) has its own account and does not read other modules' schemas directly.

## 4. Tenant isolation

- `tenant_id` column in every business table, leading in indexes; composite FKs include `tenant_id`.
- DBMS with row-level security (RLS): enable as a second layer; the App account must not bypass policies and must not own the tables.
- In all cases: filter in the shared data access layer, plus cross-tenant access tests.

## 5. Injection prevention at the DB layer

- Parameterized queries; dynamic table/column names only from an allow-list.
- Stored functions/procedures: no string concatenation in dynamic SQL; use the DBMS's identifier quoting and parameter mechanisms.
- Functions running with definer rights: pin the schema search path.

## 6. Audit

- Audit table records: who (user or service ID), what action, on which record, when, from where (correlation ID), before/after values for non-`secret` columns.
- Append-only, may be time-partitioned, retention per policy.
- Do not write `secret` values into audit; record only "changed".

## 7. Lifecycle and non-production environments

- Retention policy per data group; archive or purge by partition/batch.
- Deletion on data-subject request: list every table holding that person's data (including audit, denormalized copies, backups) and how to handle it (hard delete, anonymize).
- Dev/test/staging data: fake data or irreversibly anonymized copies; do not copy production dumps as is.
- Backups are encrypted; restore permissions are limited.
