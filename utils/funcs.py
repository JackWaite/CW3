import requests
import datetime

url = "https://api.npoint.io/094d3a7a0d9569218a14"


def get_data():
    """Converting a file from json"""
    file = requests.get(url).json()
    return file


def executed_operations():
    """Selection of operations performed"""
    words = get_data()
    executed_operations_list = [
        word for word in words if word.get('state', '').lower() == 'executed'
    ]
    return executed_operations_list


def sort_data():
    """Sorting operations by date"""
    executed_operations_list = executed_operations()
    return sorted(executed_operations_list,
                  key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'),
                  reverse=True)


def last_operations():
    """Defining the last 5 operations"""
    return sort_data()[:5]


def hiding_card(last_five_operations):
    """Masking an account and a card"""
    for k in last_five_operations:
        if 'перевод' in k['description'].lower():
            if 'account' in k['from'].lower():
                k['from'] = k['from'][:(len(k['from']) - 4) - 10] + '*' * 6 + k['from'][(len(k['from']) - 4):]
            k['from'] = k['from'][:(len(k['from']) - 4) - 6] + '*' * 6 + k['from'][(len(
                k['from']) - 4):]
        k['to'] = k['to'][:(len(k['to']) - 4) - 16] + '*' * 2 + k['to'][(len(
            k['to']) - 4):]
    return last_five_operations


def date_new(last_five_operations):
    """Data output in the required format"""
    hiding_card(last_five_operations)
    for k in last_five_operations:
        k['date'] = (datetime.datetime.strptime(k['date'], "%Y-%m-%dT%H:%M:%S.%f")).strftime(
            "%d.%m.%Y")
    return last_five_operations


def result_output(last_five_operations):
    """Output function"""
    date_new(last_five_operations)
    for w in last_five_operations:
        if 'перевод' in w['description'].lower():
            print(
                f"{w['date']} {w['description']}\n{w['from']}  -> {w['to']}\n{w['operationAmount']['amount']}"
                f" {w['operationAmount']['currency']['name']} \n ")
        else:
            print(
                f"{w['date']} {w['description']}\n{w['to']}\n{w['operationAmount']['amount']}"
                f" {w['operationAmount']['currency']['name']} \n ")
    return True


def main():
    last_five_operations = last_operations()
    result_output(last_five_operations)
