def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value in (0, 1):
                return bool(value)
            else:
                print("Please enter 0 or 1.")
        except ValueError:
            print("Invalid input! Please enter 0 or 1.")

def conjunction(A, B):
    return A and B

def disjunction(A, B):
    return A or B

def negation(A):
    return not A

def implication(A, B):
    return not A or B

def biconditional(A, B):
    return A == B

def display_results(A, B):
    print(f"\nResults for A = {int(A)}, B = {int(B)}:")
    print(f"A AND B: {int(conjunction(A, B))}")
    print(f"A OR B: {int(disjunction(A, B))}")
    print(f"NOT A: {int(negation(A))}")
    print(f"A IMPLIES B: {int(implication(A, B))}")
    print(f"A IF AND ONLY IF B: {int(biconditional(A, B))}")

def generate_truth_table():
    print("\nTruth Table:")
    print("A B | AND OR NOT(A) A->B A<->B")
    for A in [True, False]:
        for B in [True, False]:
            print(f"{int(A)} {int(B)} |  {int(conjunction(A, B))}   {int(disjunction(A, B))}   {int(negation(A))}    {int(implication(A, B))}    {int(biconditional(A, B))}")

def main():
    print("Logical Operations and Truth Table Generator")
    while True:
        print("\nMenu:")
        print("1. Evaluate logical operations")
        print("2. Generate truth table")
        print("3. Run test cases")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            A = get_input("Enter value for A (0 or 1): ")
            B = get_input("Enter value for B (0 or 1): ")
            display_results(A, B)
        elif choice == '2':
            generate_truth_table()
        elif choice == '3':
            run_test_cases()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

def run_test_cases():
    print("\nRunning test cases...")

    # Normal cases
    assert conjunction(True, True) == True, "Test case 1 failed"
    assert disjunction(True, False) == True, "Test case 2 failed"
    assert implication(False, True) == True, "Test case 3 failed"

    # Edge cases
    assert negation(True) == False, "Test case 4 failed"
    assert implication(True, False) == False, "Test case 5 failed"
    assert biconditional(False, False) == True, "Test case 6 failed"

    print("All test cases passed!")

if __name__ == "__main__":
    main()
