from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "süper_gizli_anahtar"  # Güvenlik için önemli!

# Örnek Sorular (Sonradan veritabanına çevrilebilir)
QUESTIONS = [
    {
        "question": "Python'ın yaratıcısı kimdir?",
        "options": ["Guido van Rossum", "Elon Musk", "Mark Zuckerberg", "Bill Gates"],
        "correct": "Guido van Rossum"
    },
    {
        "question": "Flask hangi dilde yazılmıştır?",
        "options": ["Java", "Python", "C++", "Ruby"],
        "correct": "Python"
    },
    {
        "question": "Python'da bir liste oluşturmak için hangi parantezler kullanılır?",
        "options": ["()", "[]", "{}", "<>"],
        "correct": "[]"
    },
    {
        "question": "Python'da bir sözlük oluşturmak için hangi parantezler kullanılır?",
        "options": ["()", "[]", "{}", "<>"],
        "correct": "{}"
    },
    {
        "question": "Python'da 'and' operatörünün alternatifi nedir?",
        "options": ["&", "&&", "+", "||"],
        "correct": "&"
    },
    {
        "question": "Python'da bir fonksiyon tanımlamak için hangi anahtar kelime kullanılır?",
        "options": ["function", "def", "func", "define"],
        "correct": "def"
    },
    {
        "question": "Python'da bir sınıf oluşturmak için hangi anahtar kelime kullanılır?",
        "options": ["class", "struct", "object", "type"],
        "correct": "class"
    },
    {
        "question": "Python'da bir değişkenin tipini öğrenmek için hangi fonksiyon kullanılır?",
        "options": ["typeof()", "type()", "instanceof()", "what_is()"],
        "correct": "type()"
    },
    {
        "question": "Python'da bir listeyi sıralamak için hangi metod kullanılır?",
        "options": ["order()", "sort()", "arrange()", "organize()"],
        "correct": "sort()"
    },
    {
        "question": "Python'da bir dosyayı okumak için hangi mod kullanılır?",
        "options": ["r", "w", "a", "x"],
        "correct": "r"
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start")
def start_quiz():
    session["question_index"] = 0  # Hangi soruda olduğunu takip et
    session["score"] = 0  # Skoru sıfırla
    return redirect(url_for("show_question"))

@app.route("/question")
def show_question():
    index = session.get("question_index", 0)
    if index >= len(QUESTIONS):
        return redirect(url_for("result"))
    question = QUESTIONS[index]
    return render_template("quiz.html", question=question, index=index)

@app.route("/answer", methods=["POST"])
def handle_answer():
    user_answer = request.form.get("answer")
    index = session.get("question_index", 0)
    
    # Cevabı kontrol et
    if user_answer == QUESTIONS[index]["correct"]:
        session["score"] += 10
    
    # Sonraki soruya geç
    session["question_index"] = index + 1
    return redirect(url_for("show_question"))

@app.route("/result")
def result():
    score = session.get("score", 0)
    return render_template("result.html", score=score, total=len(QUESTIONS)*10)

if __name__ == "__main__":
    app.run(debug=True) 
