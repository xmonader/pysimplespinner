# pysimplespinner
spinner for busy computations in the command line in python based on node-simplespinner 

You can use it as a context manager to show a spinner while doing some heavy computation

```python

    with Spinner():
        print("Long computation")
        time.sleep(5)
    print("Done")


```
