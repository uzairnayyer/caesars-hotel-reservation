import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk
from tkcalendar import Calendar
import os
import webbrowser

from styles import bnt_style, heading_style
from email_service import send_booking_email
from paths import image_path, doc_path, DB_PATH, ensure_data_dir


ensure_data_dir() 


class HotelReservationApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.state('zoomed')
        self.root.geometry("1920x1080")
        self.root.title("Luxury Hotels and Resorts | Caesars Hotels, Resorts")

        icon = tk.PhotoImage(file=image_path("book.png"))
        self.root.iconphoto(True, icon)
        self.root.configure(bg="#F0F0FF")
        self.create_main_window()
        self.root.mainloop()

    def create_main_window(self):
        self.frame = Frame(self.root, width=700, height=500)
        self.frame.pack()
        self.frame.place(anchor='center', relx=0.5, rely=0.5)

        self.img = ImageTk.PhotoImage(Image.open(image_path("mainpage.jpg")))
        self.label = Label(self.frame, image=self.img)
        self.label.pack()

        logo_image = Image.open(image_path("logo1.png")).convert("RGBA")
        logo_image = logo_image.resize((190, 190))
        self.logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = Label(self.root, image=self.logo_photo, bg="#F0F0FF", borderwidth=0)
        logo_label.pack(pady=(10, 0))

        # Frames for login and signup
        self.frame = Frame(self.root, bg="#F0F0FF")
        self.frame.place(relx=0.5, rely=0.825, anchor="center")

        bf = Frame(self.root)
        bf2 = Frame(self.root)
        bf2.pack(side="bottom", anchor="sw")
        bf3 = Frame(self.root)
        bf3.pack(side="bottom", anchor="sw")
        bf.pack(side="bottom")
        bf1 = Frame(self.root)
        bf1.pack(side="bottom", anchor="sw")
        bottomframe = Frame(self.root)
        bottomframe.pack(side="bottom", anchor="se")

        i5 = Label(bf, text="© 2025 Caesars Hotels & Resorts", fg="black")
        i5.pack(side="left")

        # Bottom buttons
        i6 = Button(bottomframe, text="Privacy Statement",
                    command=self.open_privacy, **bnt_style)
        i6.pack(side=RIGHT, padx=(10, 0))

        i7 = Button(bottomframe, text="Cookie Policy",
                    command=self.open_cookie_policy, **bnt_style)
        i7.pack(side=RIGHT, padx=(10, 0))

        i8 = Button(bottomframe, text="Terms & Conditions",
                    command=self.open_terms, **bnt_style)
        i8.pack(side=RIGHT)

        # Questions / contact
        i9 = Label(bf1, text="ANY QUESTIONS?", fg="black",
                   font=("Arial", 15, "bold"))
        i9.pack(side="left")

        i12 = Label(bf3, text="Contact Number: 021 111 969 969", fg="black")
        i12.pack(side="left")
        i12 = Label(bf3, text="Email us: caesarpalacepak@gmail.com", fg="black")
        i12.pack(side="left")
        i13 = Label(bf2, text="Location: Naran Road, Balakot, Pakistan", fg="black")
        i13.pack(side="left")

        def open_map():
            webbrowser.open("https://maps.app.goo.gl/dai9unW3MwiHcP7C7")

        map_button = Button(bf2, text="📍 View on Map", command=open_map,
                            **bnt_style)
        map_button.pack(padx=10, pady=10)

        # Login & SignUp buttons
        i3 = Button(self.frame, text="SIGN UP", command=self.sign_up, **bnt_style)
        i3.pack(side=LEFT, padx=10)

        i4 = Button(self.frame, text="LOGIN", command=self.login, **bnt_style)
        i4.pack(side=LEFT, padx=10)

    # Signup page
    def sign_up(self):
        c = Toplevel()
        c.geometry("500x500")
        c.title("SIGN UP")
        c.configure(bg="#F0F0FF")

        icon = tk.PhotoImage(file=image_path("book.png"))
        c.iconphoto(True, icon)

        logo_image = Image.open(image_path("signup.png")).convert("RGBA")
        logo_image = logo_image.resize((80, 80))
        signup_logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = Label(c, image=signup_logo_photo, bg="#F0F0FF", borderwidth=0)
        logo_label.image = signup_logo_photo
        logo_label.pack(pady=(10, 0))

        Firstname = StringVar()
        LastName = StringVar()
        phoneNumber = IntVar()
        Email = StringVar()
        createpassword = StringVar()
        confirmpassword = StringVar()

        def database():
            Fname = Firstname.get()
            Lname = LastName.get()
            number = phoneNumber.get()
            email = Email.get()
            createpass = createpassword.get()
            confirmpass = confirmpassword.get()

            if not Fname or not Lname or not number or not email or not createpass or not confirmpass:
                messagebox.showerror('Error', 'All fields are required.')
                return
            if createpass != confirmpass:
                messagebox.showerror('Error', 'Passwords do not match.')
                return

            conn = sqlite3.connect(DB_PATH)
            with conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS SIGNUP(
                        Firstname TEXT,
                        LastName TEXT,
                        phoneNumber INTEGER,
                        Email TEXT,
                        createpassword TEXT,
                        confirmpassword TEXT
                    )
                """)
                cursor.execute("""
                    INSERT INTO SIGNUP(Firstname, LastName, phoneNumber, Email,
                                       createpassword, confirmpassword)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (Fname, Lname, number, email, createpass, confirmpass))
                conn.commit()

            messagebox.showinfo('Information', 'Sign-up successfully')
            c.destroy()

        Label(c, text="First Name", font=("Arial", 10, "bold")).place(x=120, y=100)
        Label(c, text="Last Name", font=("Arial", 10, "bold")).place(x=120, y=150)
        Label(c, text="Phone Number", font=("Arial", 10, "bold")).place(x=120, y=200)
        Label(c, text="Email", font=("Arial", 10, "bold")).place(x=120, y=250)
        Label(c, text="Create Password", font=("Arial", 10, "bold")).place(x=120, y=300)
        Label(c, text="Confirm Password", font=("Arial", 10, "bold")).place(x=120, y=350)

        Entry(c, textvar=Firstname, bd=3).place(x=260, y=100)
        Entry(c, textvar=LastName, bd=3).place(x=260, y=150)
        Entry(c, textvar=phoneNumber, bd=3).place(x=260, y=200)
        Entry(c, textvar=Email, bd=3).place(x=260, y=250)
        Entry(c, textvar=createpassword, bd=3, show='*').place(x=260, y=300)
        Entry(c, textvar=confirmpassword, bd=3, show='*').place(x=260, y=350)

        Button(c, text="SUBMIT", command=database, **bnt_style).place(x=280, y=400)

    # Login page
    def login(self):
        b = Toplevel()
        b.geometry("330x355")
        b.title("LOGIN")
        b.configure(bg="#F0F0FF")

        icon = tk.PhotoImage(file=image_path("book.png"))
        b.iconphoto(True, icon)

        logo_image = Image.open(image_path("login.png")).convert("RGBA")
        logo_image = logo_image.resize((100, 100))
        login_logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = Label(b, image=login_logo_photo, bg="#F0F0FF", borderwidth=0)
        logo_label.image = login_logo_photo
        logo_label.pack(pady=(10, 0))

        def LOGin():
            x = e1.get()
            y = e2.get()
            if x == "" or y == "":
                messagebox.showinfo('message', "Fill the Username and Password")
                return

            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM SIGNUP WHERE Firstname=? AND createpassword=?",
                (x, y)
            )
            result = cursor.fetchone()
            conn.close()

            if result:
                b.destroy()
                self.hotel_log()
            else:
                messagebox.showerror('error', "Invalid Username or Password")

        Label(b, text="Username", font=("Arial", 10, "bold")).place(x=50, y=140)
        Label(b, text="Password", font=("Arial", 10, "bold")).place(x=50, y=180)
        e1 = Entry(b, bd=3)
        e1.place(x=130, y=140)
        e2 = Entry(b, bd=3, show='*')
        e2.place(x=130, y=180)

        Button(b, text="SUBMIT", command=LOGin, **bnt_style).place(x=140, y=220)

    def hotel_log(self, previous_window=None):
        if previous_window:
            previous_window.destroy()

        d = Toplevel()
        d.state('zoomed')
        d.geometry("1920x1080")
        d.title("Caesars Palace Resort")
        d.configure(bg="#F0F0FF")

        icon = tk.PhotoImage(file=image_path("book.png"))
        d.iconphoto(True, icon)

        left_frame = Label(d, bg="#F0F0FF", bd=2, relief=RIDGE)
        left_frame.place(relx=0.032, rely=0.1, relheight=0.85, relwidth=0.45)

        right_frame = Label(d, bg="#F0F0FF", bd=2, relief=RIDGE)
        right_frame.place(relx=0.52, rely=0.1, relheight=0.85, relwidth=0.45)

        logo_image = Image.open(image_path("log_logo1.png")).convert("RGBA")
        logo_image = logo_image.resize((120, 90))
        logo_photo2 = ImageTk.PhotoImage(logo_image)
        logo_labe2 = Label(d, image=logo_photo2, bg="#F0F0FF", borderwidth=0)
        logo_labe2.image = logo_photo2
        logo_labe2.pack(pady=(10, 0))

        # Room 1
        Label(d, text="   BEACH POOL VILLA", **heading_style).place(x=430, y=120)

        image = Image.open(image_path("pool.jpg"))
        test = ImageTk.PhotoImage(image)
        labell = Label(d, image=test)
        labell.image = test
        labell.place(x=70, y=120)

        Label(d, text="*Best Flexible with Breakfast and Dinner", **bnt_style).place(x=430, y=170)
        Label(d, text="*Two meals included", **bnt_style).place(x=430, y=210)
        Label(d, text="*Non-refundable", **bnt_style).place(x=430, y=250)
        Label(d, text="*Children stay for free", **bnt_style).place(x=430, y=290)
        Label(d, text="- FREE WIFI", **bnt_style).place(x=70, y=380)
        Label(d, text="- ROOM SIZE 258 M.sq / 2,776 FT.sq", **bnt_style).place(x=70, y=410)
        Label(d, text="- MAXIMUM 3 ADULTS", **bnt_style).place(x=70, y=440)
        Label(d, text="- IN-VILLA BUTLER SERVICE", **bnt_style).place(x=70, y=470)

        Button(d, text="Rs. 75,000 / night", **bnt_style).place(x=450, y=380)

        # Room 2
        Label(d, text="  SEA VIEW VILLA", **heading_style).place(x=1370, y=120)

        image = Image.open(image_path("sv_room.jpg"))
        test = ImageTk.PhotoImage(image)
        labell = Label(d, image=test)
        labell.image = test
        labell.place(x=1010, y=120)

        Label(d, text="*Best Flexible with Breakfast and Dinner", **bnt_style).place(x=1370, y=170)
        Label(d, text="*Two meals included", **bnt_style).place(x=1370, y=210)
        Label(d, text="*Non-refundable", **bnt_style).place(x=1370, y=250)
        Label(d, text="*Children stay for free", **bnt_style).place(x=1370, y=290)
        Label(d, text="- FREE WIFI", **bnt_style).place(x=1008, y=380)
        Label(d, text="- ROOM SIZE 258 M.sq / 2,776 FT.sq", **bnt_style).place(x=1008, y=410)
        Label(d, text="- MAXIMUM 3 ADULTS", **bnt_style).place(x=1008, y=440)
        Label(d, text="- IN-VILLA BUTLER SERVICE", **bnt_style).place(x=1008, y=470)

        Button(d, text="Rs. 45,000 / night", **bnt_style).place(x=1400, y=380)

        def hotel_log_A(previous_window):
            f = Toplevel()
            f.state('zoomed')
            f.geometry("1920x1080")
            f.title("Caesars Royal Resort")
            f.configure(bg="#F0F0FF")

            icon_inner = tk.PhotoImage(file=image_path("book.png"))
            f.iconphoto(True, icon_inner)

            left_frame2 = Label(f, bg="#F0F0FF", bd=2, relief=RIDGE)
            left_frame2.place(relx=0.032, rely=0.1, relheight=0.85, relwidth=0.45)

            right_frame2 = Label(f, bg="#F0F0FF", bd=2, relief=RIDGE)
            right_frame2.place(relx=0.52, rely=0.1, relheight=0.85, relwidth=0.45)

            # Logo
            logo_image2 = Image.open(image_path("log_logo2.png")).convert("RGBA")
            logo_image2 = logo_image2.resize((120, 90))
            logo_photo2_inner = ImageTk.PhotoImage(logo_image2)
            logo_labe2_inner = Label(f, image=logo_photo2_inner, bg="#F0F0FF", borderwidth=0)
            logo_labe2_inner.image = logo_photo2_inner
            logo_labe2_inner.pack(pady=(10, 0))

            # Room 3
            image = Image.open(image_path("Pool_Villa.jpg"))
            test = ImageTk.PhotoImage(image)
            labell1 = Label(f, image=test)
            labell1.image = test
            labell1.place(x=70, y=120)

            Label(f, text="  Over Water Pool Villa", **heading_style).place(x=430, y=120)
            Label(f, text="*Best Flexible with Breakfast and Dinner", **bnt_style).place(x=430, y=170)
            Label(f, text="*Two meals included", **bnt_style).place(x=430, y=210)
            Label(f, text="*Non-refundable", **bnt_style).place(x=430, y=250)
            Label(f, text="*Children stay for free", **bnt_style).place(x=430, y=290)
            Label(f, text="- FREE WIFI", **bnt_style).place(x=70, y=380)
            Label(f, text="- ROOM SIZE 267 M.sq / 2,873 FT.sq", **bnt_style).place(x=70, y=410)
            Label(f, text="- MAXIMUM 3 ADULTS", **bnt_style).place(x=70, y=440)
            Label(f, text="- IN-VILLA BUTLER SERVICE", **bnt_style).place(x=70, y=470)

            Button(f, text="Rs. 90,000 / night", **bnt_style).place(x=450, y=380)

            # Room 4
            Label(f, text="     Two Bedroom HOUSE", **heading_style).place(x=1370, y=120)

            image = Image.open(image_path("bedroom.jpg"))
            test = ImageTk.PhotoImage(image)
            labell1 = Label(f, image=test)
            labell1.image = test
            labell1.place(x=1010, y=120)

            Label(f, text="*Best Flexible with Breakfast and Dinner", **bnt_style).place(x=1370, y=170)
            Label(f, text="*Two meals included", **bnt_style).place(x=1370, y=210)
            Label(f, text="*Non-refundable", **bnt_style).place(x=1370, y=250)
            Label(f, text="*Children stay for free", **bnt_style).place(x=1370, y=290)
            Label(f, text="- FREE WIFI", **bnt_style).place(x=1008, y=380)
            Label(f, text="- ROOM SIZE 1500 M.sq / 16,140 FT.sq", **bnt_style).place(x=1008, y=410)
            Label(f, text="- MAXIMUM 6 ADULTS", **bnt_style).place(x=1008, y=440)
            Label(f, text="- IN-VILLA BUTLER SERVICE", **bnt_style).place(x=1008, y=470)

            Button(f, text="Rs. 95,000 / night", **bnt_style).place(x=1400, y=380)

            # Book Now Buttons
            Button(f, text="BOOK NOW", command=book, **bnt_style).place(x=450, y=550)
            Button(f, text="BOOK NOW", command=book, **bnt_style).place(x=1400, y=550)

            # Back
            Button(f, text="<<", command=lambda: [f.destroy(), self.hotel_log()],
                   **bnt_style).pack(side="left")

        def book():
            e = Toplevel()
            e.state('zoomed')
            e.geometry("1920x1080")
            e.title("BOOKING PAGE")
            e.configure(bg="#F0F0FF")

            icon_book = tk.PhotoImage(file=image_path("book.png"))
            e.iconphoto(True, icon_book)

            logo_image = Image.open(image_path("book.png")).convert("RGBA")
            logo_image = logo_image.resize((120, 90))
            logo_photo2 = ImageTk.PhotoImage(logo_image)
            logo_labe2 = Label(e, image=logo_photo2, bg="#F0F0FF", borderwidth=0)
            logo_labe2.image = logo_photo2
            logo_labe2.pack(pady=(10, 0))

            Label(e, text="Your Booking Details", **heading_style).place(x=620, y=100)

            # Input variables
            NIGHTS = IntVar()
            ADULTS = IntVar()
            ROOMS = IntVar()
            CHECK_IN = StringVar()
            CHECK_OUT = StringVar()
            EMAIL = StringVar()
            GUEST_NAME = StringVar()

            Label(e, text="GUEST NAME:", font=("Arial", 10, "bold")).place(x=620, y=150)
            Label(e, text="NIGHT(S):", font=("Arial", 10, "bold")).place(x=620, y=200)
            Label(e, text="ADULTS:", font=("Arial", 10, "bold")).place(x=620, y=250)
            Label(e, text="ROOMS:", font=("Arial", 10, "bold")).place(x=620, y=300)
            Label(e, text="EMAIL:", font=("Arial", 10, "bold")).place(x=620, y=500)

            e50 = Entry(e, bd=3, textvariable=GUEST_NAME)
            e50.place(x=720, y=150)

            e51 = Entry(e, bd=3, textvariable=NIGHTS)
            e51.place(x=720, y=200)

            e52 = Entry(e, bd=3, textvariable=ADULTS)
            e52.place(x=720, y=250)

            e53 = Entry(e, bd=3, textvariable=ROOMS)
            e53.place(x=720, y=300)

            e54 = Entry(e, bd=3, textvariable=EMAIL)
            e54.place(x=720, y=500)

            # Calendar
            date_var = tk.StringVar()

            def get_selected_date():
                selected_date = cal.get_date()
                date_var.set(selected_date)

            cal = Calendar(e, selectmode="day", year=2025, month=12, day=29)
            cal.place(x=300, y=200)

            select_date_button = Button(e, text="SELECT DATE",
                                        command=get_selected_date)
            select_date_button.place(x=470, y=400)

            selected_date_label = Label(e, textvariable=date_var)
            selected_date_label.place(x=400, y=400)

            # Check-in / Check-out
            def update_checkin_date():
                checkin_entry.delete(0, tk.END)
                checkin_entry.insert(0, date_var.get())
                CHECK_IN.set(date_var.get())

            def update_checkout_date():
                checkout_entry.delete(0, tk.END)
                checkout_entry.insert(0, date_var.get())
                CHECK_OUT.set(date_var.get())

            Label(e, text="CHECK-IN:", font=("Arial", 10, "bold")).place(x=620, y=350)
            checkin_entry = tk.Entry(e)
            checkin_entry.place(x=720, y=350)
            Button(e, text="CONFIRM CHECK-IN", command=update_checkin_date).place(
                x=720, y=385
            )

            Label(e, text="CHECK-OUT:", font=("Arial", 10, "bold")).place(x=620, y=435)
            checkout_entry = tk.Entry(e)
            checkout_entry.place(x=720, y=435)
            Button(e, text="CONFIRM CHECK-OUT", command=update_checkout_date).place(
                x=720, y=470
            )

            def database():
                nights = NIGHTS.get()
                adults = ADULTS.get()
                rooms = ROOMS.get()
                check_in_date = CHECK_IN.get()
                check_out_date = CHECK_OUT.get()
                guest_email = EMAIL.get()
                guest_name = GUEST_NAME.get()

                if (not nights or not adults or not rooms or
                        not check_in_date or not check_out_date or
                        not guest_email or not guest_name):
                    messagebox.showerror('Error', 'All fields are required.')
                    return

                conn = sqlite3.connect(DB_PATH)
                with conn:
                    cursor = conn.cursor()
                    cursor.execute('DROP TABLE IF EXISTS company')
                    cursor.execute("""
                        CREATE TABLE company(
                            NIGHTS INTEGER,
                            ADULTS INTEGER,
                            ROOMS INTEGER,
                            CHECK_IN TEXT,
                            CHECK_OUT TEXT,
                            EMAIL TEXT,
                            GUEST_NAME TEXT
                        )
                    """)
                    cursor.execute("""
                        INSERT INTO company(
                            NIGHTS, ADULTS, ROOMS,
                            CHECK_IN, CHECK_OUT,
                            EMAIL, GUEST_NAME
                        )
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (nights, adults, rooms,
                          check_in_date, check_out_date,
                          guest_email, guest_name))
                    conn.commit()

                messagebox.showinfo('Information', 'BOOKED SUCCESSFULLY')

                # Send confirmation email
                send_booking_email(
                    to_email=guest_email,
                    guest_name=guest_name,
                    nights=nights,
                    adults=adults,
                    rooms=rooms,
                    checkin=check_in_date,
                    checkout=check_out_date
                )

            Button(e, text="CONFIRM", command=database,
                   **bnt_style).place(x=700, y=600)

        # Book Now buttons on main room page
        Button(d, text="BOOK NOW", command=book, **bnt_style).place(x=450, y=550)
        Button(d, text="BOOK NOW", command=book, **bnt_style).place(x=1400, y=550)

        Button(d, text=">>",
               command=lambda: hotel_log_A(previous_window=d),
               **bnt_style).pack(side="right")

    def open_privacy(self):
        try:
            os.startfile(doc_path("privacy_statement.pdf"))
        except Exception as e:
            messagebox.showerror("Error", f"Cannot open privacy statement: {e}")

    def open_cookie_policy(self):
        try:
            os.startfile(doc_path("cookie_policy.pdf"))
        except Exception as e:
            messagebox.showerror("Error", f"Cannot open cookie policy: {e}")

    def open_terms(self):
        try:
            os.startfile(doc_path("terms_and_conditions.pdf"))
        except Exception as e:
            messagebox.showerror("Error", f"Cannot open terms document: {e}")



if __name__ == "__main__":
    app = HotelReservationApp()