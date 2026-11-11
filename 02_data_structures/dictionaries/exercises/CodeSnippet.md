## Code

```python
grades = {
    name: 'A' if score >= 90 else (
          'B' if score >= 80 else (
              'C' if score >= 70 else (
                  'D' if score >= 60 else 'F')))
    for name, score in scores.items()
}
```

## How It Works

1. The dictionary comprehension loops through every entry in `scores` using
   `scores.items()`. For each entry, `name` is the student's name (the key) and
   `score` is their numeric score (the value).
2. The nested `if-else` expression checks each score from highest to lowest:

   | Condition for `score` | Grade |
   | --- | --- |
   | 90 or higher | `'A'` |
   | 80 or higher, but below 90 | `'B'` |
   | 70 or higher, but below 80 | `'C'` |
   | 60 or higher, but below 70 | `'D'` |
   | below 60 | `'F'` |

   As soon as a condition is true, its letter is selected and the remaining
   conditions are skipped.
3. For each student, the comprehension adds an entry to `grades`: the student's
   name becomes the key, and the selected letter becomes the value. The original
   `scores` dictionary is not changed.

For example, if `scores` contains `{"Ana": 92, "Ben": 67}`, the result is
`{"Ana": "A", "Ben": "D"}`.

## Comparison with `04_student_grades_and_passing_status.py`

Both approaches assign the same letter grades. This code creates `grades`
directly with a dictionary comprehension. The script first copies `scores` into
`grades`, then uses a `for` loop and `if-elif-else` statements to replace each
numeric score with its letter grade.

The script also creates a second dictionary, `passing`, containing only
students whose original scores are 60 or higher. Its values are the numeric
scores, not the letter grades. The comprehension shown here creates only
`grades`.
