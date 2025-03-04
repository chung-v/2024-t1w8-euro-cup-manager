from file_operations import load_matches, save_matches
from match_operations import display_matches, add_match, total_goals, high_scoring_matches

FILE_PATH = '../data/matches.json' # In captitals as the file path is constant

def main():
    matches = load_matches(FILE_PATH)

    if not matches:
        print("No matches loaded or an error occurred. Exiting.")
        return
    while True:
        print("\nEuro Cup Manager:")
        print("1. Display all matches")
        print("2. Add a new match")
        print("3. Calculate the total goals")
        print("4. Display high-scoring matches")
        print("5. Save and Exit")

        """
        Executing the features
        """

        # match case:
        #     case 1:
        #     case 2:

        choice = input("Choose an option: ")

        if choice == '1':
            display_matches(matches)
        elif choice == '2':
            add_match(matches)
        elif choice == '3': # Need to print as it is returning a value
            print(f"Total goals scored: {total_goals(matches)}.")
        elif choice == '4':
            high_scoring = high_scoring_matches(matches, 3)
            display_matches(high_scoring)
        elif choice == '5':
            try:
                save_matches(FILE_PATH, matches)
                break
            except Exception as e:
                print(f"Error saving matches: {e}.")
        else:
            print("Invalid choice. Please try again.")

"""
Executing the file
"""

# main()

if __name__ == "__main__":
    main()