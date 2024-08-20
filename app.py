from flask import Flask, render_template, request, session, jsonify

# Vars
app = Flask(__name__)

app.secret_key = "AZERTY"
app.config["SESSION_TYPE"] = "filesystem"

global tasks

tasks = []


# Routes
@app.route("/", methods=["GET"])
def hello():
    return render_template("extend.html", tasks=tasks)


# API Endpoints

"""Task handling enpoint
On success, returns a Reponse with an HTTP 200 code
On failure, returns an HTTP 400 Response code, with the reason on the message element of the body

Returns:
    object: JSON response: {code: [code], message: [message]}
"""


@app.route("/api/task/add", methods=["POST"])
def add_task():
    code = 500
    message = "Internal Server Error"

    content = request.form["content"]
    if content and not any(task["content"] == content for task in tasks):
        tasks.append(
            {
                "id": len(tasks),
                "content": content,
            }
        )
        code = 200
        message = "Success"
    else:
        code = 400
        message = "Entry already exists"

    return jsonify({"code": code, "message": message})


@app.route("/api/task/delete/<int:id>", methods=["POST"])
def delete_task(id):
    code = 500
    message = "Internal Server Error"

    if id is not None:
        try:
            del tasks[int(id)]
            code = 200
            message = "Success"
        except Exception as e:
            code = 500
            message = f"Failed to delete task with exception {e}"
    else:
        code = 400
        message = "Task not found"

    return jsonify({"code": code, "message": message})
