# Lab 7 – Fuzz Testing

Pet Boarding application tested using Python, pytest, and Hypothesis.

## Files
- `pet_boarding.py`: corrected application with input validation.
- `test_pet_boarding.py`: six Hypothesis property-based fuzz tests.
- `Lab7_Fuzz_Testing_Report.docx`: full lab report.
- `evidence/`: before- and after-fuzzing terminal screenshots.

## Run
Create and activate a virtual environment, install dependencies, then run:

```bash
python3 -m pip install hypothesis pytest
python3 -m pytest -v test_pet_boarding.py
python3 pet_boarding.py
```

## Fuzz test result
- Before fixes: 5 failed, 1 passed.
- After fixes: 6 passed.

## Repository
https://github.com/samikshajayanth/SE-LABS-PES1UG24CS414
