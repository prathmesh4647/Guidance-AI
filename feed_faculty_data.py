from django.contrib.auth import get_user_model

# Automatically grabs your CustomUser model
User = get_user_model() 

# Cleaned list of unique faculty members extracted from the PDF
faculty_names = [
    "Nilesh Uke",
    "Soumitra Das",
    "Sunil Rathod",
    "Poorna Shankar",
    "Anita Patil",
    "Deepali Dhadwad",
    "Malayaj Kumar",
    "Deepali Junankar",
    "Shwetkranti Taware",
    "Rupali Adhau",
    "Pragati Malusare",
    "Savitri Pawar",
    "Minal Patil",
    "Mrunal Vaidya"
]

DEFAULT_PASSWORD = "Password@123"
created_count = 0

for full_name in faculty_names:
    name_parts = full_name.split()
    
    first_name = name_parts[0]
    last_name = name_parts[-1] if len(name_parts) > 1 else ""

    # Generate the college-specific email format
    if last_name:
        college_email = f"{first_name.lower()}.{last_name.lower()}@indiraicem.ac.in"
    else:
        college_email = f"{first_name.lower()}@indiraicem.ac.in"

    # For faculty, the username IS the email
    username = college_email

    # Check if the faculty user already exists
    if not User.objects.filter(username=username).exists():
        user = User.objects.create_user(
            username=username,
            email=college_email, 
            password=DEFAULT_PASSWORD,
            first_name=first_name,
            last_name=last_name,
            role='faculty'  # Assigning the faculty role
        )
        created_count += 1
        print(f"Created Faculty: {first_name} {last_name} | Username/Email: {college_email}")
    else:
        print(f"Skipped: {username} already exists.")

print(f"\n✅ Successfully created {created_count} new faculty accounts.")