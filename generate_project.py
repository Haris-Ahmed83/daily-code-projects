
import os
import datetime
import json

# Define the 180-day topic list
topic_list = [
    # Week 1-4
    {"day": 1, "category": "Frontend", "title": "Weather dashboard"},
    {"day": 2, "category": "Python", "title": "File organizer"},
    {"day": 3, "category": "API", "title": "Task API"},
    {"day": 4, "category": "DSA", "title": "Binary search viz"},
    {"day": 5, "category": "AI/ML", "title": "Sentiment analyzer"},
    {"day": 6, "category": "Database", "title": "CRUD contacts"},
    {"day": 7, "category": "Full-Stack", "title": "To-do full-stack"},
    {"day": 8, "category": "Frontend", "title": "Portfolio UI"},
    {"day": 9, "category": "Python", "title": "PDF converter"},
    {"day": 10, "category": "API", "title": "Currency API"},
    {"day": 11, "category": "DSA", "title": "Linked list viz"},
    {"day": 12, "category": "AI/ML", "title": "Image classifier"},
    {"day": 13, "category": "Database", "title": "Grade tracker"},
    {"day": 14, "category": "Full-Stack", "title": "Blog platform"},
    # Week 5-8
    {"day": 15, "category": "Frontend", "title": "Dark mode kit"},
    {"day": 16, "category": "Python", "title": "Video downloader"},
    {"day": 17, "category": "API", "title": "Weather wrapper"},
    {"day": 18, "category": "DSA", "title": "Stack/Queue demo"},
    {"day": 19, "category": "AI/ML", "title": "Text summarizer"},
    {"day": 20, "category": "Database", "title": "Expense tracker"},
    {"day": 21, "category": "Full-Stack", "title": "Chat app"},
    {"day": 22, "category": "Frontend", "title": "CSS animation lib"},
    {"day": 23, "category": "Python", "title": "Email sender"},
    {"day": 24, "category": "API", "title": "URL shortener"},
    {"day": 25, "category": "DSA", "title": "Sorting viz"},
    {"day": 26, "category": "AI/ML", "title": "Face detection"},
    {"day": 27, "category": "Database", "title": "Book manager"},
    {"day": 28, "category": "Full-Stack", "title": "E-commerce page"},
    {"day": 29, "category": "Frontend", "title": "Personal Blog"},
    {"day": 30, "category": "Python", "title": "Web Scraper"},
    {"day": 31, "category": "API", "title": "Quote Generator API"},
    {"day": 32, "category": "DSA", "title": "Graph Traversal Viz"},
    {"day": 33, "category": "AI/ML", "title": "Spam Detector"},
    {"day": 34, "category": "Database", "title": "Inventory Management"},
    {"day": 35, "category": "Full-Stack", "title": "Social Media Feed"},
    {"day": 36, "category": "Frontend", "title": "Image Gallery"},
    {"day": 37, "category": "Python", "title": "Password Generator"},
    {"day": 38, "category": "API", "title": "Recipe API"},
    {"day": 39, "category": "DSA", "title": "Tree Traversal Viz"},
    {"day": 40, "category": "AI/ML", "title": "Recommendation System"},
    {"day": 41, "category": "Database", "title": "Library Management"},
    {"day": 42, "category": "Full-Stack", "title": "Forum Application"},
    {"day": 43, "category": "Frontend", "title": "Calculator App"},
    {"day": 44, "category": "Python", "title": "Unit Converter"},
    {"day": 45, "category": "API", "title": "Joke API"},
    {"day": 46, "category": "DSA", "title": "Shortest Path Viz"},
    {"day": 47, "category": "AI/ML", "title": "Language Translator"},
    {"day": 48, "category": "Database", "title": "Customer Relationship Management"},
    {"day": 49, "category": "Full-Stack", "title": "Online Code Editor"},
    {"day": 50, "category": "Frontend", "title": "Landing Page"},
    {"day": 51, "category": "Python", "title": "QR Code Generator"},
    {"day": 52, "category": "API", "title": "News API"},
    {"day": 53, "category": "DSA", "title": "Dynamic Programming Viz"},
    {"day": 54, "category": "AI/ML", "title": "Object Detection"},
    {"day": 55, "category": "Database", "title": "Hospital Management"},
    {"day": 56, "category": "Full-Stack", "title": "Real-time Chat"},
    {"day": 57, "category": "Frontend", "title": "Quiz App"},
    {"day": 58, "category": "Python", "title": "Image Resizer"},
    {"day": 59, "category": "API", "title": "Weather Forecast API"},
    {"day": 60, "category": "DSA", "title": "Greedy Algorithm Viz"},
    {"day": 61, "category": "AI/ML", "title": "Speech Recognition"},
    {"day": 62, "category": "Database", "title": "Student Management"},
    {"day": 63, "category": "Full-Stack", "title": "Project Management Tool"},
    {"day": 64, "category": "Frontend", "title": "Tic-Tac-Toe Game"},
    {"day": 65, "category": "Python", "title": "CSV Processor"},
    {"day": 66, "category": "API", "title": "Movie Database API"},
    {"day": 67, "category": "DSA", "title": "Backtracking Viz"},
    {"day": 68, "category": "AI/ML", "title": "Face Recognition"},
    {"day": 69, "category": "Database", "title": "Employee Management"},
    {"day": 70, "category": "Full-Stack", "title": "E-commerce Store"},
    {"day": 71, "category": "Frontend", "title": "Memory Game"},
    {"day": 72, "category": "Python", "title": "Web Crawler"},
    {"day": 73, "category": "API", "title": "Book Search API"},
    {"day": 74, "category": "DSA", "title": "Divide and Conquer Viz"},
    {"day": 75, "category": "AI/ML", "title": "Handwritten Digit Recognition"},
    {"day": 76, "category": "Database", "title": "Fitness Tracker"},
    {"day": 77, "category": "Full-Stack", "title": "Online Survey Tool"},
    {"day": 78, "category": "Frontend", "title": "Countdown Timer"},
    {"day": 79, "category": "Python", "title": "PDF Merger"},
    {"day": 80, "category": "API", "title": "Random User API"},
    {"day": 81, "category": "DSA", "title": "Hashing Viz"},
    {"day": 82, "category": "AI/ML", "title": "Chatbot"},
    {"day": 83, "category": "Database", "title": "Event Management"},
    {"day": 84, "category": "Full-Stack", "title": "Job Board"},
    {"day": 85, "category": "Frontend", "title": "Image Carousel"},
    {"day": 86, "category": "Python", "title": "Video Converter"},
    {"day": 87, "category": "API", "title": "Stock Market API"},
    {"day": 88, "category": "DSA", "title": "String Matching Viz"},
    {"day": 89, "category": "AI/ML", "title": "Image Captioning"},
    {"day": 90, "category": "Database", "title": "Recipe Book"},
    {"day": 91, "category": "Full-Stack", "title": "Online Learning Platform"},
    {"day": 92, "category": "Frontend", "title": "Form Validator"},
    {"day": 93, "category": "Python", "title": "Audio Recorder"},
    {"day": 94, "category": "API", "title": "Translation API"},
    {"day": 95, "category": "DSA", "title": "Bit Manipulation Viz"},
    {"day": 96, "category": "AI/ML", "title": "Music Genre Classifier"},
    {"day": 97, "category": "Database", "title": "Bug Tracker"},
    {"day": 98, "category": "Full-Stack", "title": "Booking System"},
    {"day": 99, "category": "Frontend", "title": "Drag and Drop List"},
    {"day": 100, "category": "Python", "title": "File Encryptor/Decryptor"},
    {"day": 101, "category": "API", "title": "Geolocation API"},
    {"day": 102, "category": "DSA", "title": "Geometric Algorithms Viz"},
    {"day": 103, "category": "AI/ML", "title": "Text Generation"},
    {"day": 104, "category": "Database", "title": "Asset Management"},
    {"day": 105, "category": "Full-Stack", "title": "Content Management System"},
    {"day": 106, "category": "Frontend", "title": "Pagination Component"},
    {"day": 107, "category": "Python", "title": "System Monitor"},
    {"day": 108, "category": "API", "title": "Payment Gateway Integration"},
    {"day": 109, "category": "DSA", "title": "Network Flow Viz"},
    {"day": 110, "category": "AI/ML", "title": "Fraud Detection"},
    {"day": 111, "category": "Database", "title": "Subscription Manager"},
    {"day": 112, "category": "Full-Stack", "title": "Online Code Compiler"},
    {"day": 113, "category": "Frontend", "title": "Infinite Scroll"},
    {"day": 114, "category": "Python", "title": "Data Validator"},
    {"day": 115, "category": "API", "title": "Social Media Integration"},
    {"day": 116, "category": "DSA", "title": "Computational Geometry Viz"},
    {"day": 117, "category": "AI/ML", "title": "Anomaly Detection"},
    {"day": 118, "category": "Database", "title": "Document Management"},
    {"day": 119, "category": "Full-Stack", "title": "Customer Support Chat"},
    {"day": 120, "category": "Frontend", "title": "Interactive Map"},
    {"day": 121, "category": "Python", "title": "Log Analyzer"},
    {"day": 122, "category": "API", "title": "E-signature API"},
    {"day": 123, "category": "DSA", "title": "Convex Hull Viz"},
    {"day": 124, "category": "AI/ML", "title": "Medical Image Analysis"},
    {"day": 125, "category": "Database", "title": "Project Tracking"},
    {"day": 126, "category": "Full-Stack", "title": "Video Conferencing App"},
    {"day": 127, "category": "Frontend", "title": "Virtual Keyboard"},
    {"day": 128, "category": "Python", "title": "Web Traffic Analyzer"},
    {"day": 129, "category": "API", "title": "OCR API"},
    {"day": 130, "category": "DSA", "title": "Game Theory Viz"},
    {"day": 131, "category": "AI/ML", "title": "Predictive Maintenance"},
    {"day": 132, "category": "Database", "title": "CRM System"},
    {"day": 133, "category": "Full-Stack", "title": "Online Whiteboard"},
    {"day": 134, "category": "Frontend", "title": "Data Table Component"},
    {"day": 135, "category": "Python", "title": "Network Scanner"},
    {"day": 136, "category": "API", "title": "Speech-to-Text API"},
    {"day": 137, "category": "DSA", "title": "Randomized Algorithms Viz"},
    {"day": 138, "category": "AI/ML", "title": "Personalized Learning System"},
    {"day": 139, "category": "Database", "title": "Financial Portfolio Tracker"},
    {"day": 140, "category": "Full-Stack", "title": "Decentralized Application (DApp)"},
    {"day": 141, "category": "Frontend", "title": "Progress Bar Component"},
    {"day": 142, "category": "Python", "title": "Automated Email Reporter"},
    {"day": 143, "category": "API", "title": "Sentiment Analysis API"},
    {"day": 144, "category": "DSA", "title": "Approximation Algorithms Viz"},
    {"day": 145, "category": "AI/ML", "title": "Stock Price Predictor"},
    {"day": 146, "category": "Database", "title": "Task Scheduler"},
    {"day": 147, "category": "Full-Stack", "title": "E-voting System"},
    {"day": 148, "category": "Frontend", "title": "Notification System"},
    {"day": 149, "category": "Python", "title": "System Backup Tool"},
    {"day": 150, "category": "API", "title": "Barcode Scanner API"},
    {"day": 151, "category": "DSA", "title": "Parallel Algorithms Viz"},
    {"day": 152, "category": "AI/ML", "title": "Customer Churn Prediction"},
    {"day": 153, "category": "Database", "title": "Real Estate Listing"},
    {"day": 154, "category": "Full-Stack", "title": "Online Auction Platform"},
    {"day": 155, "category": "Frontend", "title": "Chat Widget"},
    {"day": 156, "category": "Python", "title": "Data Visualization Tool"},
    {"day": 157, "category": "API", "title": "Facial Recognition API"},
    {"day": 158, "category": "DSA", "title": "Quantum Algorithms Viz"},
    {"day": 159, "category": "AI/ML", "title": "Autonomous Driving Simulation"},
    {"day": 160, "category": "Database", "title": "Supply Chain Tracker"},
    {"day": 161, "category": "Full-Stack", "title": "Cryptocurrency Tracker"},
    {"day": 162, "category": "Frontend", "title": "Interactive Dashboard"},
    {"day": 163, "category": "Python", "title": "Network Packet Analyzer"},
    {"day": 164, "category": "API", "title": "Natural Language Processing API"},
    {"day": 165, "category": "DSA", "title": "Bioinformatics Algorithms Viz"},
    {"day": 166, "category": "AI/ML", "title": "Drug Discovery Simulation"},
    {"day": 167, "category": "Database", "title": "Gene Sequencing Database"},
    {"day": 168, "category": "Full-Stack", "title": "Medical Diagnosis System"},
    {"day": 169, "category": "Frontend", "title": "3D Model Viewer"},
    {"day": 170, "category": "Python", "title": "Scientific Calculator"},
    {"day": 171, "category": "API", "title": "Robotics Control API"},
    {"day": 172, "category": "DSA", "title": "Financial Algorithms Viz"},
    {"day": 173, "category": "AI/ML", "title": "Algorithmic Trading Bot"},
    {"day": 174, "category": "Database", "title": "High-Frequency Trading Database"},
    {"day": 175, "category": "Full-Stack", "title": "Decentralized Finance (DeFi) App"},
    {"day": 176, "category": "Frontend", "title": "Augmented Reality (AR) App"},
    {"day": 177, "category": "Python", "title": "Virtual Assistant"},
    {"day": 178, "category": "API", "title": "Quantum Computing API"},
    {"day": 179, "category": "DSA", "title": "Cryptography Algorithms Viz"},
    {"day": 180, "category": "AI/ML", "title": "Cybersecurity Threat Detection"}
]

