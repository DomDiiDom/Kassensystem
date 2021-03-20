import flask
import json

app = flask.Blueprint('Functions', __name__, template_folder='templates')

current_question = {}

@app.route("/functions/set/question", methods=["POST"])
def functionSetQuestion():
    global current_question

    id = flask.request.form["id"]
    print(f"ID: {id}")
    response = Web.sendRequest(Web.url, "/api/set/question", {"id": id})
    Web.currentQuestionID = id
    current_question = json.loads(response.text)
    Web.isAcceptingAnswers = True
    return ""

@app.route("/functions/reset/question", methods=["POST"])
def functionResetQuestion():
    Web.sendRequest(Web.url, "/api/reset/question", {"license": License.license, "id": License.id, "token": License.token})
    return ""

@app.route("/functions/set/category", methods=["POST"])
def functionSetCategory():
    category = flask.request.form["category"]
    game = flask.request.form["game"]
    Web.sendRequest(Web.url, "/api/set/category", {"category": category, "license": License.license, "id": License.id, "token": License.token, "game": game})
    return ""

@app.route("/functions/set/new", methods=["POST"])
def functionSetNewQuestion():
    print(flask.request.form)
    question = flask.request.form["question"]
    answer_1 = flask.request.form["answer_1"]
    answer_2 = flask.request.form["answer_2"]
    answer_3 = flask.request.form["answer_3"]
    answer_4 = flask.request.form["answer_4"]
    correct = flask.request.form["correct"]
    category = flask.request.form["category"]
    print("TEST")
    print(Web.categories)
    print(category)
    print(Web.categories.get(category, 0))
    Web.sendRequest(Web.url, "/api/set/new", {"category": Web.categories.get(category, 0), "license": License.license, "id": License.id, "token": License.token, "question": question, "answer_1": answer_1, "answer_2": answer_2, "answer_3": answer_3, "answer_4": answer_4, "correct": correct})

    return ""

@app.route("/functions/set/delete", methods=["POST"])
def functionDeleteNewQuestion():
    question = flask.request.form["id"]
    Web.sendRequest(Web.url, "/api/set/delete", {"license": License.license, "id": License.id, "token": License.token, "question": question})

    return ""

@app.route("/functions/set/release", methods=["POST"])
def functionRelease():
    global current_question
    _response = Web.sendRequest(Web.url, "/api/set/release", {"license": License.license, "id": License.id, "token": License.token})
    response = _response.text
    print(response)
    Web.currentQuestion = response

    for key, value in Web.currentPoll.items():
        if int(value) == int(current_question["correct"]):
            main.logger.info(f"User {key} is correct")
            main.data.addPollResultForUser(key, 1)

    Web.isAcceptingAnswers = False
    current_question = {}
    Web.currentPoll.clear()

    return ""

@app.route("/functions/set/deletecategory", methods=["POST"])
def functionDeleteCategory():
    category = flask.request.form["category"]
    Web.sendRequest(Web.url, "/api/delete/category", {"license": License.license, "id": License.id, "token": License.token, "category": category})

    return ""

@app.route("/functions/get/truckposition", methods=["POST"])
def loadTruckPosition():
    Web.isETSTargetSet = True
    if not Web.ets_target == flask.request.form["playerID"]:
        Registry.set_reg("quiz.onecommunity.ets_target", flask.request.form["playerID"])

    info = TruckyApp.getPlayerInfo(flask.request.form["playerID"])
    print("Info:")
    print(info)
    return info
