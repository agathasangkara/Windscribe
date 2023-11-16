try:
    import requests as r, os, sys as s
    from colorama import Fore as x
    from faker import Faker as f
    from datetime import datetime
except Exception as e:
    print(f" {x.RED}Some library not installed | pip install -r requirements.txt")
    exit(1)


class Windscribe:

    def __init__(self) -> None:
        self.api = r.Session()
        self.password = "@Sangkara123"
        self.hash = "6d772ab972f389264572ccec9be56ce8" #change / u can intercept app windscribe to get this             
        self.timestamp = "1700038279400" #change / u can intercept app windscribe to get this string
        # self.timestamp = str(int(datetime.now().timestamp() * 1000))
        
    def create_account(self, username, email):
        try:
            headers = {
                "content-type":"application/x-www-form-urlencoded",
                "user-agent":"user-agent"
            }
            data = f"platform=android&app_version=3.74.1259&client_auth_hash={self.hash}&session_type_id=4&time={self.timestamp}&password={self.password}&username={username}&email={email}"
            return self.api.post("https://api.windscribe.com/Users", data=data, headers=headers)
        except Exception as e:
            return None
    
    def verify_email(self, email):
        while True:
            headers = {
                "User-Agent":"Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36"
            }
            cek_message = self.api.get(f"https://tempmail.plus/api/mails?email={email}", headers=headers)
            if "Windscribe" in cek_message.text:
                return self.api.get(f"https://tempmail.plus/api/mails/{cek_message.json()['first_id']}?email={email}", headers=headers).json()['text']
            else:
                continue
    
    def claim_voucher(self, code, session):
        headers = {
            "User-Agent":"Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
            "cookie":f"ws_session_auth_hash={session}"
        }
        get_data = self.api.get("https://windscribe.com/myaccount", headers=headers).text
        csrf = get_data.split("csrf_token = '")[1].split("';")[0]
        ctime = get_data.split("csrf_time = ")[1].split(";")[0]
        data = f"code={code}&ctoken={csrf}&ctime={ctime}"
        headers = {
            "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent":"Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
            "cookie":f"ws_session_auth_hash={session}"
        }
        return self.api.post("https://windscribe.com/myaccount/claimvoucher", data=data, headers=headers)
