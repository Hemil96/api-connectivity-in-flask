# Import libraries
from flask import Flask, request, render_template, redirect
import api
import json

app = Flask(__name__)

# Routing
@app.route('/', methods=['POST', 'GET'])
def hello_world():

    if request.method == 'GET': #handling GET request
        return render_template('forms/basic_form.html')
        
    elif request.method == 'POST': #handling POST request
        api_res = api.coin(request.form['coin_name']) #fetching API response 
        print api_res # Tesing perpose [CLI]

        #Checking for keyerror/coin_name
        if api_res == "n/a":
            return render_template('forms/404.html')

        else:
            kwargs = {
                'f_name' : api_res["name"],
                'btc_rate' : api_res["btc"],
                'usd_rate' : api_res["usd"],
                'rank' : api_res["rank"],
                'ticker' : api_res["ticker"]
            }
            return render_template('forms/basic_form_result.html', **kwargs)
            # return redirect("/detail/"+request.form['coin_name'], code=302) #redirecting to other url




# @app.route('/detail/<coin_name>')
# def coinroute(coin_name):
#     api_res = api.coin(coin_name) #fetching API response 
#     print api_res # Tesing perpose [CLI]
#     kwargs = {
#         'f_name' : api_res["name"],
#         'btc_rate' : api_res["btc"],
#         'usd_rate' : api_res["usd"],
#         'rank' : api_res["rank"],
#         'ticker' : api_res["ticker"]
#     }
#     return render_template('forms/basic_form_result.html', **kwargs)