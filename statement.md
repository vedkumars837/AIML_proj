# Project Statement
**Project Title:** Multi-Utility Unit Converter

## 1. Problem Statement
In academic, professional, and daily life scenarios, individuals frequently encounter the need to convert measurements between different systems (primarily Metric and Imperial). 

For example:
* A student needing to convert Celsius to Fahrenheit for a Physics problem.
* A traveler trying to understand road signs in Miles versus Kilometers.
* A shopper comparing product volumes in Gallons versus Liters.

Performing these conversions manually is **time-consuming**, **inefficient**, and **prone to human error**. While online tools exist, they require an active internet connection and can be distracting. There is a clear need for a lightweight, offline, and centralized tool that can perform these calculations instantly and accurately.

## 2. Scope of the Project
The scope of this project is limited to the development of a console-based application (CLI) using the Python programming language. 

**In Scope:**
* Implementation of four core conversion modules: **Weight**, **Length**, **Volume**, and **Temperature**.
* Bidirectional conversion logic (e.g., converting A to B and B to A).
* Implementation of basic error handling to manage non-numeric inputs.
* A menu-driven interface for user navigation.

**Out of Scope:**
* Graphical User Interface (GUI).
* Real-time data fetching (e.g., live currency exchange rates).
* Storage of user data or conversion history in a database.

## 3. Target Users
This application is designed for a broad range of users, including:
* **Students:** For quick assistance with Science and Mathematics homework.
* **Travelers:** For understanding local measurement units (distance, weather, fuel volume) in foreign countries.
* **Professionals:** Engineers or architects who need quick, rough estimates between unit systems.
* **General Users:** For domestic tasks like cooking (volume/weight) or health tracking.

## 4. High-Level Features
The Multi-Utility Unit Converter offers the following key features:

* **Centralized Dashboard:** A single main menu provides access to all different types of converters, eliminating the need for multiple tools.
* **Bidirectional Conversion:** Users can convert values both ways (e.g., Kilograms $\leftrightarrow$ Pounds) within the same module.
* **Robust Input Handling:** The system includes validation mechanisms to prevent crashes when users enter invalid data (such as text instead of numbers).
* **Continuous Operation:** The program utilizes a loop structure, allowing users to perform multiple distinct conversions in a single session without restarting the application.
* **Precision Output:** All calculation results are automatically rounded to two decimal places to ensure readability and relevance.
