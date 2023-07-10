import random

# Create a dictionary to store the college information
college_info = {
    "Williams College": {
        "Location": "Williamstown, Massachusetts",
        "Contact": "(413) 597-3131",
        "College Mail": "",
        "College Website": "https://www.williams.edu/",
        "Courses Offered": [
            "Econometrics and Quantitative Economics",
            "Mathematics, General",
            "Biology/Biological Sciences, General",
            "Political Science and Government",
            "Psychology, General"
        ]
    },
    "Amherst College": {
        "Location": "Amherst, Massachusetts",
        "Contact": "(413) 542-2000",
        "College Mail": "",
        "College Website": "https://www.amherst.edu/",
        "Courses Offered": [
            "Computer Science",
            "Research and Experimental Psychology",
            "History, General",
            "Statistics, General",
            "English Language and Literature"
        ]
    },
    "Swarthmore College": {
        "Location": "Swarthmore, Pennsylvania",
        "Contact": "(610) 328-8000",
        "College Mail": "",
        "College Website": "https://www.swarthmore.edu/",
        "Courses Offered": [
            "Engineering and Liberal Arts",
            "Computer Information Sciences and Support Services",
            "Biological and Biomedical Sciences",
            "Literatures and Linguistics",
            "Multi/Interdisciplinary Studies",
            "Foreign Languages"
        ]
    },
    "Pomona College": {
        "Location": "Claremont, California",
        "Contact": "(909) 621-8000",
        "College Mail": "",
        "College Website": "https://www.pomona.edu/",
        "Courses Offered": [
            "Liberal Arts and Sciences",
            "Visual and Performing Arts",
            "Physical Sciences",
            "Social Sciences",
            "Biological and Biomedical Sciences",
            "Computer and Information Sciences and Support Services"
        ]
    },
    "Wellesley College": {
        "Location": "Wellesley, Massachusetts",
        "Contact": "781-283-1000",
        "College Mail": "",
        "College Website": "https://www.wellesley.edu/",
        "Courses Offered": [
            "Liberal Arts and Sciences",
            "Biological and Biomedical Sciences",
            "Literatures",
            "Physical Sciences",
            "Foreign Languages",
            "Literatures and Linguistics"
        ]
    },
    "Seneca College": {
        "Location": "Toronto, Ontario",
        "Contact": "416-491-5050",
        "College Mail": "admissions@senecacollege.ca",
        "College Website": "https://www.senecacollege.ca/",
        "Courses Offered": [
            "Computer Studies",
            "Creative Arts",
            "Engineering Technology",
            "Hospitality & Tourism",
            "Media & Communication"
        ]
    },
    "George Brown College": {
        "Location": "Toronto, Ontario",
        "Contact": "416-415-2000",
        "College Mail": "ask.george@georgebrown.ca",
        "College Website": "https://www.georgebrown.ca/",
        "Courses Offered": [
            "Hospitality & Culinary Arts",
            "Community Services",
            "Computer Technology",
            "Business",
            "Construction & Engineering Technologies"
        ]
    },
    "Humber College": {
        "Location": "Toronto, Ontario",
        "Contact": "416-675-3111",
        "College Mail": "enquiry@humber.ca",
        "College Website": "https://www.humber.ca/",
        "Courses Offered": [
            "Media Studies & Information Technology",
            "Social & Community Services",
            "Health Sciences",
            "Applied Sciences & Technology",
            "Liberal Arts & Sciences"
        ]
    },
    "Algonquin College": {
        "Location": "Ottawa, Ontario",
        "Contact": "613-727-4723",
        "College Mail": "askus@algonquincollege.com",
        "College Website": "https://www.algonquincollege.com/",
        "Courses Offered": [
            "Media & Design",
            "Health & Community Studies",
            "Information & Communications Technology",
            "Hospitality & Tourism",
            "Arts & Sciences"
        ]
    },
    "Sheridan College": {
        "Location": "Oakville, Ontario",
        "Contact": "905-845-9430",
        "College Mail": "info@sheridancollege.ca",
        "College Website": "https://www.sheridancollege.ca/",
        "Courses Offered": [
            "Skilled Trades",
            "Health & Community Services",
            "Animation",
            "Engineering & Technology",
            "Community Studies"
        ]
    },
    "Cape Peninsula University of Technology": {
        "Location": "Cape Town, South Africa",
        "Contact": "27219596767",
        "College Mail": "info@cput.ac.za",
        "College Website": "https://www.cput.ac.za/",
        "Courses Offered": [
            "Engineering",
            "Health and Wellness Sciences",
            "Applied Sciences",
            "Informatics and Design",
            "Business Studies"
        ]
    },
    "Durban University of Technology": {
        "Location": "Durban, South Africa",
        "Contact": "27313732000",
        "College Mail": "info@dut.ac.za",
        "College Website": "https://www.dut.ac.za/",
        "Courses Offered": [
            "Engineering and the Built Environment",
            "Accounting and Informatics",
            "Arts and Design",
            "Management Sciences",
            "Health Sciences"
        ]
    },
    "University of Nairobi": {
        "Location": "Nairobi, Kenya",
        "Contact": "254 20 318262",
        "College Mail": "uonbi@uonbi.ac.ke",
        "College Website": "https://www.uonbi.ac.ke/",
        "Courses Offered": [
            "Biological and Physical Sciences",
            "Agriculture and Veterinary Sciences",
            "Law",
            "Education and External Studies",
            "Biological and Physical Sciences"
        ]
    },
    "Cairo University": {
        "Location": "Giza, Egypt",
        "Contact": "20235676161",
        "College Mail": "info@cu.edu.eg",
        "College Website": "http://www.cu.edu.eg/",
        "Courses Offered": [
            "Agriculture",
            "Medicine",
            "Dentistry",
            "Pharmacy",
            "Commerce"
        ]
    },
    "Stellenbosch University": {
        "Location": "Stellenbosch, South Africa",
        "Contact": "27 21 808 9111",
        "College Mail": "info@sun.ac.za",
        "College Website": "https://www.sun.ac.za/",
        "Courses Offered": [
            "Business and Economics",
            "Natural Sciences",
            "Arts and Social Sciences",
            "Medicine and Health Sciences",
            "Social Sciences"
       ]
    },
    "National University of Singapore (NUS)": {
        "Location": "Singapore",
        "Contact": "6565166666",
        "College Mail": "enquiry@nus.edu.sg",
        "College Website": "https://www.nus.edu.sg/",
        "Courses Offered": [
            "Arts and Social Sciences",
            "Design and Environment",
            "Design and Environment",
            "Computing",
            "Law"
        ]
    },
    "Tsinghua University": {
        "Location": "Beijing, China",
        "Contact": "861062786564",
        "College Mail": "admission@tsinghua.edu.cn",
        "College Website": "https://www.tsinghua.edu.cn/en/",
        "Courses Offered": [
            "Arts and Humanities",
            "Law",
            "Medicine",
            "Information Sciences and Technology",
            "Economics and Management"
        ]
    },
    "Indian Institute of Technology Bombay": {
        "Location": "Mumbai, India",
        "Contact": "912225722545",
        "College Mail": "dean.admissions@iitb.ac.in",
        "College Website": "https://www.iitb.ac.in/",
        "Courses Offered": [
            "Aerospace Engineering",
            "Chemical Engineering",
            "Mechanical Engineering",
            "Computer Engineering",
            "Electrical Engineering"
        ]
    },
    "Seoul National University": {
        "Location": "Seoul, South Korea",
        "Contact": "822880 5114",
        "College Mail": "intadmission@snu.ac.kr",
        "College Website": "https://www.snu.ac.kr/",
        "Courses Offered": [
            "Humanities",
            "Natural Sciences",
            "Business Administration",
            "Agriculture and Life Sciences",
            "Medicine"
        ]
    },
    "University of Tokyo": {
        "Location": "Tokyo, Japan",
        "Contact": "81338122111",
        "College Mail": "iao@ml.adm.u-tokyo.ac.jp",
        "College Website": "https://www.u-tokyo.ac.jp/en/",
        "Courses Offered": [
            "Pharmaceutical Sciences",
            "Engineering",
            "Medicine",
            "Economics",
            "Agriculture"
        ]
    },
    "University College London (UCL)": {
        "Location": "London, United Kingdom",
        "Contact": "44(0)2076792000",
        "College Mail": "undergraduate-admissions@ucl.ac.uk",
        "College Website": "https://www.ucl.ac.uk/",
        "Courses Offered": [
            "Mathematical and Physical Sciences",
            "Social and Historical Sciences",
            "Built Environment",
            "Arts and Humanities",
            "Life Sciences"
        ]
    },
    "ETH Zurich – Swiss Federal Institute of Technology": {
        "Location": "Zurich, Switzerland",
        "Contact": "41446322111",
        "College Mail": "info@ethz.ch",
        "College Website": "https://ethz.ch/",
        "Courses Offered": [
            "Architecture and Civil Engineering",
            "Engineering Sciences",
            "System-oriented Natural Sciences",
            "Natural Sciences and Mathematics",
            "Engineering Sciences"
        ]
    },
    "University of Oxford": {
        "Location": "Oxford, United Kingdom",
        "Contact": "44 (0)1865 270000",
        "College Mail": "undergraduate.admissions@admin.ox.ac.uk",
        "College Website": "https://www.ox.ac.uk/",
        "Courses Offered": [
            "Physical, and Life Sciences",
            "Medicine",
            "Social Science",
            "Humanities",
            "Mathematical"
        ]
    },
    "Sorbonne University": {
        "Location": "Paris, France",
        "Contact": "33(0)144 27 44 27",
        "College Mail": "contact@sorbonne-universite.fr",
        "College Website": "https://www.sorbonne-universite.fr/en",
        "Courses Offered": [
            "Humanities",
            "Science and Engineering",
            "Technology and Management",
            "Medicine",
            "Social Sciences and Humanities"
        ]
    },
    "Technical University of Munich (TUM)": {
        "Location": "Munich, Germany",
        "Contact": "49892891",
        "College Mail": "studium@tum.de",
        "College Website": "https://www.tum.de/",
        "Courses Offered": [
            "Architecture",
            "Civil Engineering",
            "Mechanical Engineering",
            "Electrical Engineering and Information Technology",
            "Computer Science, Natural Sciences, Life Sciences"
        ]
    }
}

