from flask import Flask, jsonify

app = Flask(__name__)

# Full character data
characters = [
    {"Character Name": "Olivia", "Skill id": "106", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/202211/435b2230bb59c6a7f087d841e7dc8590.png"},
    {"Character Name": "Kelly", "Skill id": "206", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/202311/a80ef2744fa83dc119cc09249d70444e.png"},
    {"Character Name": "Ford", "Skill id": "306", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/202211/e4eba268be6b474381acc6c4b282f5ea.png"},
    {"Character Name": "Andrew", "Skill id": "406", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/564762d9a1137afaf2c9abb0ea8862b7.png"},
    {"Character Name": "Nikita", "Skill id": "506", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/93bac478d8b64e0a6b31fee8c75220d9.png"},
    {"Character Name": "Misha", "Skill id": "606", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/33110529f97da7fc1bf681e61a1de2bb.png"},
    {"Character Name": "Maxim", "Skill id": "706", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/59dc42433e877fa0cc3bb69b74dbf2c8.png"},
    {"Character Name": "Kla", "Skill id": "806", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/1655985bf74931458766921ee6bb6e0a.png"},
    {"Character Name": "Paloma", "Skill id": "906", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/93a87a41a13af14c2346379a0d917d36.png"},
    {"Character Name": "Miguel", "Skill id": "1006", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/041a8586fe9d5461a7f28510fb5786d0.png"},
    {"Character Name": "Caroline", "Skill id": "1106", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/aa43b9f99d6a367a5123dbae9f6cd5c6.png"},
    {"Character Name": "Wukong", "Skill id": "1206", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/20229/c0f1547f51f4c2b99e28ef4ec52db084.png"},
    {"Character Name": "Antonio", "Skill id": "1306", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/c87a2bcb4b4ab665908df11672aa191d.png"},
    {"Character Name": "Moco", "Skill id": "1406", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/769ceca68c62ec35cdbf90f1c0d7c73f.png"},
    {"Character Name": "Hayato", "Skill id": "1506", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/d8800f78f00e9831fc157a04aa3078aa.png"},
    {"Character Name": "Laura", "Skill id": "1706", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/a742beadf78c01fb9e05aabc51c9369e.png"},
    {"Character Name": "Rafael", "Skill id": "1806", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/738a885af3eb66c1415a0ac61bfd304b.png"},
    {"Character Name": "A124", "Skill id": "1906", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/ab1469c59a10c4669482e1ab625357dd.png"},
    {"Character Name": "Joseph", "Skill id": "2006", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/07d65d842e613a0cc22794f953c44be3.png"},
    {"Character Name": "Shani", "Skill id": "2106", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/20229/2a790a2ca70a797b5384a122ad7d8d10.png"},
    {"Character Name": "Alok", "Skill id": "2206", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/c62e709e3ad8387f5484bb12e1cc81a9.png"},
    {"Character Name": "Alvaro", "Skill id": "2306", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/d5c0af0ac8632385f2cdb0500874b2a5.png"},
    {"Character Name": "Notora", "Skill id": "2406", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/fab6aa1cb1c6ce92652a3f184d265b76.png"},
    {"Character Name": "Kelly The Swift", "Skill id": "2506", "Png Image": "https://i.postimg.cc/BnpRPsjv/Kelly-The-Swift.png"},
    {"Character Name": "Steffie", "Skill id": "2606", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/809499ee33234f1c72c6a3ab120e85dd.png"},
    {"Character Name": "Jota", "Skill id": "2706", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/20229/5ae1530683a65bdfd81f6f7f7552650c.png"},
    {"Character Name": "Kapella", "Skill id": "2806", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/9c6b10d2984125fbdd96fae9e0a84518.png"},
    {"Character Name": "Luqueta", "Skill id": "2906", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/20229/28b704e964e8057d7fc76e1a2cca7d26.png"},
    {"Character Name": "Wolfrahh", "Skill id": "3006", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/e4169a44d8a6e83549b3b7f8a7820c1e.png"},
    {"Character Name": "Clu", "Skill id": "3106", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/81def6541fb94bd20887bad6b5a725cf.png"},
    {"Character Name": "Elite Hayato", "Skill id": "3206", "Png Image": "https://i.postimg.cc/KzH9r8bZ/Hayato-Firebrand.png"},
    {"Character Name": "Jai", "Skill id": "3306", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/202412/077ccf77edb55d6b9d529e4afc1ae965.png"},
    {"Character Name": "K", "Skill id": "3406", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/cace792e96191c1623da45de2e52a589.png"},
    {"Character Name": "Dasha", "Skill id": "3506", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/8d2bc4db79fe889ab6541ae2dd7cd2cb.png"},
    {"Character Name": "Chrono", "Skill id": "3806", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/202412/6d5de642b070e208a38b037d8233df85.png"},
    {"Character Name": "Skyler", "Skill id": "4006", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/547dea01d82886891297443e8e9d270f.png"},
    {"Character Name": "Shirou", "Skill id": "4106", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/dbe25891f13c5752e84ad7daf57106cc.png"},
    {"Character Name": "Andrew the Fierce", "Skill id": "4206", "Png Image": "https://i.postimg.cc/ZK1Gzj1T/Andrew-The-Fierce.png"},
    {"Character Name": "Maro", "Skill id": "4306", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/8af9a328d62a330a76221b79670daf37.png"},
    {"Character Name": "Xayne", "Skill id": "4406", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20229/ea05dd27c4f4faf3267679d5f90cdaec.png"},
    {"Character Name": "D-Bee", "Skill id": "4506", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/f1a09717ed71e7302da8d4cc889d2e33.png"},
    {"Character Name": "Thiva", "Skill id": "4606", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/217c0184667efa92bcec0caa73af73b9.png"},
    {"Character Name": "Dimitri", "Skill id": "4706", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/024c98913571304db2cba9d257e7291a.png"},
    {"Character Name": "Moco Enigma", "Skill id": "4806", "Png Image": "https://i.postimg.cc/FznQS4Wc/Moco-Rebirth.png"},
    {"Character Name": "Leon", "Skill id": "4906", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/b79f47950001fb7f7130a6b3752b3446.png"},
    {"Character Name": "Otho", "Skill id": "5006", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/d0ea6553e85abbf0a8b718e29900b7f5.png"},
    {"Character Name": "Nairi", "Skill id": "5206", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/e21eb41a3705ff817156dd5758157274.png"},
    {"Character Name": "Luna", "Skill id": "5306", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/202211/9d03033ed89089d1f25c6be01817ebca.png"},
    {"Character Name": "Kenta", "Skill id": "5406", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/f867281184a63b0ac1bd9cc03a484bce.png"},
    {"Character Name": "Homer", "Skill id": "5506", "Png Image": "https://freefiremobile-a.akamaihd.net/common/web_event/official2.ff.garena.all/img/20228/26d226fa08410cc418959e3cc30095c7.png"},
    {"Character Name": "Iris", "Skill id": "5606", "Png Image": "https://photos.app.goo.gl/tP89GY8ZDZ9mydCKA"},
    {"Character Name": "J.Biebs", "Skill id": "5706", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/202412/d3eb3130503cd726a5b7bce881d46c93.png"},
    {"Character Name": "Tatsuya", "Skill id": "5806", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/20229/e37e48adf72a2c014c2bfa8ed483f5b5.png"},
    {"Character Name": "Santino", "Skill id": "6006", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/20233/a3810f993d32077e88c5226625bb55a9.png"},
    {"Character Name": "Orion", "Skill id": "6206", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/20238/4f4fc6c6d43fc3bb5ef4617f9f5340f7.png"},
    {"Character Name": "Alvaro Rageblast", "Skill id": "6306", "Png Image": "https://i.postimg.cc/k5k6x0H0/Alvaro-Rageblast.png"},
    {"Character Name": "Sonia", "Skill id": "6506", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/20238/8f978bdbe46d3d2366b82713082d6683.png"},
    {"Character Name": "Suzy", "Skill id": "6606", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/20246/2cdde4e7d5010be2a35971e19f2285e4.png"},
    {"Character Name": "Ignis", "Skill id": "6706", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/202311/a393f95f57bdaa3d2031a052b6acef24.png"},
    {"Character Name": "Awakened Alok", "Skill id": "22016", "Png Image": "https://i.postimg.cc/KvHMG3Nc/Awakend-Alok.png"},
    {"Character Name": "Kairos", "Skill id": "6906", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/20246/ed1e34b6c47b37675eae84daffdf63b1.png"},
    {"Character Name": "Lila", "Skill id": "7106", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/20249/b09e7f93ec7c7a47dccbd704d8e4d879.png"},
    {"Character Name": "Kassie", "Skill id": "7006", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/20246/8d87fe1959e300741eda601e800c0f40.png"},
    {"Character Name": "Ryden", "Skill id": "6806", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/20241/fb808bb7cfc4820384c7a52fee3201ea.png"},
    {"Character Name": "Koda", "Skill id": "7206", "Png Image": "https://dl.dir.freefiremobile.com/common/web_event/official2.ff.garena.all/202412/b2f635a96ed787a8e540031402ea751b.png"}
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
