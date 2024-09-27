from flask import Flask, render_template, request, redirect, url_for, flash
from flask_socketio import SocketIO, send
import sqlite3
from test import get_response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# work exp database
def create_work_db():
    # Connect to SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect('work_experience.db')
    cursor = conn.cursor()

    # Create a table for work experiences
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS work (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        company TEXT NOT NULL,
        location TEXT NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        details TEXT NOT NULL
    )
    ''')

    # Clear the existing records in the work table
    cursor.execute('DELETE FROM work')

    # Insert sample data if the table is empty
    cursor.execute('SELECT COUNT(*) FROM work')
    if cursor.fetchone()[0] == 0:  # Check if the table is empty
        cursor.execute('''
       INSERT INTO work (title, company, location, start_date, end_date, details) VALUES
        ('Software Engineering Intern', 'Amazon Web Services (AWS)', 'East Palo Alto', 'May 2024', 'Aug 2024', 
            'Developed an ECS/Fargat service with REST endpoints for S3 file retrieval, reducing manual intervention. 
             Designed and implemented an automated deployment pipeline using AWS service like CodePipeline and CodeDeploy, 
             improving deployment speed from 8 hours to 1 minute. 
             Optimized the handling of config changes, improving system efficiency and reducing downtime.'),
        ('Lead Software Engineer', 'Fidelity Investments', 'India', 'Dec 2022', 'Jun 2023', 
            'Led the development of user interfaces and automated test suites, resulting in a 65% reduction in time to market. 
             Collaborated with cross-functional teams to enhance software functionality and performance.'),
        ('Software Engineer', 'Fidelity Investments', 'India', 'Dec 2017', 'Dec 2022', 
            'Developed a backend system that streamlined configuration picking for testing, reducing test prep time from 12 hours to instantaneous. 
             Implemented CI/CD pipelines to automate testing and deployment processes.')

        ''')
    
    conn.commit()
    conn.close()

# education database
def create_education_db():
    # Connect to SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect('education.db')
    cursor = conn.cursor()

    # Create a table for education experiences
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS education (
        id INTEGER PRIMARY KEY,
        institution TEXT NOT NULL,
        degree TEXT NOT NULL,
        duration TEXT NOT NULL,
        grade TEXT
    )
    ''')

    # Clear the existing records in the education table
    cursor.execute('DELETE FROM education')

    # Insert sample data if the table is empty
    cursor.execute('SELECT COUNT(*) FROM education')
    if cursor.fetchone()[0] == 0:  # Check if the education table is empty
        cursor.execute('''
        INSERT INTO education (institution, degree, duration, grade) VALUES
        ('San Jose State University, San Jose', 'Master of Science - MS in Computer Science', '2023 - 2025', '4'),
        ('Visvesvaraya National Institute Of Technology, Nagpur, India', 'Bachelor of Technology - BTech in CSE', '2013 - 2017', '9.37'),
        ('Vimla Convent School, Odisha, India', 'High School', '2000 - 2010', '92.7')
        ''')
       
    conn.commit()
    conn.close() 

# Publications Database
def create_publications_db():
    conn = sqlite3.connect('publications.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS publications (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        url TEXT NOT NULL,
        description TEXT NOT NULL
    )
    ''')

    cursor.execute('DELETE FROM publications')

    cursor.execute('SELECT COUNT(*) FROM publications')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
        INSERT INTO publications (title, url, description) VALUES
            ('Scalable and explainable legal prediction', 'https://link.springer.com/article/10.1007/s10506-020-09273-1', 
            'Legal decision-support systems have the potential to improve access to justice, administrative efficiency, and judicial consistency...'),
            ('AI-Driven Justice: Evaluating the Impact of Artificial Intelligence on Legal Systems', 
            'https://www.researchgate.net/publication/381926291_AI-Driven_Justice_Evaluating_the_Impact_of_Artificial_Intelligence_on_Legal_Systems', 
            'This integrative literature review (ILR) examines the impact of artificial intelligence (AI) on legal systems, focusing on technologies such as...'),
            ('Advances in Artificial Intelligence-Empowered Decision Support Systems', 
            'https://link.springer.com/book/10.1007/978-3-031-62316-5', 
            'Decision Support Systems (DSSs) are Software and Information Systems which make use of various data and business models...')
        ''')
     
    conn.commit()
    conn.close()   

# Awards Database
def create_awards_db():
    conn = sqlite3.connect('awards.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS awards (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        details TEXT NOT NULL
    )
    ''')

    cursor.execute('DELETE FROM awards')

    cursor.execute('SELECT COUNT(*) FROM awards')
    cursor.execute('SELECT COUNT(*) FROM awards')
    if cursor.fetchone()[0] == 0:  # Check if the awards table is empty
        cursor.execute('''
        INSERT INTO awards (title, details) VALUES
        ('AWS Certified Developer – Associate', 'Achieved certification on the first attempt, demonstrating proficiency in developing and maintaining applications on AWS.'),
        ('Most Notable Contributor Award at Fidelity Investments', 'Recognized for significant contributions to the development of user interfaces and automated test suites, leading to a substantial reduction in time to market.'),
        ('Participation in GIDS Conference', 'Attended the Global Software Engineering Conference in Bangalore, gaining insights into the latest trends and best practices in software engineering.')
        ''')
    
    conn.commit()
    conn.close()

# Research Database
def create_research_db():
    conn = sqlite3.connect('research.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS research (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        duration TEXT NOT NULL,
        details TEXT NOT NULL
    )
    ''')

    cursor.execute('DELETE FROM research')

    cursor.execute('SELECT COUNT(*) FROM research')
    if cursor.fetchone()[0] == 0:  # Check if the research table is empty
        cursor.execute('''
        INSERT INTO research (title, duration, details) VALUES
        ('AI-Powered Legal Decision Support System', 'Aug 2024 - Present',
            'Developing a system that predicts case outcomes and sentencing using large language models (LLaMA 3.1). Dataset: Supreme Court Judgment Prediction dataset (Kaggle). Focus Areas: Fine-tuning models on legal documents, charges, and court filings for better classification and prediction.'),
        ('Blockchain Project: Ledger using Ethereum', 'Aug 2017 - Dec 2018',
            'Contributed to a blockchain-based project that converted transfer agent transactions into blockchain ledger format for secure transactions.'),
        ('Cloud Infrastructure Automation', 'May 2024 - Aug 2024',
            'Internship at AWS: Developed an ECS/Fargate service for automated S3 file retrieval and optimized config change handling to reduce deployment time.')
        ''')

    conn.commit()
    conn.close()

