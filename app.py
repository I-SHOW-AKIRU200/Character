from flask import Flask, jsonify

app = Flask(__name__)

# Full character data
characters = [
    {"Character Name": "Olivia", "Skill id": "106", "Png Image": "https://photos.app.goo.gl/jMHkTTpQFaFtyY1Q8"},
    {"Character Name": "Kelly", "Skill id": "206", "Png Image": "https://photos.app.goo.gl/KZDr7xSdJTe3MvnA9"},
    {"Character Name": "Ford", "Skill id": "306", "Png Image": "https://photos.app.goo.gl/96c9oXuBy5yviE9Q9"},
    {"Character Name": "Andrew", "Skill id": "406", "Png Image": "https://photos.app.goo.gl/5gd7Fr6wQxktLtDi9"},
    {"Character Name": "Nikita", "Skill id": "506", "Png Image": "https://photos.app.goo.gl/sfbPTvaAbocZFXLT8"},
    {"Character Name": "Misha", "Skill id": "606", "Png Image": "https://photos.app.goo.gl/ov2nwx2s3G7wL7ecA"},
    {"Character Name": "Maxim", "Skill id": "706", "Png Image": "https://photos.app.goo.gl/WMFptSZXU3hHAy2K7"},
    {"Character Name": "Kla", "Skill id": "806", "Png Image": "https://photos.app.goo.gl/44DqQMiQFBabDbgX7"},
    {"Character Name": "Paloma", "Skill id": "906", "Png Image": "https://photos.app.goo.gl/YdfwnMEUDTBPpr8J6"},
    {"Character Name": "Miguel", "Skill id": "1006", "Png Image": "https://photos.app.goo.gl/PfyuCTNqZuEm3itdA"},
    {"Character Name": "Caroline", "Skill id": "1106", "Png Image": "https://photos.app.goo.gl/XuYLNeZr7GRW4v9N6"},
    {"Character Name": "Wukong", "Skill id": "1206", "Png Image": "https://photos.app.goo.gl/hYhC1MuZ3wVPtToL9"},
    {"Character Name": "Antonio", "Skill id": "1306", "Png Image": "https://photos.app.goo.gl/1DvoNxSCmnDmBxwT9"},
    {"Character Name": "Moco", "Skill id": "1406", "Png Image": "https://photos.app.goo.gl/dEANgb8eLcFvULsE7"},
    {"Character Name": "Hayato", "Skill id": "1506", "Png Image": "https://photos.app.goo.gl/hLAC5YRZDbYxxb46A"},
    {"Character Name": "Laura", "Skill id": "1706", "Png Image": "https://photos.app.goo.gl/nBEgZZCgdjsy9uLHA"},
    {"Character Name": "Rafael", "Skill id": "1806", "Png Image": "https://photos.app.goo.gl/B9GW5fVyrSvmoHKc9"},
    {"Character Name": "A124", "Skill id": "1906", "Png Image": "https://photos.app.goo.gl/2s6EVDocMjUTKhEh8"},
    {"Character Name": "Joseph", "Skill id": "2006", "Png Image": "https://photos.app.goo.gl/euWttFjDFebJtQrf6"},
    {"Character Name": "Shani", "Skill id": "2106", "Png Image": "https://photos.app.goo.gl/KkxKraL5ZBcHj16U8"},
    {"Character Name": "Alok", "Skill id": "2206", "Png Image": "https://photos.app.goo.gl/hEyq4bPqsNuekab6A"},
    {"Character Name": "Alvaro", "Skill id": "2306", "Png Image": "https://photos.app.goo.gl/UhU2D8FhgdqriZty6"},
    {"Character Name": "Notora", "Skill id": "2406", "Png Image": "https://photos.app.goo.gl/RQNwtTN38uCJRiwF8"},
    {"Character Name": "Kelly The Swift", "Skill id": "2506", "Png Image": "https://photos.app.goo.gl/enRnvppzeJ973v2S6"},
    {"Character Name": "Steffie", "Skill id": "2606", "Png Image": "https://photos.app.goo.gl/S31VTS3McP3wyDJh7"},
    {"Character Name": "Jota", "Skill id": "2706", "Png Image": "https://photos.app.goo.gl/3BtPGNskVM6m8mPg9"},
    {"Character Name": "Kapella", "Skill id": "2806", "Png Image": "https://photos.app.goo.gl/3opsBntzsCgt4hK76"},
    {"Character Name": "Luqueta", "Skill id": "2906", "Png Image": "https://photos.app.goo.gl/kVGWhJJABA84dunR8"},
    {"Character Name": "Wolfrahh", "Skill id": "3006", "Png Image": "https://photos.app.goo.gl/wdB4U46ZyKVbuyu67"},
    {"Character Name": "Clu", "Skill id": "3106", "Png Image": "https://photos.app.goo.gl/UKdjebQ2YMcLJi6p7"},
    {"Character Name": "Elite Hayato", "Skill id": "3206", "Png Image": "https://photos.app.goo.gl/pToyN86g5ho475FS9"},
    {"Character Name": "Jai", "Skill id": "3306", "Png Image": "https://photos.app.goo.gl/ga4yahFnw99Kmg138"},
    {"Character Name": "K", "Skill id": "3406", "Png Image": "https://photos.app.goo.gl/FbZg412kXULrrpmV9"},
    {"Character Name": "Dasha", "Skill id": "3506", "Png Image": "https://photos.app.goo.gl/hepkBixqcSucJKi9A"},
    {"Character Name": "Chrono", "Skill id": "3806", "Png Image": "https://photos.app.goo.gl/3W8p5kwT4SaGK8xw6"},
    {"Character Name": "Skyler", "Skill id": "4006", "Png Image": "https://photos.app.goo.gl/dpk13Asrw4WveSBs6"},
    {"Character Name": "Shirou", "Skill id": "4106", "Png Image": "https://photos.app.goo.gl/D1kAWb1KTv9sN6rYA"},
    {"Character Name": "Andrew the Fierce", "Skill id": "4206", "Png Image": "https://photos.app.goo.gl/yTNbXiEWvmEyqZHGA"},
    {"Character Name": "Maro", "Skill id": "4306", "Png Image": "https://photos.app.goo.gl/2u5FVBXoTf2PAHMR8"},
    {"Character Name": "Xayne", "Skill id": "4406", "Png Image": "https://photos.app.goo.gl/DEWsqm7aSPSp3UVe7"},
    {"Character Name": "D-Bee", "Skill id": "4506", "Png Image": "https://photos.app.goo.gl/PDfu4pLk9Wk8EHeTA"},
    {"Character Name": "Thiva", "Skill id": "4606", "Png Image": "https://photos.app.goo.gl/JkGLTNt9hUXxGpSW9"},
    {"Character Name": "Dimitri", "Skill id": "4706", "Png Image": "https://photos.app.goo.gl/g5njZvErKBGuPu2x5"},
    {"Character Name": "Moco Enigma", "Skill id": "4806", "Png Image": "https://photos.app.goo.gl/ysHLmE5Je8ADkXPG6"},
    {"Character Name": "Leon", "Skill id": "4906", "Png Image": "https://photos.app.goo.gl/SYgHNEu1QVjgAnku8"},
    {"Character Name": "Otho", "Skill id": "5006", "Png Image": "https://photos.app.goo.gl/WhtsAY7Vda3MTBH96"},
    {"Character Name": "Nairi", "Skill id": "5206", "Png Image": "https://photos.app.goo.gl/6UXNGAwq4hvDVSiw7"},
    {"Character Name": "Luna", "Skill id": "5306", "Png Image": "https://photos.app.goo.gl/gk6eUf8HF3xqJmG3A"},
    {"Character Name": "Kenta", "Skill id": "5406", "Png Image": "https://photos.app.goo.gl/Rw3ZiKEJtimAm6vv5"},
    {"Character Name": "Homer", "Skill id": "5506", "Png Image": "https://photos.app.goo.gl/m7t7BS6WTp4Mqp6e7"},
    {"Character Name": "Iris", "Skill id": "5606", "Png Image": "https://photos.app.goo.gl/tP89GY8ZDZ9mydCKA"},
    {"Character Name": "J.Biebs", "Skill id": "5706", "Png Image": "https://photos.app.goo.gl/3Wh7LvCv4L8KttX38"},
    {"Character Name": "Tatsuya", "Skill id": "5806", "Png Image": "https://photos.app.goo.gl/HYRUXXWpbBvX8cVy5"},
    {"Character Name": "Santino", "Skill id": "6006", "Png Image": "https://photos.app.goo.gl/GueTsJ6BuxqLLMedA"},
    {"Character Name": "Orion", "Skill id": "6206", "Png Image": "https://photos.app.goo.gl/u4jWgZYebTBYQ7qz7"},
    {"Character Name": "Alvaro Rageblast", "Skill id": "6306", "Png Image": "https://photos.app.goo.gl/jrzHNyAzycx566Xj6"},
    {"Character Name": "Sonia", "Skill id": "6506", "Png Image": "https://photos.app.goo.gl/zaBBhbwonuArJSsr8"},
    {"Character Name": "Suzy", "Skill id": "6606", "Png Image": "https://photos.app.goo.gl/UsDws8RBvbvqQk677"},
    {"Character Name": "Ignis", "Skill id": "6706", "Png Image": "https://photos.app.goo.gl/2Eopgommm9ZKmrBQ9"},
    {"Character Name": "Awakened Alok", "Skill id": "22016", "Png Image": "https://photos.app.goo.gl/SB6WuyKLn5zhsYuR8"},
    {"Character Name": "Kairos", "Skill id": "6906", "Png Image": "https://photos.app.goo.gl/9Gm1hPW732rvSuYSA"},
    {"Character Name": "Lila", "Skill id": "7106", "Png Image": "https://photos.app.goo.gl/HGS6cjY71LkcCjph9"},
    {"Character Name": "Kassie", "Skill id": "7006", "Png Image": "https://photos.app.goo.gl/Jx2LU7F7YsZNB1gv6"},
    {"Character Name": "Ryden", "Skill id": "6806", "Png Image": "https://photos.app.goo.gl/xC4VFUzRzGVHT44fA"},
    {"Character Name": "Koda", "Skill id": "7206", "Png Image": "https://photos.app.goo.gl/spwL1RKaUSoPa4aa7"}
]

@app.route('/Character_name/Id=<identifier>', methods=['GET'])
def get_character(identifier):
    # Search by either Character Name or Skill ID
    for character in characters:
        if character["Character Name"].lower() == identifier.lower() or character["Skill id"] == identifier:
            return jsonify({
                "Character Name": character["Character Name"],
                "Skill id": character["Skill id"],
                "Png Image": character["Png Image"]
            })
    
    return jsonify({"error": "Character not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
