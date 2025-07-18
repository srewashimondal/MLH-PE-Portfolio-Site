from app import app
from flask import render_template

from flask import request
from playhouse.shortcuts import model_to_dict
from app.__init__ import TimelinePost


@app.route("/")
def index():
    return render_template("index.html", title="MLH Fellow")


@app.route("/education")
def education():
    return render_template("education.html", title="Education")


@app.route("/map")
def map():
    return render_template("map.html", title="Map")


@app.route("/experience")
def experience():
    experiences = [
        {
            "title": "MLH Production Engineering Fellow",
            "company": "Meta x Major League Hacking",
            "location": "Remote",
            "date": "2025",
            "type": "Fellowship",
            "description": "Learning and applying Linux-based development by building scalable applications on DigitalOcean with Docker and Kubernetes, automating CI/CD pipelines using GitHub and GitHub Actions, and collaborating in a remote SCRUM team.",
            "achievements": [
                "Collaborated with 10 fellows",
                "Learned production engineering practices",
                "Learned to use Linux commands and apply for lessons",
            ],
            "technologies": [
                "Linux",
                "HTML",
                "CSS",
                "Flask",
                "DigitalOcean",
                "VPS",
                "Git",
                "Github",
            ],
            "icon": "fa-star",
        },
        {
            "title": "Artificial Intelligence Fellow",
            "company": "AI4ALL",
            "location": "Remote",
            "date": "2025",
            "type": "Fellowship",
            "description": "Building a personalized book recommendation system using NLP techniques and KNN on Goodreads datasets. Applying Python, Pandas, NumPy, Scikit-Learn and Matplotlib to analyze user inputs in Google Collab.",
            "achievements": [
                "Cleaned and processed the Goodreads dataset using Python, Pandas, and NumPy to extract meaningful features for model training and evaluation.",
                "Created clear data visualizations with Matplotlib to communicate user rating distributions and recommendation results to stakeholders in Google Colab.",
                "Participated in weekly meetings with peers and mentors",
            ],
            "technologies": [
                "Python",
                "Google Colab",
                "Numpy",
                "Pandas",
                "Matplotlib",
                "Scikit-learn",
            ],
            "icon": "fa-book",
        },
        {
            "title": "AI Studio Intern",
            "company": "Meta",
            "location": "Remote",
            "date": "2024-2025",
            "type": "Internship",
            "description": "Developed and fine-tuned a BERT-based NLP model using the RedditBias dataset to identify and evaluate demographic bias in text datasets, leveraging Hugging Face transformers and custom evaluation metrics for robust bias detection.",
            "achievements": [
                "Created a BERT-based NLP model to find and measure bias in Reddit comments.",
                "Prepared and cleaned large text datasets to improve model results.",
            ],
            "technologies": [
                "Python",
                "Google Colab",
                "Numpy",
                "Pandas",
                "Matplotlib",
                "Scikit-learn",
            ],
            "icon": "fa-code",
        },
        {
            "title": "Software Engineering Intern",
            "company": "MyFiLi.com",
            "location": "Remote",
            "date": "2024",
            "type": "Internship",
            "description": "Programmed 5 interactive financial literacy games using JavaScript and event-driven programming in an Agile/Scrum environment, contributing to a 35% increase in users and reaching 5,000+ students across 20+ schools through engaging, hands-on learning experiences.",
            "achievements": [
                "Reduced page load times by 30% through front-end debugging and optimization using Chrome Developer Tools.",
                "Managed tasks and projects efficiently using Trello, Slack, Airtable, and Microsoft applications.",
                "Utilized Jupyter Notebooks and Airflow to support tasks.",
            ],
            "technologies": [
                "Python",
                "Javascript",
                "Visual Studio Code",
                "Git",
                "Github",
                "Flask",
            ],
            "icon": "fa-keyboard",
        },
    ]
    return render_template(
        "experience.html", experiences=experiences, title="Experience"
    )


@app.route("/hobbies")
def hobbies():
    hobbies_list = [
        {
            "icon": "fa-camera",
            "title": "Photography",
            "description": "Capturing beautiful moments with my family and friends on my digital camera.",
            "tags": [
                "Portrait Photography",
                "Landscape",
                "Street Photography",
                "Selfies",
            ],
        },
        {
            "icon": "fa-music",
            "title": "Music",
            "description": "Playing and instrument and listening to all types of music.",
            "tags": ["Harmonium", "Bollywood", "Bengali Classical Songs"],
        },
        {
            "icon": "fa-film",
            "title": "Movies",
            "description": "With my loved ones, I love to watch movies to keep me up on my toes!",
            "tags": ["Horror", "Scary", "Thriller", "Suspense"],
        },
        {
            "icon": "fa-star",
            "title": "Playing Games",
            "description": "Now that it is summer vacation, my close college friends and I have Game Nights on Fridays!",
            "tags": ["Discord Games", "CoolMathGames", "Multi-player Games"],
        },
        {
            "icon": "fa-home",
            "title": "Cooking",
            "description": "I am not very good at cooking haha, but I definitely love to learn and experiment both myself and with family :))",
            "tags": ["Noodles", "Pasta", "Dumplings", "Curry"],
        },
        {
            "icon": "fa-globe",
            "title": "Traveling",
            "description": "As of today, I have not traveled to many countries, but I love the concept of traveling and plan to travel a lot in the future with my family!!",
            "tags": [
                "United States of America",
                "Canada",
                "Bangladesh",
                "India",
            ],
        },
    ]
    return render_template("hobbies.html", hobbies=hobbies_list, title="Hobbies")


@app.route("/api/timeline_post", methods=["POST"])
def post_time_line_post():
    import re
    
    name = request.form.get("name")
    email = request.form.get("email") 
    content = request.form.get("content")
    
    # Validate required fields
    if not name:
        return "Invalid name", 400
    if not email:
        return "Invalid email", 400
    if not content:
        return "Invalid content", 400
    
    # Validate email format
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        return "Invalid email", 400
    
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

@app.route("/api/timeline_post", methods=["GET"])
def get_time_line_post():
    return {
        "timeline_posts": [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }


@app.route("/timeline")
def timeline():
    return render_template("timeline.html", title="Timeline")