def create_mentoring_db():
    conn = sqlite3.connect('mentoring.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mentoring (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        feedback TEXT NOT NULL
    )
    ''')

    cursor.execute('DELETE FROM mentoring')

    cursor.execute('SELECT COUNT(*) FROM mentoring')
    if cursor.fetchone()[0] == 0:  # Check if the mentoring table is empty
        cursor.execute('''
       INSERT INTO mentoring (title, description, feedback) VALUES
('Mentorship Program at San Jose State University', 
    'As a peer mentor, I provide guidance and support to undergraduate students in computer science. This involves helping them navigate academic challenges, offering advice on course selection, and sharing resources for personal and professional development. I organize study groups and workshops on topics such as coding practices and job interview preparation, fostering a collaborative learning environment.',
    '"Alisha''s mentorship has been invaluable. She always takes the time to explain complex concepts in a way that''s easy to understand, and her encouragement has motivated me to pursue my interests in machine learning." – Sarah J., Mentee'),
('Leadership in Hackathon Teams', 
    'Led teams during various hackathons, coordinating tasks, setting project goals, and ensuring effective communication among team members. I focused on harnessing each member''s strengths, facilitating brainstorming sessions, and driving the project to completion under tight deadlines.',
    '"Alisha is an exceptional leader. Her ability to motivate the team and keep us focused on our goals made a significant difference in our success." – Mark L., Team'),
