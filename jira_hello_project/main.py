import configparser

from jira import JIRA
from prettytable import PrettyTable

config = configparser.ConfigParser()
config.read('config.ini')

server = config.get('JIRA', 'server')
login = config.get('JIRA', 'login')
password = config.get('JIRA', 'password')

jira = JIRA(options={'server': server}, basic_auth=(login, password))
issues_list = jira.search_issues('createdDate >= -1d')

table = PrettyTable()
table.field_names = ['Key', 'Assignee', 'Summary']
for field in table.field_names:
    table.align[field] = 'l'

for issue in issues_list:
    table.add_row([str(x).strip() for x in [issue.key, issue.fields.assignee, issue.fields.summary]])

print(table)
