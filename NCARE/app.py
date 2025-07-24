import flet as ft
from datetime import date, timedelta, datetime

# --- App Styling ---
STYLE = {
    "background": "#F5F5F5",        # Light grey background
    "text": "#212529",              # Dark, readable text
    "primary": "#007BFF",           # Vibrant blue for primary actions
    "primary_container": "#E7F3FF", # Very light blue for accent backgrounds
    "card_bg": "#FFFFFF",           # White for cards
    "font_large": 28, "font_medium": 20, "font_small": 16,
    "icon_large": 48, "icon_medium": 32,
}

# --- Data Structures with More User Details ---
USERS_DATA = {
    "test": {
        "password": "test",
        "records": {
            "Personal Information": {"icon": "account_box", "fields": {"Full Name": "Test User", "Age": "30", "Phone No.": "9999988888", "Email": "test@email.com", "Blood Pressure (BP)": "120/80"}},
            "Medical History": {"icon": "history", "fields": {"Chronic Conditions": "None", "Allergies": "None"}},
        }
    }
}

DOCTOR_SPECIALTIES = [
    {
        "name": "General Physician",
        "icon": "person_outline_rounded",
        "description": "For fever, cold, infections, etc.",
        "doctors": [
            {
                "name": "Dr. Priya Singh",
                "rating": 4.8,
                "address": "12-3-45, MG Road, Near Clock Tower, Motinagar, Hyderabad – 500003, Telangana",
                "hospital": "Apollo Hospital",
                "fees": 700,
                "hospital_contact": "040-23456789"
            },
            {
                "name": "Dr. Rohit Agarwal",
                "rating": 4.6,
                "address": "H.No. 8-4-23, Krishna Nagar, Karmika Nagar, Hyderabad – 500072",
                "hospital": "Sunrise Health Clinic",
                "fees": 500,
                "hospital_contact": "040-76543210"
            },
            {
                "name": "Dr. Shalini Rao",
                "rating": 4.7,
                "address": "Plot No. 21, Near RTO Office, Moosapet, Hyderabad – 500018",
                "hospital": "CityCare Clinic",
                "fees": 600,
                "hospital_contact": "040-99887766"
            }
        ]
    },
    {
        "name": "Cardiologist",
        "icon": "favorite_border_rounded",
        "description": "For heart problems, etc.",
        "doctors": [
            {
                "name": "Dr. Anjali Mehta",
                "rating": 4.9,
                "address": "Plot No. 45, Karmika Nagar Main Road, Near Community Hall, Karmika Nagar, Hyderabad – 500072, Telangana",
                "hospital": "Care Hospital",
                "fees": 950,
                "hospital_contact": "040-98765432"
            },
            {
                "name": "Dr. Vikram Reddy",
                "rating": 4.8,
                "address": "Sanjeevani Heart Center, Near Metro Station, Ameerpet, Hyderabad – 500016",
                "hospital": "Sanjeevani Heart Center",
                "fees": 1000,
                "hospital_contact": "040-77668855"
            },
            {
                "name": "Dr. Neha Kulkarni",
                "rating": 4.7,
                "address": "Sri Nagar Colony, Road No. 2, Hyderabad – 500034",
                "hospital": "Pulse Heart Hospital",
                "fees": 900,
                "hospital_contact": "040-22334455"
            }
        ]
    },
    {
        "name": "Dermatologist",
        "icon": "spa_rounded",
        "description": "For skin, hair, and nail issues.",
        "doctors": [
            {
                "name": "Dr. Rahul Verma",
                "rating": 4.7,
                "address": "6-2-10, Opp. Green View Park, Karmika Nagar, Hyderabad – 500072",
                "hospital": "SkinCure Clinic",
                "fees": 600,
                "hospital_contact": "040-77665544"
            },
            {
                "name": "Dr. Swathi Iyer",
                "rating": 4.6,
                "address": "Shree Plaza, 3rd Floor, Himayatnagar, Hyderabad – 500029",
                "hospital": "DermaPlus",
                "fees": 700,
                "hospital_contact": "040-11223344"
            },
            {
                "name": "Dr. Karthik Nair",
                "rating": 4.5,
                "address": "Street No. 5, Begumpet, Hyderabad – 500016",
                "hospital": "Glow Skin Clinic",
                "fees": 550,
                "hospital_contact": "040-66778899"
            }
        ]
    },
    {
        "name": "Orthopedic",
        "icon": "accessibility_new_rounded",
        "description": "For bones, joints, and back pain.",
        "doctors": [
            {
                "name": "Dr. Nisha Reddy",
                "rating": 4.6,
                "address": "2nd Floor, Trinity Towers, Mount Road, Hyderabad – 500002",
                "hospital": "Trinity Bone & Joint Hospital",
                "fees": 800,
                "hospital_contact": "040-66334455"
            },
            {
                "name": "Dr. Arvind Desai",
                "rating": 4.8,
                "address": "Block A, Sri Sai Complex, Miyapur, Hyderabad – 500049",
                "hospital": "Relief Orthopedic Center",
                "fees": 900,
                "hospital_contact": "040-77889922"
            },
            {
                "name": "Dr. Sneha Thomas",
                "rating": 4.7,
                "address": "5th Cross Road, KPHB Colony, Hyderabad – 500072",
                "hospital": "JointCare Clinic",
                "fees": 750,
                "hospital_contact": "040-66554433"
            }
        ]
    },
    {
        "name": "Pediatrician",
        "icon": "child_care_rounded",
        "description": "For babies and children's health.",
        "doctors": [
            {
                "name": "Dr. Kiran Kumar",
                "rating": 4.9,
                "address": "Flat No. 8, SR Residency, Karmika Nagar, Hyderabad – 500072",
                "hospital": "Happy Kids Hospital",
                "fees": 650,
                "hospital_contact": "040-77889900"
            },
            {
                "name": "Dr. Lavanya Sharma",
                "rating": 4.8,
                "address": "Near Bus Depot, Kukatpally, Hyderabad – 500072",
                "hospital": "Little Smiles Clinic",
                "fees": 700,
                "hospital_contact": "040-99221100"
            },
            {
                "name": "Dr. M. Faheem",
                "rating": 4.7,
                "address": "1st Floor, Annapurna Towers, Moosapet, Hyderabad – 500018",
                "hospital": "NewBorn & Child Care",
                "fees": 600,
                "hospital_contact": "040-88776655"
            }
        ]
    },
    {
        "name": "Gynecologist",
        "icon": "female_rounded",
        "description": "For women’s reproductive and pregnancy care.",
        "doctors": [
            {
                "name": "Dr. Meena Joshi",
                "rating": 4.8,
                "address": "Plot No. 22, Near City Mall, Moosapet, Hyderabad – 500018",
                "hospital": "WellBeing Women’s Hospital",
                "fees": 850,
                "hospital_contact": "040-88997766"
            },
            {
                "name": "Dr. Sushma Yadav",
                "rating": 4.9,
                "address": "Opp. More Supermarket, SR Nagar, Hyderabad – 500038",
                "hospital": "Motherhood Maternity Center",
                "fees": 900,
                "hospital_contact": "040-77664433"
            },
            {
                "name": "Dr. Aarti Chawla",
                "rating": 4.7,
                "address": "Street No. 12, Padmarao Nagar, Hyderabad – 500025",
                "hospital": "LifeCare Women's Clinic",
                "fees": 800,
                "hospital_contact": "040-88445566"
            }
        ]
    }
]

