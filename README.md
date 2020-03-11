# Bank-Accout-System

In this project, I have designed an implement a system that will be used to represent bank accounts.

The system the following functionality and characteristics:
- accounts are uniquely identified by an `account number` (assume it will just be passed in the initializer)
- account holders have a `first` and `last` name
- accounts have an associated `preferred time zone offset` (e.g. -7 for MST)
- `balances` need to be zero or higher, and should not be directly settable.
- but, `deposits` and `withdrawals` can be made (given sufficient funds)
    - if a withdrawal is attempted that would result in negative funds, the transaction should be declined.
- a `monthly interest rate` exists and is applicable to all accounts **uniformly**. There should be a method that can be called to calculate the interest on the current balance using the current interest rate, and add it to the balance.
- each deposit and withdrawal must generate a `confirmation number` composed of:
    - the transaction type: `D` for deposit, and `W` for withdrawal, `I` for interest deposit, and `X` for declined (in which case the balance remains unaffected)
    - the account number
    - the time the transaction was made, using UTC
    - an incrementing number (that increments across all accounts and transactions)
    - for simplicity assume that the transaction id starts at zero (or whatever number you choose) whenever the program starts
    - the confirmation number should be returned from any of the transaction methods (deposit, withdraw, etc)
-  contains method that, given a confirmation number, returns:
    - the account number, transaction code (D, W, etc), datetime (UTC format), date time (in whatever timezone is specified in te argument, but more human readable), the transaction ID
    
For example, we have an account with:
- account number `140568` 
- preferred time zone offset of -7 (MST) 
- an existing balance of `100.00`

Suppose the last transaction ID in the system was `123`, and a deposit is made for `50.00` on `2019-03-15T14:59:00` (UTC) on that account (or `2019-03-15T07:59:00` in account's preferred time zone offset)

The new balance should reflect `150.00` and the confirmation number returned should look something like this:

```D-140568-20190315145900-124```

System also has a method that given the confirmation number returns an object with attributes:
- `result.account_number` --> `140568`
- `result.transaction_code` --> `D`
- `result.transaction_id` --> `124`
- `result.time` --> `2019-03-15 07:59:00 (MST)`
- `result.time_utc` --> `2019-03-15T14:59:00`   

Furthermore, if current interest rate is `0.5%`, and the account's balance is `1000.00`, then the result of calling the `deposit_interest` (or whatever name you choose) method, should result in a new transaction and a new balance of `1050.00`. Calling this method should also return a confirmation number.

I have created two classes: a **TimeZone** class used to store the time zone name and offset definition (in hours and minutes), and a main class called **Account** that will have the following "public" interface:
- initializer with account number, first name, last name, optional preferred time zone, starting balance (defaults to 0)
- a first name property (read/write)
- a last name property (read/write)
- a full name property (computed, read-only)
- a balance property (read-only)
- an interest rate property (class level property)
- deposit, withdraw, pay_interest methods
- parse confirmation code

Finally, I tested code using Python's **unittest** package.
