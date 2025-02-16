from flask import Flask, render_template, request, jsonify
import ipl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/teams')
def all_teams():
    return jsonify(ipl.all_teams())

@app.route('/api/teamvteam')
def teamVteamAPI():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    if not team1 or not team2:
        return jsonify({'error': 'Both team1 and team2 must be provided'}), 400

    response = ipl.teamVteamAPI(team1, team2)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
