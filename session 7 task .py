import matplotlib.pyplot as plt
x=["Saturday" , "Sunday" , "Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday"]
y = [32, 29, 35, 31, 33, 30, 34] 
plt.plot(x,y,marker="o",linestyle=":",color="green")
plt.title('Weekly Temperature Report')
plt.xlabel("Days of the Week")
plt.ylabel("Temperature (°C)")
plt.show()