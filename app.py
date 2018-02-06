from flask import Flask, jsonify
import requests
import json


app = Flask(__name__)


@app.route('/')
def sync():
	url = 'https://us9.api.mailchimp.com/3.0/lists/1a2d7ebf82/members'
	headers = {'Authorization': 'apikey 0bb2c4545c0e7409ace500b1b8257ea3-us9'}
	r = requests.get(url, headers=headers)

	if r.status_code == 200:
		members = r.json()['members']
		contacts = [{'id':member['id'],'firstname':member['merge_fields']['FNAME'],'lastname':
			member['merge_fields']['LNAME'],'email':member['email_address']} for member in members]
		
		payload = json.dumps(contacts)
		post_header = {'Authorization':'a4f751ae-7fd7-4f38-9390-fbc6378658ed', 'Content_Type': 'application/json'}
		post_url = 'http://ec2-34-242-147-110.eu-west-1.compute.amazonaws.com:8080/record'

		upload = requests.post(post_url, data=payload, headers=post_header)
		return jsonify(status='{}'.format(upload.status_code))
	else:
		return jsonify(status='{}'.format(r.status_code))


if __name__ == '__main__':
	app.run()