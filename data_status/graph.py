import matplotlib.pyplot as pylot

x = [1, 2, 3, 4, 5, 6, 7] # January 10, 2023 as DAY 1
y = [6, 11, 7, 2, 7, 0, 8] # Number of commits for AXEL-U

pylot.plot(x, y)

pylot.title("AXEL-U Commits Progress")
pylot.ylabel("Days") # Y-label
pylot.xlabel("No. of Commits") # X-label

pylot.show()