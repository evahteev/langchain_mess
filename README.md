# langchain_mess

Here messing around different langchain scenarios.


## Develop

```
pip install -r requirements.txt
```
## Talk to CSV
How it works:
```
> Entering new  chain...
huggingface/tokenizers: The current process just got forked, after parallelism has already been used. Disabling parallelism to avoid deadlocks...
To disable this warning, you can either:
	- Avoid using `tokenizers` before the fork if possible
	- Explicitly set the environment variable TOKENIZERS_PARALLELISM=(true | false)
huggingface/tokenizers: The current process just got forked, after parallelism has already been used. Disabling parallelism to avoid deadlocks...
To disable this warning, you can either:
	- Avoid using `tokenizers` before the fork if possible
	- Explicitly set the environment variable TOKENIZERS_PARALLELISM=(true | false)
 I need to find out the total amount of transactions
Action: transactions_db
Action Input: What is the total amount of transactions?
Observation:  The total amount of transactions is 50783214.81.
Thought: I now know the final answer
Final Answer: The total amount of transactions is 50783214.81.


```
```
cd talk_to_csv
python ./scripts/talk_to_csv.py
```

## Fill up warehouse descriptions 
How it works:

```bash

Generated API documentation description for Query 69:
This API Endpoint is designed to retrieve and present account balances records from a specified blockchain network. It selects and organizes the information about the account's token_address, chain_id, timestamp of last update, balance, token_standard, and token_id.

The required parameters for this query are: 
'chain_id' (text) which indicates the ID of the blockchain chain,
'network' (text) refers to the specific public blockchain network,
'account_address' (text) signifies the address of the account from which balances are being fetched,
and 'token_address' (text) that gives the address of the tokens in the account.

```