def get_project_details(day_number):
    if day_number <= len(topic_list):
        return topic_list[day_number - 1]
    else:
        # For days beyond the predefined list, generate a generic project
        # This part will need to be expanded to generate unique projects for 180 days
        # For now, it's a placeholder.
        day_of_week = datetime.date.today().weekday() # 0=Monday, 6=Sunday
        categories = ["Frontend", "Python", "API", "DSA", "AI/ML", "Database", "Full-Stack"]
        category = categories[day_of_week]
        return {"day": day_number, "category": category, "title": f"Generic Project Day {day_number}"}

def create_project_structure(day_number, project_title, category):
    project_slug = project_title.lower().replace(" ", "-")
    folder_name = f"Day-{day_number}_{project_slug}"
    project_path = os.path.join("/home/ubuntu/daily-code-projects", folder_name)

    os.makedirs(project_path, exist_ok=True)
    os.makedirs(os.path.join(project_path, "src"), exist_ok=True)

    with open(os.path.join(project_path, "README.md"), "w") as f:
        f.write(f"# {project_title}\n\n")
        f.write(f"## Category: {category}\n\n")
        f.write("This is a daily coding project.\n")

    with open(os.path.join(project_path, "DESCRIPTION.md"), "w") as f:
        f.write(f"# Description for {project_title}\n\n")
        f.write("Detailed description of the project goes here.\n")

    with open(os.path.join(project_path, "CHANGELOG.md"), "w") as f:
        f.write(f"# Changelog for {project_title}\n\n")
        f.write("- Initial commit\n")

    with open(os.path.join(project_path, ".env.example"), "w") as f:
        f.write("# Example environment variables\n")

    # Determine dependency file based on category
    if category in ["Frontend", "Full-Stack"]:
        with open(os.path.join(project_path, "package.json"), "w") as f:
            f.write(json.dumps({"name": project_slug, "version": "1.0.0", "description": project_title, "main": "index.js", "scripts": {"test": "echo \"Error: no test specified\" && exit 1"}, "keywords": [], "author": "", "license": "MIT"}, indent=2))
    else:
        with open(os.path.join(project_path, "requirements.txt"), "w") as f:
            f.write("# Project dependencies\n")

    return folder_name

