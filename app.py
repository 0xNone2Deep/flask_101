from flask import Flask, render_template, jsonify

app = Flask(__name__)

specialists = [
    {
        'fullname': "Hope Scott",
        'specialty': "Neurosurgery",
        'council_reg': "MCM/SP/6543",
        'phone': "0882.292.6648",
        'email': "hopescott@gmail.com",
        'location': "Lilongwe, Malawi",
        'experience': 5,
        'rating': 4.0,
        'brief_bio':
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore harum, placeat aperiam ex nulla voluptate explicabo ea quos saepe? Explicabo pariatur beatae earum, aperiam rerum        eligendi id ratione non tempore vero voluptate dignissimos totam dolorem dolor velit quisquam.",
        'photos': {
            'thumbnail': "./img/dr-lisa.png",
            'fullphoto': "./img/dr-banda.png",
        },
        'constypes': [
            {
                'cons_name': "Introduction 'phone' call",
                'cons_duration': "10 min",
            },
            {
                'cons_name': "face-toface consultation",
                'cons_duration': "20 min",
            },
            {
                'cons_name': "Follow-up 'phone' consultation",
                'cons_duration': "10 min",
            },
        ],
    },
    {
        'fullname': "Yohannie Mlombe",
        'specialty': "Haematologist",
        'council_reg': "MCM/SP/7654",
        'phone': "0882.292.6648",
        'email': "hopescott@gmail.com",
        'location': "Lilongwe, Malawi",
        'experience': 7,
        'rating': 4.8,
        'brief_bio':
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore harum, placeat aperiam ex nulla voluptate explicabo ea quos saepe? Explicabo pariatur beatae earum, aperiam rerum        eligendi id ratione non tempore vero voluptate dignissimos totam dolorem dolor velit quisquam.",
        'photos': {
            'thumbnail': "./img/dr-lisa.png",
            'fullphoto': "./img/dr-banda.png",
        },
        'constypes': [
            {
                'cons_name': "Introduction 'phone' call",
                'cons_duration': "10 min",
            },
            {
                'cons_name': "face-toface consultation",
                'cons_duration': "20 min",
            },
            {
                'cons_name': "Follow-up 'phone' consultation",
                'cons_duration': "10 min",
            },
        ],
    },
    {
        'fullname': "Lisa Kamanga",
        'specialty': "Oncologist",
        'council_reg': "MCM/SP/8765",
        'phone': "0882.292.6648",
        'email': "hopescott@gmail.com",
        'location': "Blantyre, Malawi",
        'experience': 9,
        'rating': 3.8,
        'brief_bio':
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore harum, placeat aperiam ex nulla voluptate explicabo ea quos saepe? Explicabo pariatur beatae earum, aperiam rerum        eligendi id ratione non tempore vero voluptate dignissimos totam dolorem dolor velit quisquam.",
        'photos': {
            'thumbnail': "./img/dr-lisa.png",
            'fullphoto': "./img/dr-banda.png",
        },
        'constypes': [
            {
                'cons_name': "Introduction 'phone' call",
                'cons_duration': "10 min",
            },
            {
                'cons_name': "face-toface consultation",
                'cons_duration': "20 min",
            },
            {
                'cons_name': "Follow-up 'phone' consultation",
                'cons_duration': "10 min",
            },
        ],
    },
    {
        'fullname': "Benjamin Phiri",
        'specialty': "Paediatrician",
        'council_reg': "MCM/SP/9876",
        'phone': "0882.292.6648",
        'email': "hopescott@gmail.com",
        'location': "Blantyre, Malawi",
        'experience': 10,
        'rating': 4.0,
        'brief_bio':
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore harum, placeat aperiam ex nulla voluptate explicabo ea quos saepe? Explicabo pariatur beatae earum, aperiam rerum        eligendi id ratione non tempore vero voluptate dignissimos totam dolorem dolor velit quisquam.",
        'photos': {
            'thumbnail': "./img/dr-lisa.png",
            'fullphoto': "./img/dr-banda.png",
        },
        'constypes': [
            {
                'cons_name': "Introduction 'phone' call",
                'cons_duration': "10 min",
            },
            {
                'cons_name': "face-toface consultation",
                'cons_duration': "20 min",
            },
            {
                'cons_name': "Follow-up 'phone' consultation",
                'cons_duration': "10 min",
            },
        ],
    },
    {
        'fullname': "Thandie Lungu",
        'specialty': "Dentist",
        'council_reg': "MCM/SP/0987",
        'phone': "0882.292.6648",
        'email': "hopescott@gmail.com",
        'location': "Mzuzu, Malawi",
        'experience': 14,
        'rating': 4.6,
        'brief_bio':
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore harum, placeat aperiam ex nulla voluptate explicabo ea quos saepe? Explicabo pariatur beatae earum, aperiam rerum        eligendi id ratione non tempore vero voluptate dignissimos totam dolorem dolor velit quisquam.",
        'photos': {
            'thumbnail': "./img/dr-lisa.png",
            'fullphoto': "./img/dr-banda.png",
        },
        'constypes': [
            {
                'cons_name': "Introduction 'phone' call",
                'cons_duration': "10 min",
            },
            {
                'cons_name': "face-toface consultation",
                'cons_duration': "20 min",
            },
            {
                'cons_name': "Follow-up 'phone' consultation",
                'cons_duration': "10 min",
            },
        ],
    },
]

@app.route("/")
def hello_world():
    return render_template('home.html', docs=specialists)

@app.route("/doctors")
def learn():
    return jsonify(specialists)

@app.route("/documentation")
def documentation():
    return render_template('home.html')

@app.route("/contact")
def contact():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)