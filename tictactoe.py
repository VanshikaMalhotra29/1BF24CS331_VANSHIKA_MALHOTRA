import random


def print_board(a):
  """Prints the 3x3 game board."""
  print("\n")
  for row in a:
    print(" | ".join(row))
    print("-" * 9)
  print("\n")


def check_winner(a, symbol):
  """Checks if the given symbol has met any of the 8 winning combinations."""
  # Combinations mapped to 2D array indices:
  # (1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)
  combinations = [
      # Rows
      [(0, 0), (0, 1), (0, 2)],
      [(1, 0), (1, 1), (1, 2)],
      [(2, 0), (2, 1), (2, 2)],
      # Columns
      [(0, 0), (1, 0), (2, 0)],
      [(0, 1), (1, 1), (2, 1)],
      [(0, 2), (1, 2), (2, 2)],
      # Diagonals
      [(0, 0), (1, 1), (2, 2)],
      [(0, 2), (1, 1), (2, 0)],
  ]

  for combo in combinations:
    if all(a[r][c] == symbol for r, c in combo):
      return True
  return False


def is_board_full(a):
  """Checks if all positions are filled."""
  for row in a:
    for cell in row:
      if cell not in ["X", "O"]:
        return False
  return True


def play_tic_tac_toe():
  # Step 1: Let user choose 'X' or 'O', computer gets the remaining symbol[span_1](start_span)[span_1](end_span)
  user_symbol = input("Choose 'X' or 'O': ").upper()
  while user_symbol not in ["X", "O"]:
    user_symbol = input("Invalid choice. Please choose 'X' or 'O': ").upper()

  comp_symbol = "O" if user_symbol == "X" else "X"
  print(f"Computer is automatically assigned: {comp_symbol}")

  # Step 2: Initialize a 2D array a[3][3][span_2](start_span)[span_2](end_span)
  a = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]
  print_board(a)

  # Step 6: Repeat steps 3-5 until a player wins or all positions are filled[span_3](start_span)[span_3](end_span)
  while True:
    # Step 3: Ask user for input position[span_4](start_span)[span_4](end_span)
    try:
      pos = int(input("Enter position (1-9): "))
      if pos < 1 or pos > 9:
        print("Invalid position. Choose a number between 1 and 9.")
        continue

      r, c = (pos - 1) // 3, (pos - 1) % 3

      # if empty, enter symbol in that position; else invalid position[span_5](start_span)[span_5](end_span)
      if a[r][c] not in ["X", "O"]:
        a[r][c] = user_symbol
      else:
        print("Position already taken. Invalid position.")
        continue
    except ValueError:
      print("Please enter a valid numeric input.")
      continue

    print_board(a)

    # Check if user won
    if check_winner(a, user_symbol):
      print("Congratulations! You win!")
      break

    # Step 7: If all positions are filled and nobody wins, display 'DRAW[span_6](start_span)'[span_6](end_span)
    if is_board_full(a):
      print("DRAW")
      break

    # Step 4: Randomly generate computer's position[span_7](start_span)[span_7](end_span)
    print("Computer's turn...")
    while True:
      comp_pos = random.randint(1, 9)
      cr, cc = (comp_pos - 1) // 3, (comp_pos - 1) % 3

      # if empty, enter symbol; else regenerate position[span_8](start_span)[span_8](end_span)
      if a[cr][cc] not in ["X", "O"]:
        a[cr][cc] = comp_symbol
        break

    print_board(a)

    # Step 5: Check winner[span_9](start_span)[span_9](end_span)
    if check_winner(a, comp_symbol):
      print("Computer wins! Better luck next time.")
      break

    # Check draw condition again after computer's move
    if is_board_full(a):
      print("DRAW")
      break

  # Step 8: End[span_10](start_span)[span_10](end_span)
  print("Game Over.")


if __name__ == "__main__":
  play_tic_tac_toe()

