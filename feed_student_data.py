from django.contrib.auth import get_user_model

# This automatically grabs your CustomUser model
User = get_user_model() 

student_data = [
    {"prn": "72245804F", "name": "Mayuri More"},
    {"prn": "72245872L", "name": "Shruti Sutar"},
    {"prn": "72245818F", "name": "Arya Pancholi"},
    {"prn": "72245805D", "name": "Taniksha Morankar"},
    {"prn": "72245795C", "name": "Akhilesh Madwalkar"},
    {"prn": "72245844E", "name": "Kshiteej Salunke"},
    {"prn": "72245802K", "name": "Manvi Tekriwal"},
    {"prn": "72245839J", "name": "Rohit Ghogare"},
    {"prn": "72245717M", "name": "Kunal Bansal"},
    {"prn": "72245808J", "name": "Naeem Mulla"},
    {"prn": "72245757L", "name": "Gokulnath G"},
    {"prn": "72245800C", "name": "Prachi Mane"},
    {"prn": "72245862C", "name": "Kshitija Shingde"},
    {"prn": "72245788L", "name": "Nikita Kokate"},
    {"prn": "72245749K", "name": "Rusheekesh Gadge"},
    {"prn": "72245799F", "name": "Gagan Mandal"},
    {"prn": "72245798H", "name": "Harshal Mali"},
    {"prn": "72245731G", "name": "Tanmay Chavan"},
    {"prn": "72245868B", "name": "Sumeet Rasal"},
    {"prn": "72245883F", "name": "Vinamrakumar Vishwakarma"},
    {"prn": "72245777E", "name": "Neha Kachkure"},
    {"prn": "72245856J", "name": "Shubham Shelke"},
    {"prn": "72320907D", "name": "Sahil Salunkhe"},
    {"prn": "72245843G", "name": "Atharva Salunke"},
    {"prn": "72245820H", "name": "Vaibhav Pandit"},
    {"prn": "72245863M", "name": "Santosh Shirke"},
    {"prn": "72245887J", "name": "Ram Wasankar"},
    {"prn": "72245739B", "name": "Anjali Deshpande"},
    {"prn": "72245851H", "name": "Shantanu Hazra"},
    {"prn": "72245859C", "name": "Abhilash Shinde"},
    {"prn": "72245836D", "name": "Vikas Prasad"},
    {"prn": "72245769D", "name": "Shantanu Jaigude"},
    {"prn": "72245830E", "name": "Kapil Phapale"},
    {"prn": "72245825J", "name": "Rohit Patil"},
    {"prn": "72245775J", "name": "Advait Javkar"},
    {"prn": "72245767H", "name": "Manas Jagzap"},
    {"prn": "72245869L", "name": "Ruturaj Suryawanshi"},
    {"prn": "72245847K", "name": "Sumedh Sangle"},
    {"prn": "72245822D", "name": "Gaurav Patil"},
    {"prn": "72245823B", "name": "Karan Patil"},
    {"prn": "72248532M", "name": "Anandhu Pillai"},
    {"prn": "72245828C", "name": "Chaitanya Pawar"},
    {"prn": "72245707D", "name": "Aniket Ahire"},
    {"prn": "72245890J", "name": "Ruturaj Yadav"},
    {"prn": "72245885B", "name": "Bhushan Waghmare"},
    {"prn": "72320897C", "name": "Pranjal Kankal"},
    {"prn": "72320902C", "name": "Arti Lokare"},
    {"prn": "72245848H", "name": "Sakshi Sapkal"},
    {"prn": "72245807L", "name": "Vaishnavi Munjal"},
    {"prn": "72245780E", "name": "Aishwarya Kasar"},
    {"prn": "72245789J", "name": "Kaveri Kolekar"},
    {"prn": "72245743L", "name": "Siddhi Dhumal"},
    {"prn": "72320906F", "name": "Rohan Bondre"},
    {"prn": "72320898M", "name": "Namrata Kedar"},
    {"prn": "72320905H", "name": "Jagruti Patil"},
    {"prn": "72320893L", "name": "Pragati Gaikwad"},
    {"prn": "72245774L", "name": "Komal Jamdade"},
    {"prn": "72245889E", "name": "Khushi Yadav"},
    {"prn": "72245857G", "name": "Bhagyashree Sherkhane"},
    {"prn": "72245888G", "name": "Sneha Wetal"},
    {"prn": "72245815M", "name": "Leelansh Nikumbh"},
    {"prn": "72245712L", "name": "Anup Munjal"},
    {"prn": "72245765M", "name": "Suraj Jadhav"},
    {"prn": "72245878K", "name": "Vaibhav Bhimnawar"},
    {"prn": "72245738D", "name": "Shlok Desai"},
    {"prn": "72320890F", "name": "Shravani Chavan"},
    {"prn": "72245791L", "name": "Vaishnavi Kurumkar"},
    {"prn": "72245860G", "name": "Pallavi Shinde"},
    {"prn": "72320900G", "name": "Aashutosh Kulkarni"},
    {"prn": "72320903M", "name": "Yash Mule"},
    {"prn": "72320904K", "name": "Saad Nadaf"},
    {"prn": "72245705H", "name": "Harshad Adsul"},
    {"prn": "72245838L", "name": "Aarya Raut"},
    {"prn": "72245834H", "name": "Yash Pingale"},
    {"prn": "72245721K", "name": "Aditya Bhiste"},
    {"prn": "72245785F", "name": "Shrinath Khade"},
    {"prn": "72245728G", "name": "Prathmesh Butte"},
    {"prn": "72245873J", "name": "Prathmesh Tamboli"},
    {"prn": "72245779M", "name": "Vijay Kadam"},
    {"prn": "72245870D", "name": "Rutuja Susar"},
    {"prn": "72245865H", "name": "Shreya Salunkhe"},
    {"prn": "72245866F", "name": "Sonia Singh"},
    {"prn": "72245733C", "name": "Vaishnavi Chopade"},
    {"prn": "72320889B", "name": "Karan Chavan"},
    {"prn": "72245761J", "name": "Gayatri Ingole"},
    {"prn": "72245778C", "name": "Prathamesh Kadam"},
    {"prn": "72245760L", "name": "Hemani Raina"},
    {"prn": "72245817H", "name": "Purva Palankar"},
    {"prn": "72245833K", "name": "Shruti Pimpalkar"},
    {"prn": "72245741D", "name": "Tejas Dhabale"},
    {"prn": "72245716C", "name": "Khayum Baig Tabasum"},
    {"prn": "72245719H", "name": "Sangeeta Suresh Behera"},
    {"prn": "72320891D", "name": "Riya Desai"},
    {"prn": "72245753H", "name": "Gaurav Dwivedi"},
    {"prn": "72245732E", "name": "Vivek Chavan"},
    {"prn": "72245754F", "name": "Gawade Rishi"},
    {"prn": "72245736H", "name": "Mayur Dange"},
    {"prn": "72152151H", "name": "Revan Gunjal"},
    {"prn": "72201689B", "name": "Lokesh Ingle"},
    {"prn": "72245962K", "name": "Adesh Chakrnarayan"},
    {"prn": "72201704k", "name": "Sahil Khune"},
    {"prn": "72245816k", "name": "Amit Padman"},
    {"prn": "72245871B", "name": "Kishor Sutar"},
    {"prn": "72245819D", "name": "Tejas Pande"},
    {"prn": "72245886L", "name": "Somwshwar Waghmode"},
    {"prn": "72320896E", "name": "Prathmesh Kadam"},
    {"prn": "72245827E", "name": "Aditya Pawar"},
    {"prn": "72245831C", "name": "Aditi Pilaji"},
    {"prn": "72245811J", "name": "Pratiksha Narute"},
    {"prn": "72245809G", "name": "Yedukrishna Nair"},
    {"prn": "72245812G", "name": "Rohit Navlakhe"},
    {"prn": "72245794E", "name": "Lokesh Nimbalkar"},
    {"prn": "72245740F", "name": "Parth Deshpande"},
    {"prn": "72245746E", "name": "Nishant Ethape"},
    {"prn": "72201758J", "name": "Harsh Solanki"},
    {"prn": "72201656F", "name": "Rohit Borde"},
    {"prn": "72245776G", "name": "Sahil Joshi"},
    {"prn": "72245801M", "name": "Rohit Mane"},
    {"prn": "72245861E", "name": "Shreekrushna Shinde"},
    {"prn": "72245855L", "name": "Swapnil shelake"},
    {"prn": "72320901E", "name": "Adarsh Kumbhar"},
    {"prn": "72320892B", "name": "Lalit Dhake"},
    {"prn": "72320908B", "name": "Soham Borkar"},
    {"prn": "72320894J", "name": "Gaikwad Rhushabh"},
    {"prn": "72320895G", "name": "Ghogare Rushikesh"},
    {"prn": "72320899K", "name": "Khandale Shekhar"},
    {"prn": "72245714G", "name": "Avhad Roshan"},
    {"prn": "72245773B", "name": "Sarthak Jambe"},
    {"prn": "72245748M", "name": "Rushikesh Gadekar"},
    {"prn": "722457470", "name": "Karan Gadekar"},
    {"prn": "72245710D", "name": "Aniket Honrao"}
]

DEFAULT_PASSWORD = "123456"
created_count = 0

for student in student_data:
    prn_upper = student['prn'].strip().upper() 
    full_name_parts = student['name'].strip().split()
    
    first_name = full_name_parts[0] if len(full_name_parts) > 0 else ""
    last_name = full_name_parts[-1] if len(full_name_parts) > 1 else ""

    if last_name:
        college_email = f"{first_name.lower()}.{last_name.lower()}@indiraicem.ac.in"
    else:
        # Fallback just in case a student only has one name listed
        college_email = f"{first_name.lower()}@indiraicem.ac.in"

    # Check if user exists, if not, create them using create_user so passwords hash correctly
    if not User.objects.filter(username=prn_upper).exists():
        user = User.objects.create_user(
            username=prn_upper,
            email= college_email, 
            password=DEFAULT_PASSWORD,
            first_name=first_name,
            last_name=last_name,
            role='student'  # <--- Essential for your CustomUser model
        )
        created_count += 1
        print(f"Created: {first_name} {last_name} ({prn_upper})")
    else:
        print(f"Skipped: {prn_upper} already exists.")

print(f"\n✅ Successfully created {created_count} new student accounts.")