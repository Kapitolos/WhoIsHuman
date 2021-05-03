from flask import Flask, redirect, url_for, render_template, request, flash
import requests
from bs4 import BeautifulSoup
import shutil
from PIL import Image
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc, resources_pb2, service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2, status_pb2
import json
import csv
import psycopg2
import random


app = Flask(__name__, static_url_path='/static')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

DB_host = '127.0.0.1'
DB_user = 'postgres'
DB_password = 'Redwings!'
DB_name= 'whoishuman'

def write_to_db(data):
    conn = psycopg2.connect(dbname=DB_name, user=DB_user, password=DB_password, host=DB_host)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    db_users = cur.fetchall()
    userid = (len(db_users))
    print(userid)
    username = data["username"]
    password = data["password"]
    fullname = data["fullname"]
    userage = data['age']
    userjob = data['occupation']
    cur.execute("""
    INSERT INTO users (username, password, fullname, userage, userjob, userid)
    VALUES (%s,%s,%s,%s,%s,%s);
    """,
    (username, password, fullname, userage, userjob, userid))
    conn.commit()
    cur.close()
    conn.close()
    return redirect("index")

def signinfunc(data):
    conn = psycopg2.connect(dbname=DB_name, user=DB_user, password=DB_password, host=DB_host)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    db_users = cur.fetchall()
    isin = False
    error = None
    for i in db_users:
        if data["username"] and data["password"] in i:
            # test=(json.dumps(i))
            # test2 = json.loads(test)
            # hero = Character(test2[5],test2[2],test2[3],test2[6],test2[7],test2[8],test2[9],test2[10],test2[11],test2[12],test2[13],test2[14],test2[15],test2[16])
            isin = True
        else:
            print("not found")
    if isin == False:
        error = 'Invalid credentials'
        flash('Not Found')
        return render_template("signin.html", error=error)
    else:
        flash('You were successfully logged in')
        return redirect('index')

@app.route("/register", methods=["POST", "GET"])
def register():
    error = None
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return write_to_db(data)
        # return render_template('register.html')
    else:
        # error = 'Invalid credentials'
        return render_template('register.html')

@app.route("/signin", methods=["POST", "GET"])
def signcheck():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return signinfunc(data)
    else:
        print("exit?")
        return render_template('signin.html')



@app.route('/guess', methods=["POST", "GET"])
def guess():
    guess = "You got it!"
    return render_template('guess.html', guess=guess)







@app.route('/')
def home():
    return render_template('loading.html')

#Clarafai all scope API key
# my_key = '55572434d01d483793322ceedcfbcbda'
facesource = 'https://thispersondoesnotexist.com/image'


channel = ClarifaiChannel.get_grpc_channel()


stub = service_pb2_grpc.V2Stub(ClarifaiChannel.get_grpc_channel())

# This is how you authenticate.
metadata = (( 'authorization', 'Key 55572434d01d483793322ceedcfbcbda'),)

requestc = service_pb2.PostModelOutputsRequest(
    # This is the model ID of a publicly available General model.
    model_id='aaa03c23b3724a16a56b629203edc62c',
    inputs=[
      resources_pb2.Input(data=resources_pb2.Data(image=resources_pb2.Image(url=f"{facesource}")))
    ])
response = stub.PostModelOutputs(requestc, metadata=metadata)
# print(response.outputs)

if response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Request failed, status code: " + str(response.status.code))


faceinfolist = []


def getfaces():
    for i in range(9):
        response2 = requests.get(facesource, stream=True)
        with open(f'./static/assets/images/img{i}.png', 'wb') as out_file:
            shutil.copyfileobj(response2.raw, out_file)
            requestc = service_pb2.PostModelOutputsRequest(
                # This is the model ID of a publicly available General model. You may use any other public or custom model ID.
                model_id='aaa03c23b3724a16a56b629203edc62c',
                inputs=[
                    resources_pb2.Input(data=resources_pb2.Data(image=resources_pb2.Image(url=f"{facesource}")))
                ])
            response = stub.PostModelOutputs(requestc, metadata=metadata)
        faceinfo = {}
        for concept in response.outputs[0].data.concepts:
            faceinfo[concept.name] = concept.value
            # faceinfolist[i].append(faceinfo)
                # print(faceinfo)
        del response2
        faceinfo['picture'] = f'./static/assets/images/img{i}.png'
        faceinfolist.append(faceinfo)
        print("face added")

# getfaces()


# print(faceinfolist[0])

def gender():
    for i in faceinfolist:
        if 'man' in i:
            if i['man'] or i['guy'] > .90:
                nameurlm = 'https://api.namefake.com/canadian/male/'
                fakename = requests.get(nameurlm)
                soup = BeautifulSoup(fakename.text, 'html.parser')
                fakenamepage = soup.prettify()
                parsename = json.loads(fakenamepage)
                facename = parsename["name"]
                print(facename)
                i['name'] = facename
            else:
                i['name'] = "I think it's Frank"

        elif 'woman' in i:
            if i['woman'] or ['girl'] > .90:
                nameurlf = 'https://api.namefake.com/canadian/female/'
                fakename = requests.get(nameurlf)
                soup = BeautifulSoup(fakename.text, 'html.parser')
                fakenamepage = soup.prettify()
                parsename = json.loads(fakenamepage)
                facename = parsename["name"]
                print(facename)
                i['name'] = facename
            else:
                i['name'] = "I can't remember...Sharon?"

        else:
            nameurltt = 'https://api.namefake.com/canadian/female/'
            fakename = requests.get(nameurltt)
            soup = BeautifulSoup(fakename.text, 'html.parser')
            fakenamepage = soup.prettify()
            parsename = json.loads(fakenamepage)
            facename = parsename["name"]
            print(facename)
            i['name'] = "Unknown Name"

def age():
    for i in faceinfolist:
        if 'young' in i:
            i['age'] = "Young"
        elif 'child' or 'adolescent' in i:
            i['age'] = "Young"
        elif 'preschool' in i:
            i['age'] = "Young"
        elif 'adult' in i:
            i['age'] = "Adult"
        else:
            i['age'] = "Senior"


def job():
    for i in faceinfolist:
        if 'musician' in i:
            i['job'] = "Musician"
        elif 'singer' in i:
            i['job'] = "Musician"
        elif 'rugby' in i:
            i['job'] = "Athlete"
        elif 'scholar' in i:
            i['job'] = "Teacher"
        elif 'elegant' in i:
            i['job'] = "Social Services"
        elif 'fashion' in i:
            i['job'] = "Entrepreneur"
        elif 'pretty' in i:
            i['job'] = "Performing Arts"
        elif 'young' in i:
            i['job'] = "Student"
        elif 'nature' in i:
            i['job'] = "Engineer"
        else:
            i['job'] = "Unemployed"

@app.route('/index', methods=["POST", "GET"])
def game():
    getfaces()
    job()
    age()
    gender()
    # humanface = f'./static/assets/images/human{random.randint(1, 35)}.jpg'
    humanface = f'./static/assets/images/human2.jpg'
    return render_template('index.html', faceinfolist=faceinfolist, humanface=humanface)

# for i in faceinfolist:
#     if 'man' in i:
#         if i['man'] > .90:
#             print('Over 90')
#
#         else:
#             print('Under 90')
#     else:
#         print('This things to do')









