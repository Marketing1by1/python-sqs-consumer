#!/usr/bin/env python3

import multiprocessing
import time

import sqsconsumer 

messageQueue = multiprocessing.Queue()

if __name__ == "__main__":
	stats = sqsconsumer.Statser()
	stats.start()

	for i in range(1):
		consumer = sqsconsumer.Consumer("",
			"us-west-2",
			"",
			"",
			messageQueue,
			3)
		consumer.run()

	while True:
		m = messageQueue.get()
		print(m.get_body())
		m.delete()
		time.sleep(5)
