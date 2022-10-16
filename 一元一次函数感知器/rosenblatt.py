import dataset
from matplotlib import pyplot as plt

xs,ys=dataset.get_beans(100)
print(xs)
print(ys)

plt.title("Size-Toxicity Function",fontsize=12)
plt.xlabel("Bean Size")
plt.ylabel("Toxicity")
plt.scatter(xs,ys)

#y=0.5*x
w=0.5
alpha=0.05
for i in range(100):
    for i in range(100):
        x=xs[i]
        y=ys[i]
        y_pre=w*x
        e=y-y_pre
        w=w+alpha*e*x

y_pre=w*xs

print(y_pre)

plt.plot(xs,y_pre)

plt.show()