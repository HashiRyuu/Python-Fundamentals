# Python Fundamentals

A collection of 36 Python programming examples, spanning arithmetic and control flow, strings, collections, file processing, object-oriented design, and desktop GUI development. The original implementations and useful technical comments are preserved. Some scripts illustrate early development approaches and are not production-ready.

## Repository layout

| Directory | Topics |
| --- | --- |
| `basics/` | Arithmetic, conditional logic, loops, bill splitting and ticket sales |
| `math-and-geometry/` | Unit conversion, surface area, paper dimensions and rope tension |
| `strings/` | String slicing, character selection, palindrome and substring operations |
| `collections/` | Lists, dictionaries, sets, duplicate detection and word frequencies |
| `file-processing/` | Reading, sorting and writing text files; baby-name dataset |
| `input-validation/` | Exception handling and password-rule validation |
| `object-oriented/` | Classes, state, encapsulation and inheritance examples |
| `gui/` | Tkinter widgets, callbacks, image display, pricing calculations and receipt generation |

## Desktop applications

- `gui/pizzanet/`: PizzaNet ordering application with size and crust selection, toppings, calculated tax, receipt and checkout callbacks.
- `gui/pizza-order-prototype/`: Earlier pizza ordering interface with a customer-name field and receipt display.
- `gui/solvay-conference/`: Historical conference image and interactive Tkinter widget example.

## Run the examples

Use Python 3.10+ (standard library only for the complete examples). For GUI scripts, use a Python installation with Tkinter and a graphical desktop. Run each script from its own directory so relative image and text-data paths resolve correctly. For example:

```sh
cd gui/pizzanet
python pizza_order_app.py
```

The baby-name script reads `babynames.txt` and creates `boynames.txt` and `girlnames.txt`. The reverse-lines script requires an `input.txt` file supplied by the user and writes `output.txt`.

## Verification and limitations

All 36 scripts were checked for Python syntax validity. The code's abstract syntax trees were compared with the original sources, allowing only the two GUI asset filename changes; executable logic was otherwise retained. Full runtime and GUI testing were not performed. The `limousine.py` example expects a Car interface not provided by the supplied `car.py`, and `forgetful_critter.py` requires an unavailable `critter` module and has a method-signature mismatch. The two `Manager` definitions illustrate variants; the later definition shadows the earlier one. The palindrome implementation and other early examples may have logical edge cases. The password validator demonstrates character checks, not secure authentication; use example strings rather than real passwords.

Original image and dataset assets are included for local use. Their redistribution rights have not been independently verified; check permissions before publishing them. No license is asserted over third-party material.
