# Caesars Hotel Reservation

A desktop hotel reservation system built with Python and Tkinter for **Caesars Hotels & Resorts**

## Features
- **Landing screen**
  - Full screen welcome page with background image
  - Quick access to Sign Up and Login

- **User Authentication**
  - Sign Up form (first name, last name, phone, email, password)
  - Login using first name and password
  - User data stored in SQLite (`data/SELF.db`)

- **Room Selection**
  - Multiple room types (Beach Pool Villa, Sea View Villa, Over Water Pool Villa, Two Bedroom House)
  - Room details: size, capacity, inclusions, rate per night
  - "BOOK NOW" buttons to open the booking page

- **Booking Page**
  - Guest name, nights, adults, rooms, email
  - Date selection using a calendar widget (tkcalendar)
  - Check in and Check-out confirmation
  - Booking saved in SQLite
  - Email confirmation sent to the guest

- **Additional Info**
  - View location on Google Maps
  - Open Privacy Statement, Cookie Policy, and Terms & Conditions PDF files

## Tech Stack

- **Python 3.x**
- **Tkinter** (GUI)
- **Pillow** (`PIL`) for image handling
- **tkcalendar** for date selection
- **SQLite3** for data storage
- **smtplib / email.message** for sending confirmation emails

## Important: Email configuration required

This project does **not** include any real email address or password for security reasons.

If you want the **booking confirmation emails** to work, you must configure your own sender email account:

1. Use a Gmail account (or similar) and create an **App Password**.
2. Set these environment variables on your system **before** running the app:

   **Windows (cmd):**
   set CAESARS_EMAIL=your_email@gmail.com
   set CAESARS_EMAIL_PASSWORD=your_app_password

## Project Structure

caesars-hotel-reservation/
├─ main.py              
├─ styles.py            
├─ email_utils.py      
├─ paths.py             
├─ requirements.txt
├─ README.md
├─ assets/
│  ├─ images/           
│  └─ docs/             
└─ data/
   └─ SELF.db           