('Volunteer Coordinator for Tech for Good Hackathon', 
    'Coordinated volunteers for the Tech for Good Hackathon, managing logistics, scheduling, and ensuring a smooth experience for participants. I facilitated communication between volunteers and organizers, helping to create an inclusive and supportive environment.',
    '"Alisha''s organizational skills were impressive. She kept everything running smoothly and was always available to help out when needed." – Emily R., Fellow Coordinator')
        ''')

    conn.commit()
    conn.close()


# Call create_db when the application starts
create_work_db()
create_publications_db()
create_awards_db()
create_education_db()
create_research_db()
create_mentoring_db()

def get_work_experience():
    conn = sqlite3.connect('work_experience.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title, company, location, start_date, end_date, details FROM work')
    work_experience = cursor.fetchall()
    conn.close()
    return work_experience

def get_publications():
    conn = sqlite3.connect('publications.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title, url, description FROM publications')
    publications = cursor.fetchall()
    conn.close()
    return publications

def get_awards():
    conn = sqlite3.connect('awards.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title, details FROM awards')
    awards = cursor.fetchall()
    conn.close()
    return awards

def get_education():
    conn = sqlite3.connect('education.db')
    cursor = conn.cursor()
    cursor.execute('SELECT institution, degree, duration, grade FROM education')
    education = cursor.fetchall()
    conn.close()
    return education    

def get_research():
    conn = sqlite3.connect('research.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title, duration, details FROM research')
    research = cursor.fetchall()
    conn.close()
    return research

def get_mentoring():
    conn = sqlite3.connect('mentoring.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title, description, feedback FROM mentoring')
    mentoring = cursor.fetchall()
    conn.close()
    return mentoring

# Route to serve the HTML page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# Route to serve the HTML page
@app.route('/about')
def about():
    return render_template('about.html')

# Route to serve the HTML page
# @app.route('/education')
# def education():
#     return render_template('education.html')

@app.route('/education')
def education():
    education_list = get_education()  # Fetch education data
    return render_template('education.html', education=education_list)    

# Route to serve the HTML page
# @app.route('/research')
# def research():
#     return render_template('research.html')

@app.route('/research')
def research():
    research_list = get_research()  # Fetch research data
    return render_template('research.html', research=research_list)

# Route to serve the HTML page
# @app.route('/work')
# def work():
#     return render_template('work.html')

@app.route('/work')
def work():
    work_experience = get_work_experience()  # Fetch work data
    return render_template('work.html', work_experience=work_experience)

# Route to serve the HTML page
# @app.route('/publications')
# def publications():
#     return render_template('publications.html')

@app.route('/publications')
def publications():
    publications = get_publications()  # Fetch publication data
    return render_template('publications.html', publications=publications)

# # Route to serve the HTML page
# @app.route('/awards')
# def awards():
#     return render_template('awards.html')

@app.route('/awards')
def awards():
    awards = get_awards()  # Fetch awards data
    return render_template('awards.html', awards=awards)

# Route to serve the HTML page
# @app.route('/mentoring')
# def mentoring():
#     return render_template('mentoring.html')

@app.route('/mentoring')
def mentoring():
    mentoring_list = get_mentoring()  # Fetch mentoring data
    return render_template('mentoring.html', mentoring=mentoring_list)

# Route to serve the HTML page
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# Route to serve the HTML page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print('Received:', name, email, message)
        
        # Process the form data (e.g., save to database, send an email, etc.)
        flash(f"Thank you {name}, your message has been received!", 'success')
        
        return redirect(url_for('contact'))
    return render_template('contact.html')

# Route to serve the HTML page
@app.route('/chat')
def home():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(msg):
    print(f'Received message: {msg}')
    send(f'{get_response(msg)}', broadcast=True)
    # send(f' You said: {msg}', broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
