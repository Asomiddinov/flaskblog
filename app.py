from __init__ import app, db
from models import Clients, Mine, User, Posts
from flask import redirect, render_template, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import logout_user, login_required, login_user, current_user
from datetime import datetime
from pytz import timezone
asia_tz = timezone('Asia/Tashkent')


@app.route("/create")
def create():
    db.create_all()
    return "All tables are created!!!"


@app.route("/signup/", methods=["GET", "POST"])
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        comment = str(password1)
        role = request.form.get("role")
        user = User.query.filter_by(email=email).all()
        if user:
            flash("This user/email is already in use!", category="error")
        elif len(email) < 5:
            flash("Email must be at least 6 characters!", category="error")
        elif len(username) < 4:
            flash("Username must be at least 5 characters", category="error")
        elif password1 != password2:
            flash("Passwords do not match", category="error")
        elif len(password1) < 4:
            flash("Password must have at least 5 characters!", category="error")
        else:
            new_user = User(email=email, username=username, comment=comment, role=role,
                            password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("User created & logged in successfully", category="success")
            return redirect(url_for("index"))
    return render_template("signup.html", form=Mine(), user=current_user)


@app.route("/login", methods=["GET", "POST"])
@app.route("/login/", methods=["GET", "POST"])
@app.route("/signin", methods=["GET", "POST"])
@app.route("/signin/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("You're logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("index"))
            else:
                flash("Incorrect password!", category="error")
        else:
            flash("There's no this kind of user", category="error")
    return render_template("login.html", user=current_user)


@app.route("/logout")
@app.route("/logout/")
def logout():
    logout_user()
    flash("You're logged out", category="success")
    return redirect(url_for("login"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/posts/", methods=["GET", "POST"])
@app.route("/posts", methods=["GET", "POST"])
@login_required
def posts():
    if request.method == "POST":
        patient = request.form["patient"]
        date_str = request.form.get('date')
        pat_code = request.form["pat_code"]
        pat_code1 = request.form["pat_code1"]
        pat_code2 = request.form["pat_code2"]
        pat_code3 = request.form["pat_code3"]
        pat_code4 = request.form["pat_code4"]
        pat_code5 = request.form["pat_code5"]
        pat_code6 = request.form["pat_code6"]
        pat_code7 = request.form["pat_code7"]
        pat_code8 = request.form["pat_code8"]
        pat_code9 = request.form["pat_code9"]
        pat_code10 = request.form["pat_code10"]
        pat_code11 = request.form["pat_code11"]
        pat_code12 = request.form["pat_code12"]
        pat_code13 = request.form["pat_code13"]
        pat_code14 = request.form["pat_code14"]
        pat_code15 = request.form["pat_code15"]
        if date_str:
            date = datetime.strptime(
                date_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc).astimezone(asia_tz)
        else:
            date = datetime.now(asia_tz)
        post = Posts(date=date, patient=patient,
                     pat_code=pat_code, pat_code1=pat_code1, pat_code2=pat_code2, pat_code3=pat_code3, pat_code4=pat_code4,
                     pat_code5=pat_code5, pat_code6=pat_code6, pat_code7=pat_code7, pat_code8=pat_code8, pat_code9=pat_code9, pat_code10=pat_code10,
                     pat_code11=pat_code11, pat_code12=pat_code12, pat_code13=pat_code13, pat_code14=pat_code14, pat_code15=pat_code15)
        db.session.add(post)
        db.session.commit()
        return render_template("posts.html", posts=Posts.query.all())
    else:
        return render_template("posts.html", posts=Posts.query.all())


@app.route("/registration", methods=["GET", "POST"])
@login_required
def registration():
    form = Mine()
    client = Clients(fullname=request.form.get("fullname"),
                     email=request.form.get("email"))
    if request.method == "POST":
        if client:
            db.session.add(client)
            db.session.commit()
            flash(message="Added to db", category="success")
            return redirect(url_for("regdata"))
        else:
            flash(message="Bu client avvaldan mavjud!", category="error")
            return redirect(url_for("registration"))
    return render_template("registration.html", form=form, client=client)


@app.route("/regdata", methods=["GET", "POST"])
def regdata():
    form = Mine()
    if form.validate_on_submit:
        client = Clients.query.all()
        return render_template("regdata.html", form=form, client=client)


if __name__ == "__main__":
    app.run(debug=True)
