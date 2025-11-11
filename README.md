# Complaint Management System

This is a Django-based complaint management system designed for a university or college. It allows students to file complaints against various departments and also includes a polling feature for voting on lecturers.

## Features

*   **User Authentication:** Students can register and log in to the system.
*   **Complaint Submission:** Authenticated users can submit complaints, specifying a title, description, and the relevant department.
*   **View Complaints:** Users can view a list of all submitted complaints, sorted by date.
*   **Lecturer Polling:** The system includes a polling feature where users can vote for lecturers.
*   **Poll Status:** Users can view the status of polls, including the number of votes for each lecturer.

## Technologies Used

*   **Backend:** Django, Python
*   **Database:** SQLite3
*   **Frontend:** HTML, CSS (basic)

## Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd sai
    ```
3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: A `requirements.txt` file is not included in the project, but you would typically create one with `pip freeze > requirements.txt` after installing the necessary packages. Based on the `settings.py` file, you will need Django.)*

4.  **Apply the database migrations:**
    ```bash
    python manage.py migrate
    ```
5.  **Create a superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```
6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
The application will be available at `http://127.0.0.1:8000/`.

## Project Structure

*   `complaint/`: The main Django app containing the models, views, and templates for the complaint and polling system.
*   `complaintbox/`: The main Django project directory containing the settings and project-level URL configurations.
*   `db.sqlite3`: The SQLite database file.
*   `manage.py`: The Django command-line utility for administrative tasks.