def generate_code(project_path, category, project_title):
    # This is a placeholder for actual code generation
    # The complexity of generating real working code will vary greatly depending on the project type and complexity.
    # For now, let's create a simple placeholder file.
    src_path = os.path.join(project_path, "src")
    if category == "Python" or category == "DSA" or category == "AI/ML" or category == "Database":
        with open(os.path.join(src_path, "main.py"), "w") as f:
            f.write(f"""""""""
# {project_title}
# Category: {category}

def main():
    print("Hello from {project_title}!")

if __name__ == "__main__":
    main()
""""""""")
    elif category == "Frontend" or category == "Full-Stack":
        with open(os.path.join(src_path, "index.html"), "w") as f:
            f.write(f"""""""""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project_title}</title>
</head>
<body>
    <h1>{project_title}</h1>
    <p>Welcome to the {project_title} project!</p>
</body>
</html>
""""""""")
        with open(os.path.join(src_path, "style.css"), "w") as f:
            f.write("/* Basic styling */\nbody { font-family: sans-serif; }\n")
        with open(os.path.join(src_path, "script.js"), "w") as f:
            f.write("console.log(\"Hello from JavaScript!\");\n")
    elif category == "API":
        with open(os.path.join(src_path, "app.py"), "w") as f:
            f.write(f"""""""""
# {project_title} API
# Category: {category}

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify(message="Hello from {project_title} API!")

if __name__ == "__main__":
    app.run(debug=True)
""""""""")
        with open(os.path.join(project_path, "requirements.txt"), "a") as f:
            f.write("Flask\n")

