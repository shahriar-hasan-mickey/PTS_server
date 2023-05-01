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
	dictionary = {}
	k = 1
	for i in data:
#	print(i)
		d = i.split(",")
		list_dic["trffic_level"] = d[0].encode("utf-8")
		list_dic["traffic_motion"] = d[1].encode("utf-8")
		list_dic["temperature"] = d[2].encode("utf-8")
		dictionary["set"+str(k)] = list_dic
		k+=1
#	list_dic = str(list_dic)
	print(list_dic)
	return dictionary



@app.route("/")
def home():
#	data = jsonConverter()
    return jsonify({'Message': jsonConverter()})


if __name__ == "__main__":
    app.run()

# this link helped : https://stackoverflow.com/questions/49571099/certbot-renew-nginx-error-open-run-nginx-pid-failed-2-no-such-file-or
