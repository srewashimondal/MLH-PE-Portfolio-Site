from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow")

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/hobbies')
def hobbies():
    hobbies_list = [
        {
            'icon': 'fa-camera',  
            'title': 'Photography',
            'description': 'Capturing beuatiful moments with my family and friends on my digital camera.',
            'tags': ['Portrait Photography', 'Landscape', 'Street Photography', 'Selfies']
        },
        {
            'icon': 'fa-music',
            'title': 'Music',
            'description': 'Playing and instrument and listening to all types of music.',
            'tags': ['Harmonium', 'Bollywood', 'Bengali Classical Songs']
        },
        {
            'icon': 'fa-film',
            'title': 'Movies',
            'description': 'With my loved ones, I love to watch movies to keep me up on my toes!',
            'tags': ['Horror', 'Scary', 'Thriller', 'Suspense']
        },
        {
            'icon': 'fa-star',
            'title': 'Playing Games',
            'description': 'Now that it is summer vacation, my close college friends and I have Game Nights on Fridays!',
            'tags': ['Discord Games', 'CoolMathGames', 'Multi-player Games']
        },
        {
            'icon': 'fa-home',
            'title': 'Cooking',
            'description': 'I am not very good at cooking haha, but I definitely love to learn and experiment both myself and with family :))',
            'tags': ['Noodles', 'Pasta', 'Dumplings', 'Curry']
        },
        {
            'icon': 'fa-globe',
            'title': 'Traveling',
            'description': 'As of today, I have not traveled to many countries, but I love the concept of traveling and plan to travel a lot in the future with my family.',
            'tags': ['United States of America', 'Canada', 'Bangladesh', 'India',]
        },
    ]
    return render_template('hobbies.html', hobbies=hobbies_list, title="Hobbies")

