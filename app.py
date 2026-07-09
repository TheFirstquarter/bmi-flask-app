from flask import Flask, render_template, request

app = Flask(__name__)


def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "저체중"
    elif bmi < 23:
        return "정상"
    elif bmi < 25:
        return "과체중"
    else:
        return "비만"


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        height = request.form.get("height", "")
        weight = request.form.get("weight", "")

        try:
            height_val = float(height)
            weight_val = float(weight)

            if height_val <= 0 or weight_val <= 0:
                error = "키와 몸무게는 0보다 큰 값을 입력해주세요."
            else:
                bmi = calculate_bmi(height_val, weight_val)
                category = get_bmi_category(bmi)
                result = {"bmi": bmi, "category": category}
        except ValueError:
            error = "키와 몸무게는 숫자로 입력해주세요."

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
