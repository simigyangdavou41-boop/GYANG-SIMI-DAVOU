"""
CSL 112: Introduction to Advanced Level Programming
Academic Portal Module — Encapsulation & Secure Class Design

Author: [Your Name]
Matric No: [Your Matric Number]
Date: 29th July 2026
"""


class Student:
    """
    Represents a student in the Academic Portal.

    All sensitive attributes (matric_number, full_name, cgpa, tuition_balance)
    are stored as private attributes and can only be accessed or modified
    through validated getter and setter methods, enforcing encapsulation.
    """

    def __init__(self, matric_no: str, name: str, initial_balance: float):
        """
        Initialises a new Student instance with validated inputs.

        Args:
            matric_no (str): The student's unique matriculation number.
            name (str): The student's full name.
            initial_balance (float): The initial tuition balance (must be >= 0).

        Raises:
            ValueError: If matric_no is empty or initial_balance is negative.
        """
        if not isinstance(matric_no, str) or matric_no.strip() == "":
            raise ValueError(
                "Invalid matric number: matric_no must be a non-empty string."
            )

        if initial_balance < 0:
            raise ValueError(
                f"Invalid tuition balance: ₦{initial_balance:,.2f} is negative. "
                "Tuition balance cannot be less than zero."
            )

        # Private attributes — name-mangled to prevent direct external access
        self.__matric_number: str = matric_no.strip()
        self.__full_name: str = name.strip()
        self.__cgpa: float = 0.00
        self.__tuition_balance: float = initial_balance

        print(f"[SYSTEM] Student record created for {self.__full_name} ({self.__matric_number}).")

    # ── Getters ────────────────────────────────────────────────────────────────

    def get_matric_number(self) -> str:
        """Returns the student's matriculation number."""
        return self.__matric_number

    def get_full_name(self) -> str:
        """Returns the student's full name."""
        return self.__full_name

    def get_cgpa(self) -> float:
        """Returns the student's current CGPA."""
        return self.__cgpa

    def get_tuition_balance(self) -> float:
        """Returns the student's outstanding tuition balance."""
        return self.__tuition_balance

    # ── Mutators / Setters ─────────────────────────────────────────────────────

    def update_cgpa(self, new_cgpa: float) -> None:
        """
        Updates the student's CGPA after validating the new value.

        Args:
            new_cgpa (float): The new CGPA value (must be between 0.00 and 5.00).

        Raises:
            TypeError: If new_cgpa is not a number.
            ValueError: If new_cgpa is outside the valid range [0.00, 5.00].
        """
        if not isinstance(new_cgpa, (int, float)):
            raise TypeError(
                f"Invalid type: CGPA must be a numeric value, got {type(new_cgpa).__name__}."
            )

        if not (0.00 <= new_cgpa <= 5.00):
            raise ValueError(
                f"Invalid CGPA: {new_cgpa} is out of bounds. "
                "CGPA must be between 0.00 and 5.00 inclusive."
            )

        self.__cgpa = float(new_cgpa)
        print(f"[UPDATE] CGPA for {self.__full_name} updated to {self.__cgpa:.2f}.")

    def pay_tuition(self, amount: float) -> None:
        """
        Processes a tuition payment, reducing the outstanding balance.

        Args:
            amount (float): The payment amount (must be greater than 0).

        Raises:
            TypeError: If amount is not a number.
            ValueError: If amount is zero or negative, or exceeds the balance.
        """
        if not isinstance(amount, (int, float)):
            raise TypeError(
                f"Invalid type: Payment amount must be numeric, got {type(amount).__name__}."
            )

        if amount <= 0:
            raise ValueError(
                f"Invalid payment: ₦{amount:,.2f} is not a positive amount. "
                "Payment must be greater than zero."
            )

        if amount > self.__tuition_balance:
            raise ValueError(
                f"Overpayment rejected: ₦{amount:,.2f} exceeds the outstanding "
                f"balance of ₦{self.__tuition_balance:,.2f}."
            )

        self.__tuition_balance -= amount
        print(
            f"[PAYMENT] ₦{amount:,.2f} payment received for {self.__full_name}. "
            f"Remaining balance: ₦{self.__tuition_balance:,.2f}."
        )

    # ── String Representation ──────────────────────────────────────────────────

    def __str__(self) -> str:
        return (
            f"Student({self.__matric_number} | {self.__full_name} | "
            f"CGPA: {self.__cgpa:.2f} | Balance: ₦{self.__tuition_balance:,.2f})"
        )

    def __repr__(self) -> str:
        return (
            f"Student(matric_no='{self.__matric_number}', name='{self.__full_name}', "
            f"cgpa={self.__cgpa}, tuition_balance={self.__tuition_balance})"
        )

    # ── Destructor ─────────────────────────────────────────────────────────────

    def __del__(self) -> None:
        """
        Destructor — called when the Student object is garbage-collected.
        Logs that the student session has been safely closed.
        """
        # Guard against accessing mangled names if partially initialised
        matric = getattr(self, "_Student__matric_number", "UNKNOWN")
        name = getattr(self, "_Student__full_name", "UNKNOWN")
        print(
            f"[CLEANUP] Student record session for {name} ({matric}) "
            "has been safely closed and deallocated from memory."
        )


