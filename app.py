from flask import Flask, request, jsonify
app = Flask(__name__)

def cut_string(str):
	new_str = ""
	for i in range(len(str)):
		if (i+1) % 3 == 0:
			print(str[i], "hello")
			new_str += str[i]
	return new_str

@app.route('/test', methods=["POST"])
def string_to_cut():
	data = request.json
	if data:
		new_str = cut_string(data['string_to_cut'])
		return jsonify({"return_string": new_str})
	return jsonify({"message": "Please enter a valid string"})