from flask import Flask, jsonify
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "secrectkey123"



def jsonConverter():
	os.system("./PTS_B_traffic_script3.py")
	file = open("mapInfo.txt", "r")
	data = file.read().split("\n")
	data = data[:len(data)-1]
	list_dic = {}
	k = 1
	for i in data:
#		print(i)
		d = i.split(",")
		list_dic["set"+str(k)] =  {"trffic_level" : d[0], "traffic_motion" : d[1], "temperature" : d[2][:-1]}
		k+=1
	file.close()
	return list_dic



@app.route("/")
def home():
#	data = jsonConverter()
    return jsonify({'Message': jsonConverter()})


if __name__ == "__main__":
    app.run(host="192.168.1.13", port=8080, debug=True)

# this link helped : https://stackoverflow.com/questions/49571099/certbot-renew-nginx-error-open-run-nginx-pid-failed-2-no-such-file-or
