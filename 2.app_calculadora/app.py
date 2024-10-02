# importamos las clases y metodos
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET',"POST"])
def aritmetica():
    if request.method == "POST":
        # valores que recibo de form n1,n2 son pasados
        num1 = float(request.form.get('n1'))
        num2 = float(request.form.get('n2'))
        # realizamos operaciones aritmeticas
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2
        return render_template('index.html', total_suma=suma,
                                             total_resta=resta,
                                             total_multiplicacion=multiplicacion,
                                             total_division=division )
    return render_template('index.html')

@app.route('/divisas', methods=['GET',"POST"])
def divisas():
    if request.method == "POST":
        # valores que recibo de form n1 son pasados
        num1 = float(request.form.get('n1'))
        # realizamos operaciones
        multiplicacion = num1 * 4.213
        return render_template('divisas.html', total_res=multiplicacion)
    return render_template('divisas.html')


if __name__ == "__main__":
    app.run(debug=True)



