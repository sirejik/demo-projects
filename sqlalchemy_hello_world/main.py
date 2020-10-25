from prettytable import PrettyTable

from data.models import create_tables_by_models_if_not_exist
from data.objects import create_account
from utils.db import get_db_engine, get_session


db_engine = get_db_engine()
create_tables_by_models_if_not_exist(db_engine)
session = get_session(db_engine)

table = PrettyTable()
table.field_names = ['First name', 'Last name', 'Login', 'Password']
for field in table.field_names:
    table.align[field] = 'l'

for _ in range(10):
    account = create_account(session)
    table.add_row(
        [account.first_name, account.last_name, account.authentication.login, account.authentication.password]
    )

print(table)
