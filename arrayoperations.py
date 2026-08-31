"""
Group Activity (Lab) - Python Array Operations Program
"""

numbers = []


# ---------- PASOJEL - Create List + User Input ----------
def create_list():
    global numbers
    numbers = []
    n = int(input("How many integers do you want to enter? "))
    for i in range(n):
        value = int(input(f"Enter integer {i + 1}: "))
        numbers.append(value)
    print("Array of integers:", numbers)


# ---------- TRANCE - Display + Largest Value ----------
def display_and_largest():
    if not numbers:
        print("The list is empty.")
        return
    print("All elements:", numbers)
    largest = max(numbers)
    print("Largest value:", largest)


# ---------- MUNSOD - Smallest Value + Average ----------
def smallest_and_average():
    if not numbers:
        print("The list is empty.")
        return
    smallest = min(numbers)
    print("Smallest value:", smallest)
    average = sum(numbers) / len(numbers)
    print("Average:", average)


# ---------- PAUMAR - Update + Insertion ----------
def update_and_insert():
    if not numbers:
        print("The list is empty. Add elements first.")
        return

    # Update an element
    index = int(input(f"Enter the index to update (0 to {len(numbers) - 1}): "))
    if 0 <= index < len(numbers):
        new_value = int(input("Enter the new value: "))
        numbers[index] = new_value
        print("Updated list:", numbers)
    else:
        print("Invalid index.")

    # Insert a new element
    insert_index = int(input(f"Enter the index to insert (0 to {len(numbers)}): "))
    insert_value = int(input("Enter the value to insert: "))
    if 0 <= insert_index <= len(numbers):
        numbers.insert(insert_index, insert_value)
        print("List after insertion:", numbers)
    else:
        print("Invalid index.")


# ---------- MARTOS - Deletion + Linear Search ----------
def delete_and_linear_search():
    if not numbers:
        print("The list is empty.")
        return

    # Deletion
    del_index = int(input("Enter position to delete: "))
    if 0 <= del_index < len(numbers):
        removed = numbers.pop(del_index)
        print(f"Removed: {removed}")
        print("New list:", numbers)
    else:
        print("Invalid position")

    if not numbers:
        return

    # Linear search
    search_val = int(input("Enter value to search: "))
    found = False
    for i in range(len(numbers)):
        if numbers[i] == search_val:
            print(f"Found at position {i}")
            found = True
            break
    if not found:
        print("Not found in the list")


# ---------- PANGAN - Sorting + Binary Search ----------
def sort_and_binary_search():
    if not numbers:
        print("The list is empty.")
        return

    # Sort the list
    numbers.sort()
    print("Sorted list:", numbers)

    # Binary search
    search_val = int(input("Enter value to search using binary search: "))
    low = 0
    high = len(numbers) - 1
    found = False

    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == search_val:
            print(f"Found at position {mid}")
            found = True
            break
        elif numbers[mid] < search_val:
            low = mid + 1
        else:
            high = mid - 1

    if not found:
        print("Not found in the list")


# ---------- MENU ----------
def show_menu():
    print("\n===== ARRAY OPERATIONS MENU =====")
    print("1. Create List + User Input")
    print("2. Display + Largest Value")
    print("3. Smallest Value + Average")
    print("4. Update + Insertion")
    print("5. Deletion + Linear Search")
    print("6. Sorting + Binary Search")
    print("0. Exit")


def main():
    actions = {
        "1": create_list,
        "2": display_and_largest,
        "3": smallest_and_average,
        "4": update_and_insert,
        "5": delete_and_linear_search,
        "6": sort_and_binary_search,
    }

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Exiting program. Goodbye!")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