# Define the bot's responses
bot_responses = [
    "Welcome to the College Inquiry Bot! How can I assist you today?",
    "How can I help you with your college inquiries?",
    "Feel free to ask me any questions about colleges!"
]

# Function to handle user queries
def handle_user_query(user_query):
    response = random.choice(bot_responses)
    return response

# Function to get college information
def get_college_info(college_name):
    if college_name in college_info:
        return college_info[college_name]
    else:
        return None

# Function to list all available colleges
def list_colleges():
    print("Bot: Here are the available colleges:")
    for index, college in enumerate(college_info.keys(), start=1):
        print(f"{index}. {college}")

# Main conversation loop
print("Bot: " + random.choice(bot_responses))
while True:
    print("User: Choose an option:")
    print("1. Get college information")
    print("2. List all colleges")
    print("3. Exit")
    user_choice = input("User: ")

    if user_choice == "1":
        college_name = input("User: Enter the college name: ")
        college_info = get_college_info(college_name)

        if college_info:
            print("Bot: Here is some information about", college_name)
            print("Location:", college_info["Location"])
            print("Contact:", college_info["Contact"])
            print("College Website:", college_info["College Website"])
            print("Courses Offered:")
            for course in college_info["Courses Offered"]:
                print("-", course)
        else:
            print("Bot: College information not found.")

    elif user_choice == "2":
        list_colleges()
        college_choice = input("User: Enter the number of the college for more information: ")
        college_index = int(college_choice) - 1
        if 0 <= college_index < len(college_info):
            college_name = list(college_info.keys())[college_index]
            college_info = get_college_info(college_name)

            print("Bot: Here is some information about", college_name)
            print("Location:", college_info["Location"])
            print("Contact:", college_info["Contact"])
            print("College Website:", college_info["College Website"])
            print("Courses Offered:")
            for course in college_info["Courses Offered"]:
                print("-", course)
        else:
            print("Bot: Invalid college selection.")

    elif user_choice == "3":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Invalid choice. Please select a valid option.")