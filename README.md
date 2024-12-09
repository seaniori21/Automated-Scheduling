# Automated Scheduling System

## Overview

The Automated Scheduling System is a web application built to help employers automate employee scheduling while considering various constraints like employee availability, preferences, and shift limits

## Features

- **Employee Management**: Add, edit, and remove employee details.
- **Shift Preferences**: Employees can specify their availability and shift preferences.
- **Automated Scheduling**: Automatically generates optimized schedules based on employee availability and preferences.
- **Real-Time Updates**: Changes to employee availability or shift assignments are reflected immediately in the schedule.
- **User Authentication**: Secure login and access to user-specific schedules.
- **Responsive UI**: Fully responsive design for both desktop and mobile devices.

## Technologies Used

- **Frontend**: 
  - React
  - Tailwind CSS
- **Backend**: 
  - Flask (Python)
- **Database**:
  - SQLite
  
## Setup & Installation

### Prerequisites

- Node.js (v14 or higher)
- Python (v3.6)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/automated-scheduling.git
   cd automated-scheduling
   ```
2. **Install frontend dependencies:**:
   ```bash
   cd frontend
    npm install
   ```
3. **Install backend dependencies:**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
4. **Setup Database:**:
   ```bash
   cd database
   python database_setup.py
   python insert_data.py
   ```
5. **Run the development server:**:
   ```bash
   cd frontend
   npm start
   ```
   ```bash
   cd backend
   python app.py
   ```



