try:
    from api import Windscribe
    from colorama import Fore as x
    import requests as r, sys as s, random, os
except Exception as e:
    s.exit(f" {x.RED}Some library not installed | pip install -r requirements.txt")

os.system('cls' if os.name == "nt" else 'clear')
try:
    datauser = r.get("http://api.suhu.my.id/v2/faker", headers={"User-Agent": "PanelNewbie/0.2 (Linux; rdhoni;) Termux/0.2"}).json()
    username = datauser["nama"].replace(" ","").lower()
    email = f"{username}{random.randint(10,99)}@any.pink"
    try:
        #create account
        signup = Windscribe().create_account(username, email)
        if signup.status_code == 201:
            session = signup.json()["data"]["session_auth_hash"]
            print(f" {username} | {x.GREEN}Successfully Create{x.WHITE}")
            # Verify Email Temporary Account
            msg = Windscribe().verify_email(email)
            verify = r.get(f"{msg.split('Confirm Email (for 10GB) ( ')[1].split(' )')[0]}", headers={"User_Agent":"Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36"})
            code = "" # code / voucher
            claim = Windscribe().claim_voucher(code, session)
            if claim.json()["success"] == 0:
                print(f' {claim.json()["message"]} | {x.RED}Failed Approved\n')
            else:
                print(f' {claim.json()["plan"]} | {x.GREEN}Successfully Approved\n')
        else:
            s.exit(f" {x.RED}{signup.json()['message']}")
    except Exception as e:
        s.exit(f" {x.RED}An Error Occured | {e}")
except Exception as e:
    s.exit(f" {x.RED}An Error Occured | {e}")
