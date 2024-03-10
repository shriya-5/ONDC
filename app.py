from flask import Flask, render_template, request
import pandas as pd
from io import StringIO

app = Flask(__name__)

# Dummy DataFrame for illustration
dummy_df = pd.DataFrame({
    'Pincode': ['12345', '67890', '98765'],
    'Location': ['City A', 'City B', 'City C']
})

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']

        if uploaded_file:
            csv_data = uploaded_file.read().decode('utf-8')
            df = pd.read_csv(StringIO(csv_data))
            table_html = df.to_html(classes='table table-striped')
            return render_template('index.html', table_html=table_html)

    return render_template('index.html', table_html=None)

@app.route('/search_pincode', methods=['POST'])
def search_pincode():
    pincode_to_search = request.form.get('pincode')

    # Add your logic to check if the pincode is present or not
    # For example, you can use a predefined DataFrame or a database
    if pincode_to_search in dummy_df['Pincode'].values:
        result = 'found'
    else:
        result = ''

    return render_template('status.html', result=result)

if __name__ == '__main__':
    app.run(debug=Truefrom flask import Flask, render_template, request
import pandas as pd
from io import StringIO

app = Flask(__name__)

# Dummy DataFrame for illustration
dummy_df = pd.DataFrame({
    'Pincode': ['12345', '67890', '98765'],
    'Location': ['City A', 'City B', 'City C']
})

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']

        if uploaded_file:
            csv_data = uploaded_file.read().decode('utf-8')
            df = pd.read_csv(StringIO(csv_data))
            table_html = df.to_html(classes='table table-striped')
            return render_template('index.html', table_html=table_html)

    return render_template('index.html', table_html=None)

@app.route('/search_pincode', methods=['POST'])
def search_pincode():
    pincode_to_search = request.form.get('pincode')

    # Add your logic to check if the pincode is present or not
    # For example, you can use a predefined DataFrame or a database
    if pincode_to_search in dummy_df['Pincode'].values:
        result = 'found'
    else:
        result = ''

    return render_template('status.html', result=result)

if __name__ == '__main__':
    app.run(debug=Truefrom flask import Flask, render_template, request
import pandas as pd
from io import StringIO

app = Flask(__name__)

# Dummy DataFrame for illustration
dummy_df = pd.DataFrame({
    'Pincode': ['12345', '67890', '98765'],
    'Location': ['City A', 'City B', 'City C']
})

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']

        if uploaded_file:
            csv_data = uploaded_file.read().decode('utf-8')
            df = pd.read_csv(StringIO(csv_data))
            table_html = df.to_html(classes='table table-striped')
            return render_template('index.html', table_html=table_html)

    return render_template('index.html', table_html=None)

@app.route('/search_pincode', methods=['POST'])
def search_pincode():
    pincode_to_search = request.form.get('pincode')

    # Add your logic to check if the pincode is present or not
    # For example, you can use a predefined DataFrame or a database
    if pincode_to_search in dummy_df['Pincode'].values:
        result = 'found'
    else:
        result = ''

    return render_template('status.html', result=result)

if __name__ == '__main__':
    app.run(debug=True,port=8000)