# --- Main Application ---
def main(page: ft.Page):
    page.title = "NCARE"
    page.bgcolor = STYLE["background"]
    page.window_width = 600
    page.window_height = 800

    def get_greeting():
        user_name = page.client_storage.get("user_name") or "User"
        hour = datetime.now().hour
        if 5 <= hour < 12: return f"Good morning, {user_name}!"
        elif 12 <= hour < 17: return f"Good afternoon, {user_name}!"
        else: return f"Good evening, {user_name}!"

    def route_change(e: ft.RouteChangeEvent):
        route_str = e.route
        page.views.clear()

        # --- Login and Sign-Up Views ---
        if route_str == "/login":
            username_field = ft.TextField(label="Username", width=300)
            password_field = ft.TextField(label="Password", password=True, width=300)
            def login_click(e):
                user = username_field.value.lower()
                if user in USERS_DATA and password_field.value == USERS_DATA[user]["password"]:
                    page.client_storage.set("user_name", USERS_DATA[user]["records"]["Personal Information"]["fields"]["Full Name"])
                    page.go("/choice")
                else:
                    username_field.error_text = "Invalid credentials"; page.update()
            page.views.append(ft.View(route="/login", vertical_alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, controls=[ft.Text("NCARE", size=40, weight=ft.FontWeight.BOLD, color=STYLE["primary"]), ft.Container(height=20), username_field, password_field, ft.ElevatedButton("Login", on_click=login_click, width=300, height=50), ft.TextButton("Don't have an account? Sign Up", on_click=lambda _: page.go("/signup"))]))
        
        elif route_str == "/signup":
            new_username = ft.TextField(label="Choose a Username", width=300)
            new_password = ft.TextField(label="Choose a Password", password=True, width=300)
            full_name = ft.TextField(label="Your Full Name", width=300)
            def signup_click(e):
                user = new_username.value.lower()
                if not user or not new_password.value or not full_name.value: new_username.error_text = full_name.error_text = new_password.error_text = "All fields are required"
                elif user in USERS_DATA: new_username.error_text = "Username already exists"
                else:
                    USERS_DATA[user] = {"password": new_password.value, "records": {"Personal Information": {"icon": "account_box", "fields": {"Full Name": full_name.value, "Age": "", "Phone No.": "", "Email": "", "Blood Pressure (BP)": ""}}, "Medical History": {"icon": "history", "fields": {"Chronic Conditions": "", "Allergies": ""}}}}
                    page.go("/login")
                page.update()
            page.views.append(ft.View(route="/signup", appbar=ft.AppBar(title=ft.Text("Create Account"), bgcolor="surfacevariant"), vertical_alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, controls=[full_name, new_username, new_password, ft.ElevatedButton("Sign Up", on_click=signup_click, width=300, height=50)]))

        # --- Guard clause ---
        elif not page.client_storage.get("user_name"):
            page.go("/login"); return

        # --- Choice Page View ---
