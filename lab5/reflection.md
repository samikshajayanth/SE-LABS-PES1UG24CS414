# Lab 5 – Reflection
## Static Code Analysis

### 1. What is static code analysis and why is it important?

Static code analysis examines source code without executing the program. It helps identify programming errors, security vulnerabilities, and coding-standard violations early. This improves code quality, reliability, security, and maintainability.

### 2. What is the difference between Pylint, Bandit, and Flake8?

- Pylint checks code quality, logical issues, naming conventions, unused variables, and programming practices.
- Bandit identifies common security vulnerabilities and unsafe coding patterns.
- Flake8 checks Python formatting, PEP 8 compliance, whitespace, and unused imports.

The tools complement one another because they focus on different aspects of code quality.

### 3. What challenges did you face while fixing the issues?

The main challenge was correcting unsafe code without changing the restaurant order system's intended behavior. The mutable default argument, unsafe eval(), weak hashing, and shell execution required particular attention. After making changes, the program was run again and the analysis tools were rerun to verify the fixes.

### 4. How does static code analysis improve software quality?

Static analysis helps developers identify problems before deployment. It reduces debugging effort, improves security, encourages consistent coding practices, and makes programs easier to maintain. Using multiple tools provides broader coverage than relying on a single tool.

## Final results

- Original Pylint score: 4.81/10; final score: 10.00/10.
- Original Bandit findings: 5; final findings: 0.
- Original Flake8 violations: 9; final violations: 0.
- The restaurant order system executed successfully after modification.

*These are responses to the four reflection prompts in the lab handout. If the instructor provides a separate question sheet, use its exact wording.*
