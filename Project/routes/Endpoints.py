from flask import render_template, request
from Project import app, data
from Project import jupyter_import as jp
from IPython.display import HTML
from Project import functions as fn

@app.route("/")
def Home():
    name = 'Stock Market Project'
    author = 'Iskander Sergazin'
    return render_template('home.html', name=name, author=author)

@app.route("/introduction")
def Intro():
    corr = HTML(jp.corr_intro.to_html(classes='table table-striped'))
    return render_template('introduction.html',corr_intro = corr)
@app.route("/task_1")
def Task1():
    table = HTML(jp.task1_table.to_html(classes='table table-striped'))
    return render_template('task1.html', table = table)
@app.route("/task_2")
def Task2():
    filtered_df = HTML(jp.filtered_dtf1.to_html(classes='table table-striped'))
    return render_template('task2.html', filtered_df=filtered_df)

@app.route("/task_3")
def Task3():
    corr3 = HTML(jp.corr_3.to_html(classes='table table-striped'))
    dq3 = HTML(jp.dq3.to_html(classes='table table-striped'))
    corr4 = HTML(jp.corr4.to_html(classes='table table-striped'))
    return render_template('task3.html', corr3 = corr3, dq3 = dq3, corr4 = corr4)
@app.route("/task_4")
def Task4():
    return render_template('task4.html')

@app.route("/task_6")
def Task6():
    filtereddf_res = HTML(jp.filtered_df_RES.to_html(classes='table table-striped'))
    sample = HTML(jp.sample.to_html(classes='table table-striped'))
    resu = HTML(jp.resu.to_html(classes='table table-striped'))
    PC = jp.PC
    PCSP500 = jp.PCSP500
    PT = jp.PT
    resu2 = HTML(jp.resu2.to_html(classes='table table-striped'))
    PC2 = round(jp.PC2)
    finish = round(jp.finish)
    return render_template('task6*.html', filter = filtereddf_res, sample = sample, resu=resu, PC=PC, PCSP500 = PCSP500, PT = PT, resu2 = resu2, finish = finish, PC2= PC2)

@app.route("/data_intro")
def Table():
    data = HTML(jp.dp_intro.to_html(classes='table table-striped'))
    return render_template('data_intro.html', data=data)

@app.route('/task_7')
def task7():
    return render_template('task7.html')

@app.route('/task_7', methods=['POST'])
def my_form_post():
    PERSTD1 = int(request.form['PERSTD'])
    BVSTD1  = int(request.form['BVSTD'])
    x = int(request.form['x'])
    return fn.task7(BVSTD1, PERSTD1).sample(x).to_html()

