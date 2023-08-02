# langchain_mess

Here messing around different langchain scenarios.


## Develop

```
pip install -r requirements.txt
```
## Talk to CSV

```How it works
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

