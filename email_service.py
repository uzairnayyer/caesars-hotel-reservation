"""
Email utilities.

NOTE: You must set CAESARS_EMAIL and CAESARS_EMAIL_PASSWORD
as environment variables with your own email + app password.
No credentials are included in this repository.

In windows(cmd):
    set CAESARS_EMAIL=your_email@gmail.com
    set CAESARS_EMAIL_PASSWORD=your_app_password
"""

import os
import smtplib
from email.message import EmailMessage


def send_booking_email(to_email, guest_name, nights, adults, rooms, checkin, checkout):
    """
    Send a booking confirmation email.

    Uses environment variables:
      CAESARS_EMAIL           -> sender email address
      CAESARS_EMAIL_PASSWORD  -> app password for that email
    """

    sender_email = os.environ.get("CAESARS_EMAIL")
    sender_password = os.environ.get("CAESARS_EMAIL_PASSWORD")

    if not sender_email or not sender_password:
        print("Email not sent: CAESARS_EMAIL or CAESARS_EMAIL_PASSWORD not set.")
        return

    try:
        msg = EmailMessage()
        msg['Subject'] = "Booking Confirmation - Caesars Palace"
        msg['From'] = sender_email
        msg['To'] = to_email

        msg.set_content(f"""
Dear {guest_name},

We are delighted to confirm your reservation at Caesars Palace Resort.

Please find your booking details below:

    • Guest Name: {guest_name}
    • Number of Nights: {nights}
    • Number of Adults: {adults}
    • Rooms Reserved: {rooms}
    • Check-in Date: {checkin}
    • Check-out Date: {checkout}

📍 Location: Naran Road, Balakot, Pakistan

We sincerely appreciate your choice to stay with us. Our team is committed to providing you with an exceptional and luxurious experience throughout your visit.

If you have any questions or special requests prior to your arrival, please do not hesitate to contact us.

Warmest regards,  
Caesars Palace Reservations Team  
📧 caesarpalacepak@gmail.com  
📞 021 111 969 969
        """)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)

        print("Email sent successfully!")

    except Exception as e:
        print(f"Error sending email: {e}")