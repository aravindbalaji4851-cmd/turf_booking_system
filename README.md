# Turf Booking System

A Django REST Framework based backend application for managing turfs and customer bookings through REST APIs.

## Features

* Turf management

  * Add turf details
  * View turf details
  * Update turf details
  * Delete turf details

* Booking management

  * Create turf bookings
  * View all bookings
  * View individual booking
  * Update booking
  * Delete booking

* Customer registration

* Booking date and time management

* Booking duration support

* Automatic calculation of booking end time

* Prevents overlapping bookings for the same turf

* REST API development using Django REST Framework

## Technologies Used

* Python
* Django
* Django REST Framework
* SQLite
* Git
* GitHub

## Project Structure

```text
turf_booking_system/
│
├── booking_v2/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── slot_booking/
├── turf/
├── turf_booking_system/
├── APIDOC.http
├── db.sqlite3
└── manage.py
```

## Booking Model

The booking system stores the following information:

* Customer name
* Turf
* Booking date
* Start time
* Booking duration
* End time
* Phone number
* Email

The booking model uses Django's `DurationField` to store the booking duration. The end time is calculated automatically based on the selected start time and duration.

## Booking Validation

The application checks whether a turf already has a booking that overlaps with the requested time.

If an overlapping booking exists, the system prevents the new booking and returns a message indicating that the slot is already booked.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/aravindbalaji4851-cmd/turf_booking_system.git
```

### 2. Navigate to the project directory

```bash
cd turf_booking_system
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install django djangorestframework
```

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

## API Testing

The repository contains an `APIDOC.http` file with API requests for testing the project.

You can use the **REST Client** extension in Visual Studio Code to send the requests directly from the `APIDOC.http` file.

## Learning Objectives

This project was developed to practice:

* Django REST Framework
* CRUD operations
* Django models
* Serializers
* API views
* Django ORM
* Database operations
* Foreign key relationships
* Date and time handling
* Duration calculations
* API validation
* Preventing overlapping bookings
* REST API development

## Future Improvements

* User authentication and authorization
* Turf search and filtering
* Online payment integration
* Booking cancellation
* Availability checking
* Admin dashboard
* Email or SMS booking notifications

## Author

**Aravind Balaji K J**

GitHub: https://github.com/aravindbalaji4851-cmd
