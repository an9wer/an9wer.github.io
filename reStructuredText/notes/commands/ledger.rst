ledger
======

::

    Assets + Expenses = Liabilities + Income + Equity

Transaction State
-----------------

A transaction can have a “state”: cleared, pending, or uncleared. The default
is uncleared.

To mark a transaction cleared, put an asterisk ‘*’ after the date, before the
code or payee:

::

    2012-03-10 * KFC
        Expenses:Food                $20.00
        Assets:Cash

To mark it pending, use a ‘!’:

::

    2012-03-10 ! KFC
        Expenses:Food                $20.00
        Assets:Cash

What these mean is entirely up to you. The ``--cleared`` option limits reports
to only cleared items, while ``--uncleared`` shows both uncleared and pending
items, and ``--pending`` shows only pending items. 

You can mark individual postings as cleared or pending, in case one “side” of
the transaction has cleared, but the other hasn’t yet:

::

    2012-03-10 KFC
        Liabilities:Credit           $100.00
        * Assets:Checking


References
----------

`Plain Text Accounting <https://plaintextaccounting.org/>`_

`Ledger official documents <https://www.ledger-cli.org/3.0/doc/ledger3.html#Cleared-Report>`_

`Double-entry accounting <https://www.mathstat.dal.ca/~selinger/accounting/tutorial.html>`_

`Wikipedia: Double-entry bookkeeping <https://en.wikipedia.org/wiki/Double-entry_bookkeeping_system>`_

`Wikipedia: Normal balance <https://en.wikipedia.org/wiki/Normal_balance>`_

`Wikipedia: Equity <https://en.wikipedia.org/wiki/Equity_(finance)>`_

`Wikipedia: Debits and credits <https://en.wikipedia.org/wiki/Debits_and_credits>`_

有借必有贷，借贷必相等。会计中的借贷只是个记账符号，资产和费用类，借是增加，贷
是减少。负债、所有者权益、收入，借是减少，贷是增加。借方在账簿的左侧，贷方在账
簿的右侧。在任何会计事项中记账的原则如下：(1)资产、费用增加时，记入借方;资产、
费用减少时，记入贷方。(2)负债、所有者权益、收入增加时，记入贷方;负债、所有者权
益、收入减少时，记入借方。
