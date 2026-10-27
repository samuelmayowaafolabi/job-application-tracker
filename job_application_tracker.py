applications_tracker = {
    "applications": [
        {
            "company": "Shell",
            "role": "Graduate Trainee",
            "status": "Applied",
        },
        {
            "company": "Seplat",
            "role": "Graduate Trainee",
            "status": "Interviewed",
        },
        {
            "company": "Dangote Refineries",
            "role": "Entry Level Engineer",
            "status": "Applied",
        },
        {
            "company": "First Bank",
            "role": "IT Officer",
            "status": "Applied",
        },

    ]
}
def add_application(company, role, status):
    new_application = {
        "company": company,
        "role": role,
         "status": status,
    }
    applications_tracker["applications"].append(new_application)

def view_applications(applications_tracker):
    if applications_tracker["applications"]:
        for application in applications_tracker["applications"]:
            print(f"{application["company"]}: {application["role"]}, {application["status"]}")
    else:
        print("No applications found")
add_application("Chevron", "Process Engineer", "Applied")
view_applications(applications_tracker)

def search_application(company):
    for application in applications_tracker["applications"]:
        if company == application["company"]:
            return (f"{application["company"]}: {application["role"]}, {application["status"]}")
    return "Application not found"
print(search_application("Shell"))
print(search_application("Microsoft"))

def delete_application(company):
        for application in applications_tracker["applications"]:
            if company == application["company"]:
                applications_tracker["applications"].remove(application)
                return (f"{application["company"]}: {application["role"]}, {application["status"]}")
        return "Application not found"
print(delete_application("Seplat"))
view_applications(applications_tracker)

while True:
    print("\n===== JOB APPLICATION TRACKER =====")
    print("1. Add Application")
    print("2. View Applications")
    print("3. Search Application")
    print("4. Delete Application")
    print("5. Exit")

    choose = int(input("Choose an option: "))
    
    if choose == 1:
        company = input("Enter company name: ")
        role = input("Enter role applied for: ")
        status = input("Enter application status: ")
        add_application(company, role, status)
    elif choose == 2:
        view_applications(applications_tracker)
    elif choose == 3:
        company = input("Enter company name: ")
        print(search_application(company))
    elif choose == 4:
        company = input("Enter company name: ")
        print(delete_application(company))
    elif choose == 5:
        print("You ended this tracker")
        break
    else:
        print("Invalid option. Please enter a number from 1 to 5.")
