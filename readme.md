#This is a test python lock which will lock your python for 1 hr after called. Takes a break...

```
pip install git+https://github.com/DAF201/lock
```

How to use:

```python

import locks

locks.create_clock()

```

this will lock your python for 1 hour, if any action is engaged, the countdown will be reset, including pip.

It will automatically unlock after no action for 1 hr

<img src='https://github.com/DAF201/locks/blob/main/locks/Screenshot%20(370).png'>
