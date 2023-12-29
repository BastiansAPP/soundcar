from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Endpoint dla oryginalnej podstrony
@app.route('/page')
def page():
    return render_template('page.html')

# Endpoint dla nowej podstrony
@app.route('/page1')
def page1():
    return render_template('page1.html')

# Endpoint dla nowej podstrony 2
@app.route('/page2')
def page2():
    return render_template('page2.html')

# Endpoint dla nowej podstrony 3
@app.route('/page3')
def page3():
    return render_template('page3.html')

# Endpoint dla nowej podstrony 4
@app.route('/page4')
def page4():
    return render_template('page4.html')
    
# Endpoint dla nowej podstrony 5
@app.route('/page5')
def page5():
    return render_template('page5.html')
    
# Endpoint dla nowej podstrony 6
@app.route('/page6')
def page6():
    return render_template('page6.html')
    
# Endpoint dla nowej podstrony 7
@app.route('/page7')
def page7():
    return render_template('page7.html')
    
# Endpoint dla nowej podstrony 8
@app.route('/page8')
def page8():
    return render_template('page8.html')
    
# Endpoint dla nowej podstrony 9
@app.route('/page9')
def page9():
    return render_template('page9.html')
    
# Endpoint dla nowej podstrony 10
@app.route('/page10')
def page10():
    return render_template('page10.html')
    
# Endpoint dla nowej podstrony 11
@app.route('/page11')
def page11():
    return render_template('page11.html')

# Endpoint dla nowej podstrony 12
@app.route('/page12')
def page12():
    return render_template('page12.html')
    
# Endpoint dla nowej podstrony 13
@app.route('/page13')
def page13():
    return render_template('page13.html')
    
# Endpoint dla nowej podstrony 14
@app.route('/page14')
def page14():
    return render_template('page14.html')
    
# Endpoint dla nowej podstrony 15
@app.route('/page15')
def page15():
    return render_template('page15.html')
    
# Endpoint dla nowej podstrony 16
@app.route('/page16')
def page16():
    return render_template('page16.html')
    
# Endpoint dla nowej podstrony 17
@app.route('/page17')
def page17():
    return render_template('page17.html')
    
# Endpoint dla nowej podstrony 18
@app.route('/page18')
def page18():
    return render_template('page18.html')
    
# Endpoint dla nowej podstrony 19
@app.route('/page19')
def page19():
    return render_template('page19.html')
    
# Endpoint dla nowej podstrony 20
@app.route('/page20')
def page20():
    return render_template('page20.html')
    
# Endpoint dla nowej podstrony 21
@app.route('/page21')
def page21():
    return render_template('page21.html')
    
# Endpoint dla nowej podstrony 22
@app.route('/page22')
def page22():
    return render_template('page22.html')
    
# Endpoint dla nowej podstrony 23
@app.route('/page23')
def page23():
    return render_template('page23.html')
    
# Endpoint dla nowej podstrony 24
@app.route('/page24')
def page24():
    return render_template('page24.html')
    
# Endpoint dla nowej podstrony 25
@app.route('/page25')
def page25():
    return render_template('page25.html')
    
# Endpoint dla nowej podstrony 26
@app.route('/page26')
def page26():
    return render_template('page26.html')
    
# Endpoint dla nowej podstrony 27
@app.route('/page27')
def page27():
    return render_template('page27.html')
    
# Endpoint dla nowej podstrony 28
@app.route('/page28')
def page28():
    return render_template('page28.html')
    
# Endpoint dla nowej podstrony 29
@app.route('/page29')
def page29():
    return render_template('page29.html')

