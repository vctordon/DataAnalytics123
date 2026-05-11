#SALES LIST

sales_data = [
('Marcus Webb', 'East', 4250.00),
('Priya Sharma', 'West', 5875.50),
('DeShawn Carter', 'East', 3100.75),
('LaTonya Rivers', 'South', 6420.00),
('Bob Nguyen', 'West', 4980.25),]


# Loop through each record and unpack the tuple
for name, region, total_sales in sales_data:
    print(f"{name} ({region}): ${total_sales:,.2f}")

    # Check for top performers
    if total_sales > 5000:
        print(" ^ Top performer!")