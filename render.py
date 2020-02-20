from flask import Flask, render_template


entireDataset = {
    'sneakerData' : {'NY':'Yeezys(from entireDataset)',
                    'NJ':'Jersey Shoes'},
    'incomeData' : {'NY': 50000,
                    'NJ':40000}
}

app = Flask(__name__)

@app.route('/')
def project():
   return render_template("index.html",
   data = entireDataset)

@app.route('/map')
def map():
    return render_template("Project3.html",
    data = entireDataset)

if __name__ == "__main__": 
    app.run(debug = True)