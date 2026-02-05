# MySQL Database GUI: Project Overview

This project is a desktop application that provides a graphical user interface (GUI) to perform CRUD (Create, Read, Update, Delete) operations on a MySQL database. Built using Python's `tkinter` library, it allows users to interact with a database named `gui` and a table also named `gui` without writing manual SQL queries.

## 🌟 Key Features

* **Database Automation**: Automatically creates the `gui` database and the required table (`Name` varchar, `Age` int) if they do not already exist upon connection.
* **CRUD Operations**:
    * **Insert**: Adds new records containing a name and age.
    * **Update**: Modifies the age of an existing record based on the provided name.
    * **Delete**: Removes a record from the table using the name as a reference.
    * **Select**: Queries and displays the age for a specific name.
* **Data Visualization**: Includes a "Show All" feature that retrieves and displays every record stored in the table via a message box.
* **User Feedback**: Uses modal message boxes to confirm successful operations, warn about input errors, or display connection issues.

## 🛠️ Technology Stack

* **Frontend**: `tkinter` (Python's standard GUI package).
* **Database Backend**: MySQL.
* **Connector**: `mysql-connector-python` (`msc`) for managing communication between the Python application and the MySQL server.

## 📁 Project Structure

* `main.py`: The single-file entry point containing the `MySQLDatabaseGUI` class. It manages the window layout, database connection logic, and all event-driven functions for the buttons.

## 🚀 Getting Started

1. **Prerequisites**:
    * Ensure a MySQL server is running on `localhost`.
    * Install the required connector:
      ```bash
      pip install mysql-connector-python
      ```
2. **Configuration**:
    * Open `main.py`.
    * Update the `password` field in the `msc.connect` calls (currently set to `"634237"`) to match your local MySQL root password.
3. **Run the Application**:
    ```bash
    python main.py
    ```

## 📝 Usage

* **Connection**: Click **"Connect to MySQL"** first to initialize the database and enable the CRUD operation buttons.
* **Adding Data**: Enter a name and age in the provided text fields and click **"Insert"**.
* **Searching**: Enter a name and click **"Select"** to find a specific person's age.
* **Cleanup**: The application automatically empties the input fields after successful data insertion, updates, or deletions.