# --- Choice Page View ---
        elif route_str == "/choice":
            page.views.append(
                ft.View(
                    route="/choice",
                    # Add alignment to the main view to center all content
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    padding=40,
                    controls=[
                        ft.Column(
                            # Arrange items with spacing
                            spacing=40,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    get_greeting(),
                                    size=STYLE["font_large"],
                                    weight=ft.FontWeight.BOLD,
                                    text_align=ft.TextAlign.CENTER
                                ),
                                ft.Column(
                                    spacing=20,
                                    width=400,
                                    controls=[
                                        ft.ElevatedButton(
                                            content=ft.Row([ft.Icon("person"), ft.Text("Book for Me")], alignment=ft.MainAxisAlignment.CENTER),
                                            height=70,
                                            on_click=lambda _: page.go("/book?for=me")
                                        ),
                                        ft.ElevatedButton(
                                            content=ft.Row([ft.Icon("people"), ft.Text("Book for Someone Else")], alignment=ft.MainAxisAlignment.CENTER),
                                            height=70,
                                            on_click=lambda _: page.go("/book_for_other")
                                        ),
                                        ft.ElevatedButton(
                                            content=ft.Row([ft.Icon("edit_note"), ft.Text("My Data")], alignment=ft.MainAxisAlignment.CENTER),
                                            height=70,
                                            on_click=lambda _: page.go("/my_data")
                                        ),
                                    ]
                                ),
                                ft.TextButton(
                                    "Logout",
                                    on_click=lambda _: (page.client_storage.remove("user_name"), page.go("/login"))
                                )
                            ]
                        )
                    ]
                )
            )

        # --- My Data View (Editable) ---
        elif route_str == "/my_data":
            username = [user for user, data in USERS_DATA.items() if data["records"]["Personal Information"]["fields"]["Full Name"] == page.client_storage.get("user_name")][0]
            personal_fields = USERS_DATA[username]["records"]["Personal Information"]["fields"]
            field_controls = {label: ft.TextField(value=value, read_only=True, border="none") for label, value in personal_fields.items()}

            def toggle_edit_mode(e):
                is_edit = e.control.data == 'edit'
                for field in field_controls.values(): field.read_only = not is_edit; field.border = ft.InputBorder.UNDERLINE if is_edit else ft.InputBorder.NONE
                if not is_edit: # If saving
                    for label, textfield in field_controls.items(): USERS_DATA[username]["records"]["Personal Information"]["fields"][label] = textfield.value
                    page.client_storage.set("user_name", field_controls["Full Name"].value) # Update stored name if changed
                edit_button.visible, save_button.visible = not is_edit, is_edit
                page.update()

            edit_button = ft.IconButton(icon="edit", on_click=toggle_edit_mode, data="edit")
            save_button = ft.IconButton(icon="save", on_click=toggle_edit_mode, data="save", visible=False)
            
            page.views.append(ft.View(route="/my_data", appbar=ft.AppBar(title=ft.Text("My Data"), actions=[edit_button, save_button], leading=ft.IconButton(icon="arrow_back", on_click=lambda _: page.go("/choice"))), padding=20, controls=[
                ft.Column([ft.ListTile(title=ft.Text(label, weight=ft.FontWeight.BOLD), subtitle=field) for label, field in field_controls.items()])
            ]))

        # --- Book for Someone Else Form ---
        elif route_str == "/book_for_other":
            patient_name = ft.TextField(label="Patient Name")
            patient_phone = ft.TextField(label="Phone No.", keyboard_type=ft.KeyboardType.PHONE)
            patient_age = ft.TextField(label="Age", keyboard_type=ft.KeyboardType.NUMBER)

            def continue_booking(e):
                # Store details temporarily and proceed
                page.client_storage.set("other_patient_name", patient_name.value)
                page.go("/book?for=other")
            
            page.views.append(ft.View(route="/book_for_other", appbar=ft.AppBar(title=ft.Text("Enter Patient Details"), leading=ft.IconButton(icon="arrow_back", on_click=lambda _: page.go("/choice"))), padding=30, controls=[
                patient_name, patient_phone, patient_age, ft.Container(height=20),
                ft.ElevatedButton("Continue", on_click=continue_booking, height=50)
            ]))

        # --- Find Specialty View ---
        elif route_str.startswith("/book"):
            page.views.append(ft.View(route=route_str, appbar=ft.AppBar(title=ft.Text("Find a Specialty"), leading=ft.IconButton(icon="arrow_back", on_click=lambda _: page.go("/choice"))), padding=20, controls=[
                ft.ListView(expand=True, spacing=10, controls=[ft.ListTile(leading=ft.Icon(name=s["icon"]), title=ft.Text(s["name"], weight=ft.FontWeight.BOLD), subtitle=ft.Text(s["description"]), on_click=lambda _, s=s: page.go(f"/doctors/{s['name']}")) for s in DOCTOR_SPECIALTIES])
            ]))

        # --- Doctors List View ---
        elif route_str.startswith("/doctors/"):
            specialty_name = route_str.split("/")[-1]
            specialty = next((s for s in DOCTOR_SPECIALTIES if s["name"] == specialty_name), None)
            if specialty:
                page.views.append(ft.View(route=route_str, appbar=ft.AppBar(title=ft.Text(f"{specialty['name']}s"), leading=ft.IconButton(icon="arrow_back", on_click=lambda _: page.go("/book"))), padding=20, controls=[ft.ListView(spacing=15, expand=True, controls=[ft.Card(content=ft.Container(padding=15, content=ft.Column([ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[ft.Text(doc["name"], weight=ft.FontWeight.BOLD), ft.Row(spacing=5, controls=[ft.Icon("star", color="amber"), ft.Text(str(doc["rating"]))])]), ft.Row(spacing=5, controls=[ft.Icon("location_on"), ft.Text(doc["address"])]), ft.Row([ft.Container(expand=True), ft.ElevatedButton("More Details", on_click=lambda _, s=specialty_name, d=doc["name"]: page.go(f"/details/{s}/{d}"))])]))) for doc in specialty["doctors"]])]))

        # --- Doctor Details View ---
                
        elif route_str.startswith("/details/"):
            parts = route_str.split("/"); specialty_name, doctor_name = parts[-2], parts[-1]
            specialty = next((s for s in DOCTOR_SPECIALTIES if s["name"] == specialty_name), None)
            doctor = next((d for d in specialty["doctors"] if d["name"] == doctor_name), None)
            if doctor:
                selected_date = ft.Text("Please select a date and time", weight=ft.FontWeight.BOLD)
                symptoms_field = ft.TextField(label="What are your symptoms?", multiline=True, min_lines=2)
                def show_confirmation(e):
                    page.open(ft.AlertDialog(modal=True, title=ft.Text("Appointment Confirmed! ✅"), content=ft.Column([ft.Text(f"With {doctor['name']} at {doctor['hospital']}"), ft.Text(f"On: {selected_date.value}"), ft.Text(f"Address: {doctor['address']}"), ft.Divider(), ft.Text("Thank you for choosing NCARE!")], tight=True), actions=[ft.TextButton("OK", on_click=lambda _: page.go("/choice"))]))
                def handle_time(e): page.close(time_picker); selected_date.value = f"{date_picker.value.strftime('%d-%b-%Y')} at {time_picker.value.strftime('%I:%M %p')}"; page.update()
                time_picker = ft.TimePicker(on_change=handle_time)
                def handle_date(e): page.close(date_picker); page.open(time_picker)
                date_picker = ft.DatePicker(on_change=handle_date, first_date=date.today())
                page.overlay.extend([date_picker, time_picker])
                page.views.append(
                    ft.View(
                        route=route_str,
                        appbar=ft.AppBar(title=ft.Text(doctor["name"]), leading=ft.IconButton(icon="arrow_back", on_click=lambda _: page.go(f"/doctors/{specialty_name}"))),
                        padding=20,
                        controls=[
                            ft.ListView(expand=True, spacing=15, controls=[
                                ft.ListTile(leading=ft.Icon("apartment"), title=ft.Text(doctor["hospital"]), subtitle=ft.Text(doctor["address"])),
                                ft.ListTile(leading=ft.Icon("call"), title=ft.Text(doctor["hospital_contact"]), subtitle=ft.Text("Contact for appointment")),
                                # --- THIS IS THE FIXED LINE ---
                                ft.ListTile(leading=ft.Icon("currency_rupee"), title=ft.Text(f"{doctor['fees']}"), subtitle=ft.Text("Consultation Fees")),
                                ft.Divider(),
                                symptoms_field,
                                ft.Divider(),
                                ft.Row([selected_date, ft.IconButton(icon="calendar_month", on_click=lambda _: page.open(date_picker))]),
                                ft.Container(height=10),
                                ft.ElevatedButton("Book Appointment", on_click=show_confirmation, height=50)
                            ])
                        ]
                    )
                )
        
        else:
            page.views.append(ft.View(route=route_str, appbar=ft.AppBar(title=ft.Text("Error")), controls=[ft.Text("Page not found.")]))


        page.update()

    def view_pop(view):
        page.views.pop(); page.go(page.views[-1].route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/login")

if __name__ == "__main__":
    ft.app(target=main)