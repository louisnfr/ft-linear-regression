import matplotlib.pyplot as plt

f = open("data.csv", "r")
lines = f.readlines()

xPoints: list[int] = []
yPoints: list[int] = []

for line in lines[1:]:
    x, y = line.strip().split(",")
    xPoints.append(int(x))
    yPoints.append(int(y))

plt.plot(xPoints, yPoints, "o")
plt.plot(xPoints, yPoints)
plt.xlabel(lines[0].split(",")[0])
plt.ylabel(lines[0].split(",")[1])
plt.show()
