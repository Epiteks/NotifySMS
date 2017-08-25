import os
import json
from bs4 import BeautifulSoup
from freemobilesms import SMS
from requester import Request


def _request(endpoint, method, token, body, data, error_type):
    req = Request("https://api.epiteks.xyz/intra/{endpoint}".format(endpoint=endpoint), method, body)
    if token is not None:
        req.set_header("token", token)
    status = req.execute()
    if status:
        return req.parse()["data"][data]
    else:
        raise Exception("Error while {type}".format(type=error_type))


def login(email, password):
    body = {
        "login": email,
        "password": password
    }
    return _request("login", "POST", None, body, "token", "login")


def get_history(token):
    return _request("infos", "GET", token, None, "history", "getting history")


def get_new_items(items):

    def _read():
        with open("history.json", "r") as file_data:
            parsed_data = json.load(file_data)
            return parsed_data["history"], int(parsed_data["last_id"])

    def _write(history):
        last_id = int(history[0]["id"])
        for item in history:
            id = int(item["id"])
            if id > last_id:
                last_id = id
        output_data = {
            "last_id": last_id,
            "history": history
        }
        with open("history.json", "w") as file_data:
            json.dump(output_data, file_data)

    try:
        history, last_id = _read()
        result = []
        for item in items:
            if int(item["id"]) > last_id:
                result.append(item)
        history = history + items
        _write(history)
        return result
    except:
        _write(items)
        return items


def format_item(item):
    url = "https://intra.epitech.eu"
    soup = BeautifulSoup(item["title"], "html.parser")
    links = []
    output = u"EPITECH\n-------\n{message}\n-----\nLiens:\n{links}"
    message = None
    for link in soup.find_all("a"):
        links.append("[{index}]: {url}{link}".format(index=len(links) + 1, url=url, link=link.get("href")))
        link.replace_with("{string}[{index}]".format(string=link.string, index=len(links)))
    for p in soup.find_all("p"):
        message = p.getText()
    return output.format(message=message, links="\n".join(links))


def send_message(content):
    service = SMS()
    return service.send(content)

if __name__ == '__main__':
    token = login(os.environ["EPITECH_MAIL"], os.environ["EPITECH_PWD"])
    data = get_history(token)
    if len(data):
        items = get_new_items(data)
        for item in items:
            text = format_item(item)
            code, message = send_message(text)
            print("ITEM #{id} : {code} ({message})".format(id=item["id"], code=code, message=message))
