import requests
import datetime

url = "https://api.npoint.io/094d3a7a0d9569218a14"


class BankTransactions:
    def init(self, url):
        self.url = url

    def get_data(self):
        """Converting a file from json"""
        file = requests.get(self.url).json()
        return file

    def executed_operations(self):
        """Selection of operations performed"""
        words = self.get_data()
        executed_operations_list = [
            word for word in words if word.get('state', '').lower() == 'executed'
        ]
        return executed_operations_list

    def sort_data(self):
        """Sorting operations by date"""
        executed_operations_list = self.executed_operations()
        return sorted(executed_operations_list,
                      key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'),
                      reverse=True)

    def last_operations(self):
        """Defining the last 5 operations"""
        return self.sort_data()[:5]

    def hiding_card(self, last_five_operations):
        """Masking an account and a card"""
        for k in last_five_operations:
            if 'transfer' in k['description'].lower():
                if 'account' in k['from'].lower():
                    k['from'] = k['from'][:(len(k['from']) - 4) - 10] + '*' * 6 + k['from'][(len(k['from']) - 4):]
                k['from'] = k['from'][:(len(k['from']) - 4) - 6] + '*' * 6 + k['from'][(len(
                    k['from']) - 4):]
            k['to'] = k['to'][:(len(k['to']) - 4) - 16] + '*' * 2 + k['to'][(len(
                k['to']) - 4):]
        return last_five_operations

    def date_new(self, last_five_operations):
        """Data output in the required format"""
        self.hiding_card(last_five_operations)
        for k in last_five_operations:
            k['date'] = (datetime.datetime.strptime(k['date'], "%Y-%m-%dT%H:%M:%S.%f")).strftime(
                "%d.%m.%Y")
        return last_five_operations

    def result_output(self, last_five_operations):
        """Output function"""
        self.date_new(last_five_operations)
        for w in last_five_operations:
            if 'transfer' in w['description'].lower():
                print(
                    f"{w['date']} {w['description']}\n{w['from']} ->"
                    f" {w['to']}\n{w['operationAmount']['amount']} {w['operationAmount']['currency']['name']} \n ")
            else:
                print(
                    f"{w['date']} {w['description']}\n{w['to']}\n{w['operationAmount']['amount']}"
                    f" {w['operationAmount']['currency']['name']} \n ")
        return True

    def main(self):
        last_five_operations = self.last_operations()
        self.result_output(last_five_operations)


if __name__ == 'main':
    BankTransactions().main()

