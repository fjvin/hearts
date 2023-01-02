from flask import Flask, jsonify, request

app = Flask(__name__)

# 1.Create a REST API using FLASK and insert a new heart record to a JSON file. 
# The heart rate information is composed of heart_id, date, and heart_rate.  (2 points)
heartsJSON = [

    {
        "heart_id" : 0,
        "date" : "02-01-2023",
        "heart_rate" : 70
    },

    {
        "heart_id" : 1,
        "date" : "02-01-2023",
        "heart_rate" : 73
    }

]

# 2. Create a REST API using FLASK to read heart information from a JSON file. 
# The heart rate information is composed of heart_id, date, and heart_rate. (2 points)
@app.route('/hearts', methods=['GET'])
def getAllHearts():
    return jsonify(heartsJSON)

# 3. Create a REST API using FLASK to read the heart information of a specific heart_id from a JSON file. 
# The heart rate information is composed of heart_id, date, and heart_rate. (2 points)
@app.route('/hearts/<int:index>', methods=['GET'])
def getHeartById(index):
    return jsonify(heartsJSON[index])

# 4. Create a REST API using FLASK to update a heart record of a specific heart_id. 
# The heart rate information is composed of heart_id, date, and heart_rate.  (2 points)
@app.route('/hearts/<int:index>', methods=['PUT'])
def updateHeart(index):
    heart = request.get_json()
    # print(hearts)

    if 'heart_rate' in heart.keys():
        heartsJSON[index]['heart_rate'] = heart['heart_rate']
        return f'heart_id: {index} updated', 200
    
    if 'date' in heart.keys():
        heartsJSON[index]['date'] = heart['date']
        return f'heart_id: {index} updated', 200

    return f'heart_id: {index} failed to update', 500


# 5. Create a REST API using FLASK to delete a heart record of a specific heart_id. 
# The heart rate information is composed of heart_id, date, and heart_rate.  (2 points).
@app.route('/hearts/<int:index>', methods=['DELETE'])
def deleteHeart(index):
    heartsJSON.pop(index)
    return f'heart_id: {index} deleted', 200

if __name__ == '__main__':

    app.run()