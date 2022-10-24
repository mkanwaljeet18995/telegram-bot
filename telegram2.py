import requests
import json


def send_telegram_message(message: str,
                          chat_id: str,
                          api_key: str,
                          proxy_username: str = None,
                          proxy_password: str = None,
                          proxy_url: str = None):
    responses = {}

    proxies = None
    if proxy_url is not None:
        proxies = {
            'https': f'http://{proxy_username}:{proxy_password}@{proxy_url}',
            'http': f'http://{proxy_username}:{proxy_password}@{proxy_url}'
        }
    headers = {'Content-Type': 'application/json',
               'Proxy-Authorization': 'Basic base64'}
    data_dict = {'chat_id': chat_id,
                 'text': message,
                 'parse_mode': 'HTML',
                 'disable_notification': True}
    data = json.dumps(data_dict)
    url = f'https://api.telegram.org/bot{api_key}/sendMessage'
    response = requests.post(url,
                             data=data,
                             headers=headers,
                             proxies=proxies,
                             verify=False)
    return response


def print_hi(name):
    chat_id = "5747397041"
    # "1781954191"
    # "5747397041"
    api_key = "5544054333:AAGt__sHvHACotN3azOVM_GP4q5I4j9qx7M"
    send_telegram_message("GOOD ONE", chat_id, api_key)


if __name__ == '__main__':
    print_hi('PyCharm')
