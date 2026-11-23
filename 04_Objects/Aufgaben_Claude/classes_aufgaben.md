# Classes

---

# Build a Bank Account System

## Problem

Implement a banking system that manages different account types, each with its own withdrawal and interest rules.

Your implementation must include three classes: `BankAccount`, `SavingsAccount`, and `CheckingAccount`.

## Requirements

1. `BankAccount` (base class)

* The constructor accepts `owner` and `balance` (default `0`).
* `deposit(amount)` adds the amount and returns `True`. If `amount <= 0`, nothing changes and it returns `False`.
* `withdraw(amount)` subtracts the amount and returns `True`. If `amount <= 0` or `amount > balance`, nothing changes and it returns `False`.
* `__str__()` returns `"Owner: $Balance"`, with two decimal places.

2. `SavingsAccount` (subclass of `BankAccount`)

* The constructor accepts `owner`, `balance`, and `rate` (a percentage).
* `add_interest()` increases the balance by `balance * rate / 100`.
* Uses `super()` to initialize inherited attributes.

3. `CheckingAccount` (subclass of `BankAccount`)

* The constructor accepts `owner`, `balance`, and `overdraft_limit`.
* Overrides `withdraw(amount)` so the balance may drop to `-overdraft_limit`, but no lower.
* Uses `super()` to initialize inherited attributes.

Constraints:

* Do not use `type()` or `isinstance()`.
* Do not duplicate `deposit()` in the subclasses.
* Do not use global variables or external libraries.

## Example

```python
acc = BankAccount("Anna", 100)
savings = SavingsAccount("Ben", 1000, 5)
checking = CheckingAccount("Cara", 100, 200)

print(acc.deposit(50))      # True
print(acc.withdraw(200))    # False
print(acc)                  # Anna: $150.00

savings.add_interest()
print(savings.balance)      # 1050.0

print(checking.withdraw(250))  # True
print(checking.balance)        # -150
print(checking.withdraw(100))  # False

accounts = [acc, savings, checking]
print(sum(a.balance for a in accounts))  # 1050.0
```

## Bonus Challenge — Unique Account IDs

Give every account a unique `account_id` that is assigned automatically (1, 2, 3, …) and shared across all account types. Add a class attribute `account_count` that tracks how many accounts exist.

```python
print(acc.account_id)             # 1
print(savings.account_id)         # 2
print(checking.account_id)        # 3
print(BankAccount.account_count)  # 3
```

Implement `__lt__` so accounts can be compared by balance:

```python
for a in sorted(accounts):
    print(a.owner)
# Cara
# Anna
# Ben
```

---

# Build a Shape Hierarchy

## Problem

Implement a geometry system where each shape calculates its own area and perimeter.

Your implementation must include three classes: `Shape`, `Rectangle`, and `Circle`.

## Requirements

1. `Shape` (base class)

* The constructor accepts `name`.
* `area()` and `perimeter()` raise `NotImplementedError`.
* `__str__()` returns `"Name: area=A, perimeter=P"`, with two decimal places.
* `__lt__(other)` compares shapes by area.

2. `Rectangle` (subclass of `Shape`)

* The constructor accepts `width` and `height`.
* Implements `area()` and `perimeter()`.
* Uses `super()` to set the name `"Rectangle"`.

3. `Circle` (subclass of `Shape`)

* The constructor accepts `radius`.
* Implements `area()` and `perimeter()` (circumference).
* Uses `super()` to set the name `"Circle"`.

Constraints:

* Use polymorphism. Do not use `type()` or `isinstance()`.
* You may import only the `math` module.
* Do not use global variables.

## Example

```python
r = Rectangle(3, 4)
c = Circle(1)
s = Rectangle(2, 2)

print(r.area())       # 12
print(r.perimeter())  # 14

print(r)  # Rectangle: area=12.00, perimeter=14.00
print(c)  # Circle: area=3.14, perimeter=6.28

shapes = [r, c, s]

print(round(sum(x.area() for x in shapes), 2))  # 19.14
print(max(shapes))                              # Rectangle: area=12.00, perimeter=14.00

for shape in sorted(shapes):
    print(round(shape.area(), 2))
# 3.14
# 4
# 12
```

## Bonus Challenge — Abstract Base Class

Turn `Shape` into an abstract base class using `abc`, with `area()` and `perimeter()` as abstract methods.

```python
Shape("Test")  # TypeError
```

Explain why this is safer than raising `NotImplementedError`.

---

# Build an Employee Payroll System

## Problem

Implement a payroll system that handles different employee types with different pay rules.

Your implementation must include three classes: `Employee`, `Manager`, and `Developer`.

## Requirements

1. `Employee` (base class)

* Define class attributes `role = "Employee"` and `company = "Acme"`.
* The constructor accepts `name` and `base_salary`. An invalid salary is stored as `0`.
* `monthly_pay()` returns the base salary.
* `__str__()` returns `"Name (Role): $Pay"`, with two decimal places.
* Add a `@staticmethod` named `is_valid_salary(amount)` that returns `True` if `amount >= 0`. Use it in the constructor.

2. `Manager` (subclass of `Employee`)

* The constructor accepts `name`, `base_salary`, and `bonus` (default `0`).
* Overrides `role` with `"Manager"`.
* Overrides `monthly_pay()` to return base salary plus bonus.
* Uses `super()` to initialize inherited attributes.

3. `Developer` (subclass of `Employee`)

* Define a class attribute `overtime_rate = 40`.
* The constructor accepts `name`, `base_salary`, and `overtime_hours` (default `0`).
* Overrides `role` with `"Developer"`.
* Overrides `monthly_pay()` to return base salary plus `overtime_hours * overtime_rate`.
* Uses `super()` to initialize inherited attributes.

Constraints:

* Use inheritance and method overriding. Do not use `type()` or `isinstance()` in your classes.
* `__str__()` must be defined only once, in `Employee`.
* Do not use global variables or external libraries.

## Example

```python
e = Employee("Anna", 3000)
m = Manager("Ben", 5000, 1000)
d = Developer("Cara", 4000, 10)

print(e.monthly_pay())  # 3000
print(m.monthly_pay())  # 6000
print(d.monthly_pay())  # 4400

print(e)  # Anna (Employee): $3000.00
print(m)  # Ben (Manager): $6000.00
print(d)  # Cara (Developer): $4400.00

print(Employee("Tom", -100).monthly_pay())  # 0

staff = [e, m, d]
print(sum(p.monthly_pay() for p in staff))             # 13400
print(max(staff, key=lambda p: p.monthly_pay()).name)  # Ben
```

## Bonus Challenge — Alternative Constructor

Add a `@classmethod` named `from_string(cls, text)` to `Employee`. It parses `"Name,Salary"` and returns an instance of the class it was called on.

```python
x = Developer.from_string("Max,4000")

print(type(x).__name__)  # Developer
print(x.monthly_pay())   # 4000
print(x.role)            # Developer
```

Explain why `@classmethod` is the right choice here instead of a `@staticmethod`.
