from multiprocessing import Process
import main  # this is where your Discord bot runs
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot and port are running!"

# Start the bot in a separate process
def start_bot():
    main.run()  # this must be your Discord bot starter

Process(target=start_bot).start()