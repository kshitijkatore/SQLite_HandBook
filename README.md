# Smart Record Manager (Web App)

A user-friendly web application for managing student records, built with Streamlit and SQLite. The app allows you to add, view, search, update, delete, analyze, visualize, and export student data, with simple authentication for secure access.

---

## Features

- **User Authentication:** Register and log in to access the app.
- **Add Student:** Input new student records (name, age, grade, city).
- **View Students:** Display all student records in a table.
- **Search:** Filter students by grade and city.
- **Update/Delete:** Edit or remove existing student records.
- **Statistics:** View total students, average age, and grade counts.
- **Visualization:** Pie chart for grade distribution, histogram for age.
- **Export:** Download all student data as a CSV file.

---

## Tech Stack

- **Frontend & App Framework:** [Streamlit](https://streamlit.io/)
- **Database:** SQLite (via `sqlite3`)
- **Data Handling:** pandas
- **Visualization:** matplotlib, plotly

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd SQLite_HandBook
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Run the app:**
   ```bash
   streamlit run smart_record_manager/app.py
   ```

2. **Open in your browser:**  
   The app will open automatically or visit the provided local URL.

3. **Login/Register:**  
   - Register a new account or log in with existing credentials.
   - After login, use the sidebar menu to navigate between features.

---

## Project Structure

```
SQLite_HandBook/
│
├── requirements.txt
├── smart_record_manager/
│   ├── app.py           # Main Streamlit app entry point
│   ├── db.py            # Database models and operations
│   ├── views.py         # UI views for all app features
│   ├── auth.py          # User authentication logic
│   ├── students.db      # SQLite database file
│   └── __pycache__/     # Python bytecode cache (ignore)
│
├── SQLite/
│   ├── 01_Basics_Sqlite.ipynb
│   ├── Intermediate_practice.ipynb
│   ├── example.db
│   ├── sales_data.db
│   ├── student.db
│   └── students.db
│
└── venv/                # Python virtual environment (ignore)
```

---

## Database Schema

- **student**
  - `id` (INTEGER, PRIMARY KEY)
  - `name` (TEXT)
  - `age` (INTEGER)
  - `grade` (TEXT)
  - `city` (TEXT)

- **users**
  - `username` (TEXT, PRIMARY KEY)
  - `password` (TEXT, NOT NULL)

---

## Dependencies

- streamlit
- matplotlib
- plotly
- pandas

(See `requirements.txt`)

---

## Screenshots

Below are some screenshots demonstrating the app's UI and features:

### Login / Register
![Login](smart_record_manager\screenshots\Screenshot 2025-07-07 125951.png)

### Add Student
![Add Student](smart_record_manager\screenshots\Screenshot 2025-07-07 125104.png)

### View Students
![View Students](smart_record_manager\screenshots\Screenshot 2025-07-07 125147.png)

### Search Students
![Search Students](smart_record_manager\screenshots\Screenshot 2025-07-07 125230.png)

### Update/Delete Student
![Update/Delete Student](smart_record_manager\screenshots\Screenshot 2025-07-07 125327.png)
![Update/Delete Student](smart_record_manager\screenshots\Screenshot 2025-07-07 125354.png)
### Statistics
![Statistics](smart_record_manager\screenshots\Screenshot 2025-07-07 125652.png)

### Visualize
![Visualize](smart_record_manager\screenshots\Screenshot 2025-07-07 125751.png)

> _Place your screenshots in a `screenshots/` folder in the project root for them to display here._

---

## Notes

- The `SQLite/` folder contains additional practice notebooks and databases, not directly used by the app.
- The `venv/` and `__pycache__/` folders can be ignored.

---

## License

[MIT License] (or specify your license here)