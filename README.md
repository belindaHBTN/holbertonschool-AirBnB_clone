# AirBnB Clone - The Console

This project is the first step towards building an AirBnB clone, and it focuses on creating a command-line interface (CLI) to manage AirBnB objects.

## Command Interpreter

The command interpreter allows you to perform various operations on AirBnB objects. Here's how to get started with it:

### Starting the Command Interpreter

To start the command interpreter, run the following command:

```
$ ./console.py
```

### Using the Command Interpreter

Once you are inside the command interpreter, you can use the following commands:

- `help`: Display the list of available commands and their descriptions.
- `quit`: Exit the command interpreter.

### Examples

Here are a few examples of how to use the command interpreter:

1. Get help:

```
(hbnb) help
```
2. Quit the command interpreter:
```
(hbnb) quit
```
## Project Information

The AirBnB clone project involves creating a command interpreter and building various classes to manage AirBnB objects. Some key points about the project are:

- The parent class `BaseModel` handles initialization, serialization, and deserialization of instances.
- Objects can be serialized and deserialized between instances, dictionaries, JSON strings, and files.
- Several classes (e.g., `User`, `State`, `City`, `Place`) inherit from `BaseModel` to represent different AirBnB objects.
- The project includes a file storage engine for data persistence.
- Unittests are provided to validate the classes and storage engine.

## What is a Command Interpreter?

The command interpreter in this project is similar to a shell, but it is specifically designed for managing AirBnB objects. The command interpreter allows you to perform actions such as creating new objects, retrieving objects from files or databases, updating object attributes, and more.

## Execution

The command interpreter can be used in interactive mode or non-interactive mode:

### Interactive Mode

In interactive mode, run the `console.py` file without any arguments:
```
$ ./console.py
```
### Non-Interactive Mode

In non-interactive mode, you can provide commands through pipes or input redirection. For example:
```
$ echo "help" | ./console.py
```
or
```
$ cat test_help | ./console.py
```
That's it! You're ready to start using the AirBnB clone command interpreter.