# Endpoint dla oryginalnej podstrony
@app.route('/submit', methods=['POST'])
def submit():
    data = request.form

    with open('odpowiedzi.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound1: {data['rating1']} | sound2: {data['rating2']}\n")

    # Przekieruj do nowej podstrony po zakończeniu zapisu
    return redirect(url_for('page1'))

# Endpoint dla nowej podstrony
@app.route('/submit_new', methods=['POST'])
def submit_new():
    data = request.form

    with open('odpowiedzi1.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound1: {data['rating2']} | sound3: {data['rating3']}\n")

    # Przekieruj do nowej podstrony 2 po zakończeniu zapisu
    return redirect(url_for('page2'))

# Endpoint dla nowej podstrony 2
@app.route('/submit_new2', methods=['POST'])
def submit_new2():
    data = request.form

    with open('odpowiedzi2.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound1: {data['rating3']} | sound4: {data['rating4']}\n")

    # Przekieruj do nowej podstrony 3 po zakończeniu zapisu
    return redirect(url_for('page3'))

# Endpoint dla nowej podstrony 3
@app.route('/submit_new3', methods=['POST'])
def submit_new3():
    data = request.form

    with open('odpowiedzi3.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound1: {data['rating4']} | sound5: {data['rating5']}\n")

    # Przekieruj do nowej podstrony 4 po zakończeniu zapisu
    return redirect(url_for('page4'))

# Endpoint dla nowej podstrony 4
@app.route('/submit_new4', methods=['POST'])
def submit_new4():
    data = request.form

    with open('odpowiedzi4.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound1: {data['rating4']} | sound6: {data['rating5']}\n")

    # Przekieruj do nowej podstrony 4 po zakończeniu zapisu
    return redirect(url_for('page5'))
    
# Endpoint dla nowej podstrony 5
@app.route('/submit_new5', methods=['POST'])
def submit_new5():
    data = request.form

    with open('odpowiedzi5.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound2: {data['rating4']} | sound3: {data['rating5']}\n")

    # Przekieruj do nowej podstrony 5 po zakończeniu zapisu
    return redirect(url_for('page6'))
    
# Endpoint dla nowej podstrony 6
@app.route('/submit_new6', methods=['POST'])
def submit_new6():
    data = request.form

    with open('odpowiedzi6.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound2: {data['rating4']} | sound4: {data['rating5']}\n")

    # Przekieruj do nowej podstrony 6 po zakończeniu zapisu
    return redirect(url_for('page7'))
    
# Endpoint dla nowej podstrony 7
@app.route('/submit_new7', methods=['POST'])
def submit_new7():
    data = request.form

    with open('odpowiedzi7.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound2: {data['rating4']} | sound5: {data['rating5']}\n")

    # Przekieruj do nowej podstrony 7 po zakończeniu zapisu
    return redirect(url_for('page8'))
    
# Endpoint dla nowej podstrony 8
@app.route('/submit_new8', methods=['POST'])
def submit_new8():
    data = request.form

    with open('odpowiedzi8.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound2: {data['rating4']} | sound6: {data['rating5']}\n")

    # Przekieruj do nowej podstrony 8 po zakończeniu zapisu
    return redirect(url_for('page9'))
    
# Endpoint dla nowej podstrony 9
@app.route('/submit_new9', methods=['POST'])
def submit_new9():
    data = request.form

    with open('odpowiedzi9.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound3: {data['rating4']} | sound4: {data['rating5']}\n")

    # Przekieruj do nowej podstrony 9 po zakończeniu zapisu
    return redirect(url_for('page10'))
    
# Endpoint dla nowej podstrony 10
@app.route('/submit_new10', methods=['POST'])
def submit_new10():
    data = request.form

    with open('odpowiedzi10.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound3: {data['rating4']} | sound5: {data['rating5']}\n")

    # Przekieruj do nowej podstrony 10 po zakończeniu zapisu
    return redirect(url_for('page11'))
    
# Endpoint dla nowej podstrony 11
@app.route('/submit_new11', methods=['POST'])
def submit_new11():
    data = request.form

    with open('odpowiedzi11.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound3: {data['rating4']} | sound6: {data['rating5']}\n")

    # Przekieruj do nowej podstrony 11 po zakończeniu zapisu
    return redirect(url_for('page12'))

# Endpoint dla nowej podstrony 12
@app.route('/submit_new12', methods=['POST'])
def submit_new12():
    data = request.form

    with open('odpowiedzi12.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound4: {data['rating4']} | sound5: {data['rating5']}\n")

    # Przekieruj do nowej podstrony 12 po zakończeniu zapisu
    return redirect(url_for('page13'))
    
# Endpoint dla nowej podstrony 13
@app.route('/submit_new13', methods=['POST'])
def submit_new13():
    data = request.form

    with open('odpowiedzi13.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound4: {data['rating4']} | sound6: {data['rating5']}\n")

    # Przekieruj do nowej podstrony 13 po zakończeniu zapisu
    return redirect(url_for('page14'))
    
# Endpoint dla nowej podstrony 14
@app.route('/submit_new14', methods=['POST'])
def submit_new14():
    data = request.form

    with open('odpowiedzi14.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound5: {data['rating4']} | sound6: {data['rating5']}\n")

    # Przekieruj do nowej podstrony 14 po zakończeniu zapisu
    return redirect(url_for('page15'))
    
# Endpoint dla nowej podstrony 15
@app.route('/submit_new15', methods=['POST'])
def submit_new15():
    data = request.form

    with open('odpowiedzi15.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound1: {data['rating1']} | sound2: {data['rating2']} | soundotoczenia: {data['rating3']}\n")

    # Przekieruj do nowej podstrony 15 po zakończeniu zapisu
    return redirect(url_for('page16'))
    
# Endpoint dla nowej podstrony 16
@app.route('/submit_new16', methods=['POST'])
def submit_new16():
    data = request.form

    with open('odpowiedzi16.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound1: {data['rating1']} | sound3: {data['rating2']} | soundotoczenia: {data['rating3']}\n")

    # Przekieruj do nowej podstrony 16 po zakończeniu zapisu
    return redirect(url_for('page17'))
    
# Endpoint dla nowej podstrony 17
@app.route('/submit_new17', methods=['POST'])
def submit_new17():
    data = request.form

    with open('odpowiedzi17.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound1: {data['rating1']} | sound4: {data['rating2']} | soundotoczenia: {data['rating3']}\n")

    # Przekieruj do nowej podstrony 17 po zakończeniu zapisu
    return redirect(url_for('page18'))
    
# Endpoint dla nowej podstrony 18
@app.route('/submit_new18', methods=['POST'])
def submit_new18():
    data = request.form

    with open('odpowiedzi18.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound1: {data['rating1']} | sound5: {data['rating2']} | soundotoczenia: {data['rating3']}\n")

    # Przekieruj do nowej podstrony 18 po zakończeniu zapisu
    return redirect(url_for('page19'))
    
# Endpoint dla nowej podstrony 19
@app.route('/submit_new19', methods=['POST'])
def submit_new19():
    data = request.form

    with open('odpowiedzi19.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound1: {data['rating1']} | sound6: {data['rating2']} | soundotoczenia: {data['rating3']}\n")

    # Przekieruj do nowej podstrony 19 po zakończeniu zapisu
    return redirect(url_for('page20'))
    
# Endpoint dla nowej podstrony 20
@app.route('/submit_new20', methods=['POST'])
def submit_new20():
    data = request.form

    with open('odpowiedzi20.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound2: {data['rating1']} | sound3: {data['rating2']} | soundotoczenia: {data['rating3']}\n")

    # Przekieruj do nowej podstrony 20 po zakończeniu zapisu
    return redirect(url_for('page21'))
    
# Endpoint dla nowej podstrony 21
@app.route('/submit_new21', methods=['POST'])
def submit_new21():
    data = request.form

    with open('odpowiedzi21.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound2: {data['rating1']} | sound4: {data['rating2']} | soundotoczenia: {data['rating3']}\n")

    # Przekieruj do nowej podstrony 21 po zakończeniu zapisu
    return redirect(url_for('page22'))
    
# Endpoint dla nowej podstrony 22
@app.route('/submit_new22', methods=['POST'])
def submit_new22():
    data = request.form

    with open('odpowiedzi22.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound2: {data['rating1']} | sound5: {data['rating2']} | soundotoczenia: {data['rating3']}\n")

    # Przekieruj do nowej podstrony 22 po zakończeniu zapisu
    return redirect(url_for('page23'))
    
# Endpoint dla nowej podstrony 23
@app.route('/submit_new23', methods=['POST'])
def submit_new23():
    data = request.form

    with open('odpowiedzi23.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound2: {data['rating1']} | sound6: {data['rating2']} | soundotoczenia: {data['rating3']}\n")

    # Przekieruj do nowej podstrony 23 po zakończeniu zapisu
    return redirect(url_for('page24'))
    
# Endpoint dla nowej podstrony 24
@app.route('/submit_new24', methods=['POST'])
def submit_new24():
    data = request.form

    with open('odpowiedzi24.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound3: {data['rating1']} | sound4: {data['rating2']} | soundotoczenia: {data['rating3']}\n")

    # Przekieruj do nowej podstrony 24 po zakończeniu zapisu
    return redirect(url_for('page25'))
    
# Endpoint dla nowej podstrony 25
@app.route('/submit_new25', methods=['POST'])
def submit_new25():
    data = request.form

    with open('odpowiedzi25.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound3: {data['rating1']} | sound5: {data['rating2']} | soundotoczenia: {data['rating3']}\n")

    # Przekieruj do nowej podstrony 25 po zakończeniu zapisu
    return redirect(url_for('page26'))
    
# Endpoint dla nowej podstrony 26
@app.route('/submit_new26', methods=['POST'])
def submit_new26():
    data = request.form

    with open('odpowiedzi26.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound3: {data['rating1']} | sound6: {data['rating2']} | soundotoczenia: {data['rating3']}\n")

    # Przekieruj do nowej podstrony 26 po zakończeniu zapisu
    return redirect(url_for('page27'))
    
# Endpoint dla nowej podstrony 27
@app.route('/submit_new27', methods=['POST'])
def submit_new27():
    data = request.form

    with open('odpowiedzi27.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound4: {data['rating1']} | sound5: {data['rating2']} | soundotoczenia: {data['rating3']}\n")

    # Przekieruj do nowej podstrony 27 po zakończeniu zapisu
    return redirect(url_for('page28'))
    
# Endpoint dla nowej podstrony 28
@app.route('/submit_new28', methods=['POST'])
def submit_new28():
    data = request.form

    with open('odpowiedzi28.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound4: {data['rating1']} | sound6: {data['rating2']} | soundotoczenia: {data['rating3']}\n")

    # Przekieruj do nowej podstrony 28 po zakończeniu zapisu
    return redirect(url_for('page29'))
    
# Endpoint dla nowej podstrony 29
@app.route('/submit_new29', methods=['POST'])
def submit_new29():
    data = request.form

    with open('odpowiedzi29.txt', 'a') as file:
        file.write(f"Ocena: {data['rating']} | Pyt1: {data['pyt1']} | Pyt2: {data['pyt2']} | Pyt3: {data['pyt3']} | Pyt4: {data['pyt4']} | Pyt5: {data['pyt5']} | sound5: {data['rating1']} | sound6: {data['rating2']} | soundotoczenia: {data['rating3']}\n")

    # Przekieruj do strony głównej po zakończeniu zapisu
    return 'Dane zapisane poprawnie. Dziękujemy za udział w badaniu'
    
if __name__ == '__main__':
    app.run(debug=True)
