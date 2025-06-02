# DM-Wizard

DM-Wizard is a Telegram bot designed to assist with Discrete Mathematics (DM) problems. The bot provides a user-friendly interface for solving various combinatorial and logical problems, including factorials, permutations, combinations, circular permutations, logic expressions, and more.

## Features

- **King Polynomial Calculation**: Solve board-based King Polynomial problems by providing board configurations.
- **Logical Calculator**: Enter logical expressions to evaluate truth values and count satisfying assignments.
- **DM Calculator**: Includes the following discrete math operations:
  - **Factorial**
  - **Circular Permutation**
  - **Permutation**
  - **Combination**
- **Red-Handed Problem Solver**: Calculate the number of ways to distribute items with constraints.

## How It Works

The bot uses interactive Telegram inline buttons to guide users through the selection of operations. Each operation prompts for the necessary input format and provides results directly in the chat.

### Supported Operations and Input Formats

- **King Polynomial**: Enter the board description; e.g.,
  ```
  3 3
  0 0 0
  0 0 0
  0 1 0
  ```
- **Logical Calculator**: Enter any logical expression using `and`, `or`, `not`, and parentheses.
- **Factorial**: Enter a number or an expression like `10!!!`.
- **Circular Permutation**: Enter the problem statement as prompted.
- **Permutation/Combination**: Enter two numbers separated by a space, e.g., `5 2`.
- **Red-Handed**: Enter the distribution problem as instructed (see bot for details).

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/Alireza-Sobhdoost/DM-Wizard.git
   ```
2. Install dependencies:
   ```bash
   pip install python-telegram-bot
   ```
3. Set your Telegram Bot token:
   - The bot expects a `Token.py` file with a `getToken()` method that returns your bot token.
4. Run the bot:
   ```bash
   python TelegramBot.py
   ```

## Code Structure

- `TelegramBot.py`: Main bot logic, command, and message handlers.
- `DmCalc.py`: Mathematical functions for factorial, permutation, combination, and circular permutation.
- `Logic.py`: Logic expression processing and evaluation.
- `KingPolynomial.py` & `RedHanded.py`: Specialized problem solvers (imported by the bot).

## Logging

All bot interactions and errors are logged to `bot_log.txt` for debugging and auditing.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change or add.

## License

This project is licensed under the MIT License.

---

**Author:** Alireza Sobhdoost
