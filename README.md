![LastCommit-Ecommerce_Project](https://img.shields.io/github/last-commit/ecopque/grocerystore_project?logo=&logoColor=white&label=/grocerystore_project&color=9bf12&&style=flat)&nbsp;
# Grocery Store Project

## Inventory and Sales Management System

This project is an inventory and sales management system developed using pure Python, focusing on simplicity and organization. The system adopts the Model-View-Controller (MVC) architecture to ensure a well-defined and maintainable codebase. The goal was to create a solution using Python concepts, avoiding functions like `map`, `filter`, `lambda`, and others.

### Technologies Used

- **Python 3.11**: The main programming language used to develop the project.
- **MVC Architecture**: A design pattern used to separate concerns and responsibilities.
- **File System**: Utilization of text files to store data (e.g., categories, customers, products).

## Project Structure

The project is organized into three main layers according to the MVC architecture:

- **Model**: Represents the data and the interactions with the data storage (text files).
- **View**: Contains the user interface (UI), which is command-line-based.
- **Controller**: Handles business logic and interacts with both the Models and Views.
- **DAO**: Manages data interactions with the text files, providing methods for reading, writing, and updating data.

###################### INSERT MIND MAP


## Features

The system offers the following features, divided by operation categories:

### 1. **Categories**:
- Register, remove, update, and list categories.

### 2. **Inventory/Stock**:
- Register, remove, update, and view products.

### 3. **Suppliers**:
- Register, remove, update, and list suppliers.

### 4. **Customers**:
- Register, remove, update, and view customers.

### 5. **Employees**:
- Register, remove, update, and list employees.

### 6. **Sales**:
- Register new sales.
- Generate total sales reports.
- Show sales within a specific date range.

## Execution

Once the application starts, you will be presented with an interactive menu in the terminal that allows you to manage categories, inventory, suppliers, customers, employees, and sales. Each category has its own submenu for interacting with the system.

## Final Considerations

This project was developed with the goal of learning and applying pure Python concepts, as well as the MVC architecture. The choice to use Python without external dependencies was made to keep the code simple and easy to understand. The inventory and sales management features are implemented in a modular way, ensuring maintainability and readability.

## Contributions

If you'd like to contribute to this project, feel free to open a pull request with improvements or bug fixes!