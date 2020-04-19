from flask import Flask,request
import hashlib,sqlite3

app = Flask(__name__)

user_name="abderrahmen"
s_key="1234"

@app.route('/verify')
def verify():
    sent = request.args["crp_key"]
    print(sent)
    db_conn = sqlite3.connect('conpany.db')
    lignes = db_conn.execute("SELECT user_names, s_keys from COMPANY_TAB1")
    print(lignes)
    print("zzzzzzzzzzzzzzzzzzzzzzzzzz")
    for col in lignes:
        print(col[0])
        user_name_encoded=col[0].encode()
        s_key_encoded=col[1].encode()
        print(col[1])
        c= hashlib.md5() 
        c.update(user_name_encoded)
        c.update(s_key_encoded)
        cript = c.hexdigest()
        print(sent)
        if cript== sent:
            req="true"
    print(req)
    return req

    

    

if __name__ == '__main__':
    app.run()
