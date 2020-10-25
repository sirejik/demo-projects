import names

from password_generator import PasswordGenerator

from data.models import Account, Authentication


def create_account(session):
    account = Account(first_name=names.get_first_name(), last_name=names.get_last_name())
    session.add(account)

    password_generator = PasswordGenerator()
    authentication = Authentication(
        account=account,
        login='{}_{}'.format(account.first_name, account.last_name).lower(),
        password=password_generator.generate()
    )
    session.add(authentication)

    session.commit()
    return account
