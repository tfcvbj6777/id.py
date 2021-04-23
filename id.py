import amino 
email = input("Почта:")
password = input("Пароль:")
client = amino.Client()
client.login(email=email, password=password)
while True:
    link = input('адресная ссылка объекта: ');
    info = client.get_from_code(link)
    info = info.json["extensions"]["linkInfo"];
    comid  = info["ndcId"];
    objectid = info["objectId"];
    print(f'ID сообщества: {comid} ID объекта: {objectid}')
