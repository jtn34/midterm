# Advanced Python Calculator for Software Engineering Graduate Course

## Project Overview

This project is a modular command-line calculator application built in Python, designed around key software engineering principles such as extensibility, maintainability, and scalability. The application features a robust REPL (Read-Eval-Print Loop) interface, a dynamic plugin system, calculation history management with Pandas, and comprehensive logging and configuration capabilities. It leverages multiple design patterns to ensure clean architecture and code reuse.

## Core Functionalities
REPL Interface: Users interact with the calculator in real-time, executing arithmetic commands like add, subtract, multiply, and divide. Users can also invoke history and plugin-related commands directly from the REPL.

Plugin System: New commands are seamlessly integrated using a dynamic plugin loader. This enables modular development without altering core code. The menu command lists all available plugins dynamically.

Calculation History (via Pandas): All operations are stored in a CSV-backed history system. Users can view, load, clear, and delete historical calculation records through REPL commands.

Logging (with ENV Configuration): All activities (commands run, errors, file operations) are logged with severity levels (INFO, WARNING, ERROR). Log level and file path are set dynamically via environment variables (LOG_LEVEL, LOG_FILE).

Environment Variables: Used for configuring logging behavior and file paths, promoting flexibility and production-readiness.

## Design Patterns Used
Command Pattern: Each command (e.g., AddCommand, HistoryCommand) inherits from a base Command class, encapsulating execution logic and maintaining a clean REPL command structure.

Factory Method Pattern: The CommandFactory dynamically registers and instantiates commands based on user input and available plugin modules.

Facade Pattern: HistoryManager abstracts away complex Pandas operations, providing a simplified interface for file and data management.

Singleton Pattern: The logger configuration behaves like a singleton, ensuring consistent logging behavior across the application.

Strategy Pattern: Can be optionally applied to implement different calculation strategies or logging behaviors depending on future requirements.

## Testing, Logging, and Standards
Test Coverage: The project is tested using Pytest with a minimum of 90% coverage, validating arithmetic operations, plugin loading, and history management.

Code Quality: Enforced through Pylint to meet PEP8 standards. Clean and readable code structure is maintained throughout.

Logging Practices: Logging is applied across command execution, plugin loading, and error handling. This ensures observability and easier debugging.

LBYL vs EAFP: Exception handling throughout the code follows Pythonic principles. For instance, file access and plugin loading employ EAFP to gracefully handle missing files or imports, while LBYL is used to check the existence of the history file before reading.

## Final Statement
Was stuck on commands for almost two hours, finally resolved everthing and the calaculator can operate and complete functions.
## 📽️ Demo Video

Watch the full demonstration here: [Calculator Demo Video](https://drive.google.com/file/d/11ShVReSW9mzxVcrC2Uoj_cN_66kc8TuA/view?usp=sharing)

<img src="https://drive.google.com/file/d/11ShVReSW9mzxVcrC2Uoj_cN_66kc8TuA/view?usp=sharing" width="500" />
