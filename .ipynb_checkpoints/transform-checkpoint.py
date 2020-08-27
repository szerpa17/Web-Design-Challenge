import pandas as pd 
  
# Rad CSV
transform = pd.read_csv("cities.csv") 
  
# Save as HTML
transform.to_html("table.html", classes=["table", "table-bordered", "table-striped", "table-hover"], index=False) 
