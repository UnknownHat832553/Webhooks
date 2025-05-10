from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return """<!DOCTYPE html>
<head><title>กลุ่ม Discord ผม</title><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><style>*{margin:0;padding:0;box-sizing:border-box;}body{font-family:'Arial',sans-serif;background:linear-gradient(45deg,#6a11cb,#2575fc);display:flex;justify-content:center;align-items:center;height:100vh;color:white;}.wrapper{display:flex;justify-content:center;align-items:center;width:100%;height:100%;}.card{background-color:#2C2F3E;border-radius:20px;box-shadow:0 10px 30px rgba(0,0,0,0.2);padding:40px;text-align:center;width:100%;max-width:400px;transition:transform 0.3s ease-in-out,box-shadow 0.3s ease-in-out;}.card:hover{transform:translateY(-10px);box-shadow:0 15px 50px rgba(0,0,0,0.3);}h1{font-size:2.5rem;margin-bottom:20px;letter-spacing:1px;}p{font-size:1.2rem;margin-bottom:30px;}button{background-color:#7289DA;color:white;border:none;padding:15px 30px;font-size:1.2rem;border-radius:25px;cursor:pointer;transition:background-color 0.3s,transform 0.2s;width:100%;}button:hover{background-color:#5C6EB1;transform:scale(1.1);}button:active{background-color:#4F5A8A;transform:scale(1);}</style>
</head>
<body><div class="wrapper"><div class="card"><h1>สวัสดีคับ!</h1><p>กลุ่ม Discord ของผม</p><button onclick="joinDiscord()">เข้าร่วม Discord</button></div></div><script>function joinDiscord(){const discordLink = 'https://discord.gg/x3XkCBswvY';window.location.href = discordLink;}</script>
</body>
</html>"""

def run():
  app.run(host='0.0.0.0',port=8080)

def server_on():
    t = Thread(target=run)
    t.start()