def update_root_readme(day_number, date_str, project_title, category):
    readme_path = os.path.join("/home/ubuntu/daily-code-projects", "README.md")
    with open(readme_path, "a") as f:
        f.write(f"| {day_number} | {date_str} | {project_title} | {category} |\n")

def main():
    os.chdir("/home/ubuntu/daily-code-projects")

    # Read the current day from a counter file, or initialize to 0
    day_counter_path = ".day_counter"
    current_day = 0
    if os.path.exists(day_counter_path):
        with open(day_counter_path, "r") as f:
            current_day = int(f.read().strip())
    current_day += 1

    project_details = get_project_details(current_day)
    project_title = project_details["title"]
    category = project_details["category"]
    date_str = datetime.date.today().strftime("%Y-%m-%d")

    folder_name = create_project_structure(current_day, project_title, category)
    generate_code(os.path.join("/home/ubuntu/daily-code-projects", folder_name), category, project_title)

    # Git operations
    os.system("git add .")
    commit_message = f"🚀 Day {current_day}: {project_title} — {category} [{date_str}]"
    os.system(f"git commit -m \"{commit_message}\"")
    os.system("git push origin main")

    update_root_readme(current_day, date_str, project_title, category)

    # Update the day counter
    with open(day_counter_path, "w") as f:
        f.write(str(current_day))

    print(f"Successfully generated and pushed Day {current_day} project: {project_title}")

if __name__ == "__main__":
    main()
