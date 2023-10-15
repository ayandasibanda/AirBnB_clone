AirBnB Clone Project
Project Description
Welcome to the AirBnB clone project! This project aims to create a simplified version of the popular AirBnB platform. The development will be carried out in several steps, starting with the implementation of a command-line interpreter to manage AirBnB objects. This command interpreter will serve as the foundation for subsequent tasks, including HTML/CSS templating, database storage, API integration, and front-end development.

Command Interpreter
The command interpreter is a crucial component of the AirBnB clone project. It provides a user-friendly interface for managing various AirBnB objects. Here are the key aspects of the command interpreter:

Initialization
The command interpreter relies on a parent class called BaseModel. This class is responsible for the initialization, serialization, and deserialization of future instances.

Serialization/Deserialization Flow
The serialization/deserialization process involves the following steps:

1. Instance creation
2. Conversion to a dictionary
3. Transformation to a JSON string
4. Storage in a file

This flow ensures that object data can be easily saved, retrieved, and manipulated throughout the project.

Classes
Several classes are created to represent different AirBnB objects, such as User, State, City, Place, etc. These classes inherit from the BaseModel class, establishing a hierarchical structure.

Storage Engine
The first abstracted storage engine implemented in this step is the File storage. It allows the program to save and retrieve data efficiently.

Unit Tests
Comprehensive unit tests are created to validate the functionality of all classes and the storage engine. This ensures the reliability and correctness of the implemented features.
