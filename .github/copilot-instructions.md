# Copilot Instructions for this Repository ✅

Purpose
- Short, focused guidance for an AI coding agent working on this repository of beginner Python exercises (in Portuguese).

Quick facts
- Project type: collection of small Python scripts (no package, no tests, no CI).
- Language: Python 3 (uses standard library only: e.g., math, random).
- Typical run: `python <path/to/file.py>` from repo root on Windows.

Project layout (examples)
- `exercicios/` — main exercises named `exNNN.py` (e.g., `ex003.py`, `ex010.py`).
- `Nova pasta/` — class/aula examples (`aula08.py`, `aula09.py`, etc.) and small tests (`teste01.py`).

What to expect (patterns found)
- Scripts are interactive: they use `input()` to prompt the user (prompts are in Portuguese) and print results with `print()`.
  - Example: `ex003.py` prompts for numbers and prints an f-string result.
- Formatting: both f-strings and `str.format()` are used; numeric formatting like `{:.2f}` is common (`ex010.py`).
- Imports: only standard library modules (`math`, `random`), often using both `import math` and `from math import ...` (`aula08.py`).
- Variable names and prompts are in Portuguese (e.g., `soma`, `numero`, `Digite ...`).

Guidance for edits and new work
- When adding a new exercise: place it under `exercicios/` and follow the naming `exNNN.py` and Portuguese prompt style.
- For non-interactive code or to enable testing: move logic into functions and add an `if __name__ == "__main__":` block only for CLI-style interaction. Example pattern to add:
  ```py
  def soma(a, b):
      return a + b

  if __name__ == "__main__":
      n1 = int(input('Digite o primeiro numero: '))
      n2 = int(input('Digite o segundo numero: '))
      print(f'Soma: {soma(n1, n2)}')
  ```
- Keep user-facing text in Portuguese and preserve the concise/educational style.

Running & debugging
- Run single scripts directly: `python exercicios/ex003.py` (Windows PowerShell recommended).
- There is no virtualenv or requirements file — standard Python installation suffices.
- Watch out for directory names with spaces and non-ASCII characters (e.g., `Nova pasta`) when scripting CI or automation.

Testing and CI
- No tests or CI config were found. If adding tests, prefer converting interactive logic into pure functions (see above) and add a simple `tests/` folder with pytest-compatible tests.

Limitations / things not present
- No package structure, no setup.py/pyproject.toml, no manifest of external dependencies, and no existing unit tests or CI pipelines.

Examples to reference
- `ex003.py`: f-string printing with input-driven values
- `ex010.py`: numeric formatting with `str.format` (`{:.2f}`)
- `ex020.py`: uses `random.shuffle` on a list of inputs
- `aula08.py`: demonstrates both `import math` and `from math import sqrt, ceil`

If anything is unclear or you want me to expand sections (for example, adding a short cookbook of common refactors to make exercises testable), tell me which parts to improve and I will iterate. 🔧
