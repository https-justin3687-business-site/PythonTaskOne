# Get radius from user
radius = int(input("Enter the radius:"))
PIE_VALUE = 3.1415926535
# calculate area
def calculate_area(PIE_VALUE, radius):
  if radius>= 1:
     area = PIE_VALUE * radius**2
     area = round(area)
     return area
    
    
print(calculate_area(PIE_VALUE, radius))








