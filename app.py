from flask import Flask, render_template, request, redirect, url_for, send_file
import pandas as pd
import os
import io
import random

# Import custom modules
from modules.linde_mh_fun_facts import linde_mh_facts
from modules.gpm_utils import get_gpm

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        gpm_mode = request.form.get('gpm_mode', 'avg GPM')
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            df = pd.read_excel(filepath)

            # Apply GPM logic per category
            df['GPM Used'] = df['Category'].apply(lambda x: get_gpm(x, gpm_mode))
            df['Dynamic Price'] = df['Dynamic Cost'] * (1 + df['GPM Used'] / 100)
            df['GPM Calc'] = round(((df['Dynamic Price'] - df['Dynamic Cost']) / df['Dynamic Price']) * 100, 2)

            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False)
            output.seek(0)

            return send_file(output, as_attachment=True, download_name='updated_file.xlsx')

    fun_fact = random.choice(linde_mh_facts)
    return render_template('index.html', fun_fact=fun_fact)

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)

