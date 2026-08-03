from arm import R3arm
import numpy as np
import pandas as pd
jacobian_test = R3arm(140,110,90)
theta = np.array([np.pi/4,np.pi/3,np.pi/2])
Jnum = jacobian_test.jacobian_numerical(theta)
J = jacobian_test.jacobian(theta)
Jerr = J-Jnum
df1 = pd.DataFrame(Jnum, columns=["θ₁", "θ₂", "θ₃"], index=["ẋ", "ẏ"])
df2 = pd.DataFrame(J, columns=["θ₁", "θ₂", "θ₃"], index=["ẋ", "ẏ"])
Jerr = pd.DataFrame(Jerr, columns=["θ₁", "θ₂", "θ₃"], index=["ẋ", "ẏ"])
print("Numerical jacobian:")
print(df1)
print("Analytical jacobian:")
print(df2)
print("Numerical error (Analytical - Numerical)")
print(Jerr)