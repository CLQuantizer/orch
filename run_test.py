from time import sleep

from tq.tasks.tokenize import add

if __name__ == "__main__":
    # sleep 2 seconds
    sleep(2)
    result = add.delay(4, 4)
    print(f"Task ID: {result.id}")
    print(f"Task result: {result.get()}")