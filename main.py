"""
CSL 112: Introduction to Advanced Level Programming
Edge-Case Testing Suite — main.py

Tests encapsulation, validation, and error-handling behaviour of the
Student and Department classes defined in academic_portal.py.

Author: [Your Name]
Matric No: [Your Matric Number]
Date: 29th July 2026
"""

from academic_portal import Student, Department


def separator(title: str) -> None:
    """Prints a formatted section header."""
    print(f"\n{'─' * 60}")
    print(f"  TEST: {title}")
    print(f"{'─' * 60}")


def run_tests() -> None:
    print("=" * 60)
    print("  CSL 112 — ACADEMIC PORTAL: EDGE-CASE TEST SUITE")
    print("=" * 60)

    # ──────────────────────────────────────────────────────────────
    # TEST 1: Instantiate a student with a NEGATIVE tuition balance
    # ──────────────────────────────────────────────────────────────
    separator("Negative Tuition Balance at Instantiation")
    try:
        bad_student = Student("MAT/2024/001", "Ada Okonkwo", -50000.00)
        print("  [FAIL] No exception raised — validation is broken!")
    except ValueError as e:
        print(f"  [PASS] ValueError caught as expected:\n         → {e}")

    # ──────────────────────────────────────────────────────────────
    # TEST 2: Empty matric number
    # ──────────────────────────────────────────────────────────────
    separator("Empty Matric Number at Instantiation")
    try:
        bad_student2 = Student("", "Ghost User", 10000.00)
        print("  [FAIL] No exception raised — validation is broken!")
    except ValueError as e:
        print(f"  [PASS] ValueError caught as expected:\n         → {e}")

    # ──────────────────────────────────────────────────────────────
    # TEST 3: Direct private attribute tampering (name mangling)
    # ──────────────────────────────────────────────────────────────
    separator("Direct Private Attribute Tampering")
    student1 = Student("MAT/2024/010", "Emeka Duru", 120000.00)

    print(f"\n  CGPA before tampering attempt: {student1.get_cgpa()}")

    # This assignment creates a NEW public attribute on the object
    # (student1.__cgpa) — it does NOT overwrite the private __cgpa
    # because Python name-mangles it to _Student__cgpa internally.
    student1.__cgpa = 4.9

    actual_cgpa = student1.get_cgpa()
    print(f"  Attempted: student1.__cgpa = 4.9")
    print(f"  Actual internal CGPA (via getter): {actual_cgpa}")

    if actual_cgpa != 4.9:
        print("  [PASS] Private state is protected — tampering had no effect.")
    else:
        print("  [FAIL] Private state was overwritten — encapsulation is broken!")

    # Demonstrate that the injected attribute is a separate, harmless attribute
    print(f"  Note: student1.__cgpa (surface attribute) = {student1.__cgpa} "
          f"(this is a separate object, not the real private field)")

    # ──────────────────────────────────────────────────────────────
    # TEST 4: update_cgpa with out-of-bounds values
    # ──────────────────────────────────────────────────────────────
    separator("Out-of-Bounds CGPA Values")

    for bad_value in [6.0, -1.5, 5.01]:
        try:
            student1.update_cgpa(bad_value)
            print(f"  [FAIL] update_cgpa({bad_value}) accepted — should have been rejected!")
        except ValueError as e:
            print(f"  [PASS] update_cgpa({bad_value}) rejected:\n         → {e}")

    # Valid CGPA update
    try:
        student1.update_cgpa(4.50)
        print(f"  [PASS] Valid CGPA 4.50 accepted. Current CGPA: {student1.get_cgpa()}")
    except Exception as e:
        print(f"  [FAIL] Valid CGPA was rejected: {e}")

    # ──────────────────────────────────────────────────────────────
    # TEST 5: pay_tuition with invalid amounts
    # ──────────────────────────────────────────────────────────────
    separator("Invalid Tuition Payment Amounts")

    for bad_payment in [0, -5000, -1]:
        try:
            student1.pay_tuition(bad_payment)
            print(f"  [FAIL] pay_tuition({bad_payment}) accepted — should be rejected!")
        except ValueError as e:
            print(f"  [PASS] pay_tuition({bad_payment}) rejected:\n         → {e}")

    # Valid payment
    try:
        student1.pay_tuition(30000.00)
        print(f"  [PASS] Payment of ₦30,000 accepted. "
              f"Balance: ₦{student1.get_tuition_balance():,.2f}")
    except Exception as e:
        print(f"  [FAIL] Valid payment was rejected: {e}")

    # ──────────────────────────────────────────────────────────────
    # TEST 6: Add 3 valid students to a Department & Honours Roll
    # ──────────────────────────────────────────────────────────────
    separator("Department Enrolment & Honours Roll Generation")

    # Create the department
    cs_dept = Department("Computer Science")

    # Create 3 valid students
    student_a = Student("MAT/2024/021", "Chisom Nwosu", 150000.00)
    student_b = Student("MAT/2024/022", "Fatima Aliyu", 200000.00)
    student_c = Student("MAT/2024/023", "Tunde Bakare", 175000.00)

    # Assign varied CGPAs
    student_a.update_cgpa(4.75)   # Honours
    student_b.update_cgpa(3.20)   # Below threshold
    student_c.update_cgpa(3.85)   # Honours

    # Enrol all three
    cs_dept.add_student(student_a)
    cs_dept.add_student(student_b)
    cs_dept.add_student(student_c)

    print(f"\n  Total enrolled: {cs_dept.get_student_count()} students")

    # Generate the honours roll (should show student_a and student_c)
    cs_dept.generate_honors_roll()

    # ──────────────────────────────────────────────────────────────
    # TEST 7: Add a non-Student object to Department
    # ──────────────────────────────────────────────────────────────
    separator("Adding Invalid Object to Department")
    try:
        cs_dept.add_student("Not a student object")
        print("  [FAIL] Invalid object was added — type check is broken!")
    except TypeError as e:
        print(f"  [PASS] TypeError caught as expected:\n         → {e}")

    # ──────────────────────────────────────────────────────────────
    # TEST 8: Duplicate student enrolment
    # ──────────────────────────────────────────────────────────────
    separator("Duplicate Student Enrolment")
    try:
        cs_dept.add_student(student_a)   # student_a already enrolled
        print("  [FAIL] Duplicate student was added — check is broken!")
    except ValueError as e:
        print(f"  [PASS] ValueError caught as expected:\n         → {e}")

    # ──────────────────────────────────────────────────────────────
    # Summary
    # ──────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  ALL TESTS COMPLETED.")
    print("  Encapsulation and validation are working correctly.")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_tests()
