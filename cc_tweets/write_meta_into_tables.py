import boto3
import json

def gen_url(user_id, hour, category):
    return "https://s3.amazonaws.com/cc-project-s3/{0}/{1}_{2}.mp3".format(user_id, hour, category)


def get_audio_url(user_id):
	category = ["summary", "science", "business", "sport", "world"]
	dic = {}
	for cat in category:
		tmp_list = []
		for t in range(0, 24):
			next = t-1
			if next == -1:
				next = 23
			tmp_dic = {'time':t, 'url':gen_url(user_id, t, cat), 'next_url':gen_url(user_id, next, cat)}
			tmp_list.append(tmp_dic)
		dic[cat] = tmp_list
	return dic
	
	# for i in range(0, 24):
	# 	next = i - 1
	# 	if next == -1 :
	# 		next = 23
	# 	tmp = {}
	# 	for cat in category:
	# 		tmp[cat] = {
	# 			'url':gen_url(user_id, i, cat),
	# 			'next':str(next)
	# 		}
	# 	dic[str(i)] = tmp
	#
	# return dic

# dump meta json into dynamodb
dynamodb = boto3.resource('dynamodb')
meta_table = dynamodb.Table('META')
audio_table = dynamodb.Table('AUDIO')

with open('./data/meta.json','r') as json_file:
	meta = json.load(json_file)

for each in meta:
	meta_table.put_item(
		Item = each
	)
	print(each['user_id'] + ' is created!')

# create keys in AUDIO TABLE
res = meta_table.scan(ProjectionExpression="user_id")
user_list = [dic['user_id'] for dic in res['Items']]

for usr in user_list:
	audio_table.put_item(
		Item = {
			'user_id':usr,
			'category':get_audio_url(usr)
		}
	)

# create s3 folders
s3 = boto3.client('s3')
res = meta_table.scan(ProjectionExpression="user_id")
user_list = [dic['user_id'] for dic in res['Items']]

for usr in user_list:
	s3.put_object(Bucket='cc-project-s3', Key=usr + "/")
