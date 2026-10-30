# Lab 5 – Static Code Analysis
## Restaurant Order System

| Issue | Type | Original line(s) | Description | Fix approach |
|---|---|---:|---|---|
| Weak MD5 hashing | Security – High | 47 | MD5 is not suitable for security-sensitive hashing. | Replaced with SHA-256 for ticket identifiers. |
| Shell command execution | Security – High | 58 | Shell execution with a filename can create command-injection risk. | Removed os.system(); used pathlib for file output. |
| Unsafe eval() | Security – Medium | 42 | eval() can execute arbitrary Python expressions. | Replaced with a numeric discount rate and validation. |
| Bare exception | Quality/Security – Low | 26 | Bare except hides unexpected errors. | Removed broad exception handling and used dict.pop(). |
| Insecure random PIN | Security – Low | 51 | random is not intended for security-sensitive values. | Replaced with secrets.randbelow(). |
| Mutable default argument | Quality | 15 | A list default is shared between calls. | Changed default to None and initialize a fresh list. |
| Unused import | Style | 6 | math was never used. | Removed the import. |
| Unused variables | Quality | 31, 41 | Assigned values were never used. | Removed unused variables. |
| Naming convention | Style | 15, 23, 30, 40 | Function names did not follow snake_case. | Renamed functions to snake_case. |
| Formatting and documentation | Style | Multiple | Long lines, missing docstrings and missing final newline. | Reformatted code and added docstrings. |
| File handling | Quality | 55 | File was opened without explicit encoding or context management. | Used pathlib and a context manager with UTF-8. |

## Final results

- Pylint: 4.81/10 before; 10.00/10 after.
- Bandit: 5 findings before; 0 after.
- Flake8: 9 violations before; 0 after.