# ──────────────────────────────────────────────────────────────────────────────


class Department:
    """
    Represents an academic department that manages a collection of Student objects.
    """

    def __init__(self, dept_name: str):
        """
        Initialises a Department with a name and an empty student list.

        Args:
            dept_name (str): The name of the department.
        """
        self.dept_name: str = dept_name
        self.__students_list: list[Student] = []
        print(f"[SYSTEM] Department '{self.dept_name}' initialised.")

    def add_student(self, student_object) -> None:
        """
        Adds a validated Student instance to the department roster.

        Args:
            student_object: Must be a Student instance.

        Raises:
            TypeError: If student_object is not a Student instance.
            ValueError: If a student with the same matric number already exists.
        """
        if not isinstance(student_object, Student):
            raise TypeError(
                f"Invalid input: Expected a Student instance, "
                f"got {type(student_object).__name__}."
            )

        # Prevent duplicate enrolment
        existing_matrics = [s.get_matric_number() for s in self.__students_list]
        if student_object.get_matric_number() in existing_matrics:
            raise ValueError(
                f"Duplicate entry: A student with matric number "
                f"'{student_object.get_matric_number()}' is already enrolled."
            )

        self.__students_list.append(student_object)
        print(
            f"[ENROL] {student_object.get_full_name()} added to {self.dept_name}. "
            f"Total students: {len(self.__students_list)}."
        )

    def get_student_count(self) -> int:
        """Returns the number of students currently enrolled in the department."""
        return len(self.__students_list)

    def generate_honors_roll(self) -> None:
        """
        Prints the Honours Roll — students with a CGPA of 3.50 or above.
        Reads student data exclusively through public getter methods.
        """
        print(f"\n{'═' * 55}")
        print(f"  🏅  HONOURS ROLL — {self.dept_name.upper()}")
        print(f"{'═' * 55}")

        honors_students = [
            s for s in self.__students_list if s.get_cgpa() >= 3.50
        ]

        if not honors_students:
            print("  No students currently qualify for the Honours Roll (CGPA ≥ 3.50).")
        else:
            for rank, student in enumerate(
                sorted(honors_students, key=lambda s: s.get_cgpa(), reverse=True),
                start=1,
            ):
                print(
                    f"  {rank}. {student.get_full_name():<25} "
                    f"| {student.get_matric_number():<12} "
                    f"| CGPA: {student.get_cgpa():.2f}"
                )

        print(f"{'═' * 55}\n")

    def __str__(self) -> str:
        return f"Department(name='{self.dept_name}', students={len(self.__students_list)})"
