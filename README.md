# CSL 112 — Secure Student Academic Portal
### A Beginner-Friendly Guide to This Project

---

## What Is This Project?

This project is a **coursework assignment** for CSL 112 (Introduction to Advanced Level Programming). The goal is to build a small software system that manages student academic records — things like CGPA and tuition fees — in a **secure and controlled way**.

Think of it like a school's online portal where a student can check their balance or CGPA, but they **cannot just go in and change their score to 5.0** without the system checking if that's even a valid score first. That controlled, protected approach is what this assignment is all about.

---

## The Big Idea: Encapsulation

The core concept being practised here is called **Encapsulation** — one of the most important ideas in programming.

> **Encapsulation** means keeping sensitive data locked away inside a "capsule" (a class), so that it can only be read or changed through safe, official checkpoints.

**A real-world analogy:**
Imagine your bank account balance. You can't walk into the bank's database and type in a new number. Instead, you deposit money, and the bank's system checks if your deposit is valid before updating your balance. Encapsulation works the same way in code.

---

## Files in This Project

| File | What it does |
|---|---|
| `academic_portal.py` | The main code — defines what a Student and a Department *are* |
| `main.py` | A test script that tries to break the system with bad inputs |
| `student_uml.png` | A diagram (blueprint) showing how the classes are designed |
| `README.md` | This file — explains everything in plain English |
| `.gitignore` | Tells Git which files to ignore when saving your project |

---

## The Two Classes Explained

A **class** in programming is like a template or a blueprint. Just like a form has fields for "Name", "Date of Birth", etc., a class defines what information an object holds and what it can do.

### Student Class

This is the blueprint for a single student record. Every student created from this blueprint will have:

**Private Information (locked away, cannot be touched directly):**
- `matric_number` — The student's unique ID (e.g. MAT/2024/010)
- `full_name` — The student's name
- `cgpa` — Their Grade Point Average (starts at 0.00)
- `tuition_balance` — How much fees they still owe

**The Rules (what the system checks before allowing any change):**

| Action | Rule |
|---|---|
| Create a student | Matric number must not be empty. Balance cannot be negative. |
| Update CGPA | New CGPA must be between **0.00 and 5.00**. Nothing outside that. |
| Pay tuition | Payment amount must be **greater than zero**. |

If anyone tries to break these rules (e.g. set a CGPA of 6.0), the system **raises an error** and rejects it. This is called **validation**.

---

### Department Class

This is the blueprint for a Department (e.g. Computer Science). A department:

- Holds a **list of Student objects**
- Only accepts real, valid Student objects into that list (not random data)
- Can generate an **Honours Roll** — a list of every student with a CGPA of **3.50 or above**

---

## How the Security Works (Name Mangling)

In Python, if you name a variable with **two underscores** in front (like `__cgpa`), Python automatically hides it from the outside world. This is called **name mangling**.

For example, if someone tries to cheat by doing this:

```python
student.__cgpa = 4.9
```

Python doesn't actually change the real internal CGPA. Instead, it creates a harmless, separate variable that has no effect. The real `__cgpa` stays exactly as it was. The test in `main.py` proves this.

---

## What main.py Tests

The test file tries **8 different attacks** on the system to make sure nothing can be broken:

1. Create a student with a **negative balance** — System rejects it
2. Create a student with an **empty matric number** — System rejects it
3. Try to **directly change CGPA** from outside — Python blocks it (name mangling)
4. Set CGPA to **6.0, -1.5, or 5.01** — All rejected as out of range
5. Make a payment of **zero or a negative amount** — Rejected
6. Add **3 valid students** to a Department and print the Honours Roll — Works correctly
7. Try to add a **random string** (not a student) to the Department — Rejected
8. Try to **enrol the same student twice** — Rejected as a duplicate

---

## The UML Diagram (student_uml.png)

UML stands for **Unified Modelling Language**. It is a standard way to draw a blueprint of your classes *before* you start coding — like an architect drawing a floor plan before building a house.

The diagram shows:
- The two classes (Student and Department)
- Every attribute and method, with visibility symbols:
  - `-` (minus) = **Private** — only accessible from inside the class
  - `+` (plus) = **Public** — accessible from anywhere
- An arrow showing that Department *manages* Student objects

---

## Git and GitHub (Version Control)

**Git** is a tool that tracks every change you make to your code over time — like "track changes" in Microsoft Word, but for code.

**GitHub** is a website where you store and share your Git project online.

For this assignment, you need to make **at least 3 saves (commits)** with meaningful labels:

```
1. docs: add UML diagram for Student class
2. feat: implement Student class with encapsulated setters/getters
3. test: verify edge case validation in main runner
```

Then push it all to a public GitHub repository named **CSL112-Lab-Encapsulation** and add your lecturer (Nannim) as a collaborator.

---

## How to Run the Project

Open your terminal, navigate to this folder, and type:

```bash
python main.py
```

You will see all 8 tests run and confirm that the system is working correctly.

---

## Summary Table

| Concept | What It Means in Simple Terms |
|---|---|
| **Class** | A blueprint/template for creating objects |
| **Object** | A real instance created from a class (e.g. one specific student) |
| **Encapsulation** | Locking sensitive data away so it can only be changed safely |
| **Private attribute** | A variable only the class itself can touch directly |
| **Getter** | A method that lets you *read* a private value |
| **Setter / Mutator** | A method that lets you *change* a private value — with validation |
| **Validation** | Checking that a value makes sense before accepting it |
| **Destructor** | Code that runs automatically when an object is deleted from memory |
| **UML Diagram** | A visual blueprint of a class and its relationships |
| **Git commit** | A saved snapshot of your code at a point in time |

---

*CSL 112 — Independent Lab Activity | Submission: 29th July 2026*
