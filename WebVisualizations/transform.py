import pandas as pd 
  
# Rad CSV
transform = pd.read_csv("cities.csv") 
  
# Save as HTML
transform.to_html("table.html") 
  
# # assign it to a  
# # variable (string) 
# html_file = a.to_html() 


# Need to build for loop in order to assign partitions.