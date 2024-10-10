import sqlite3
import csv
from datetime import datetime

# Function to generate a daily report
def generate_daily_report(date):
    # Connect to the database
    connection = sqlite3.connect('sales.db')
    cursor = connection.cursor()

    # Query sales for the specified date
    cursor.execute('''
        SELECT * FROM daily_sales WHERE date = ?
    ''', (date,))
    
    sales = cursor.fetchall()

    # Create a CSV file for the report
    report_name = f'sales_report_{date}.csv'
    with open(report_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write the header
        csv_writer.writerow(['ID', 'Date', 'Product', 'Quantity', 'Price', 'Total'])
        
        # Write sales data
        csv_writer.writerows(sales)
    
    print(f'Report generated: {report_name}')
    
    # Close the connection
    connection.close()

# Generate report for the current date
current_date = datetime.now().strftime('%Y-%m-%d')
generate_daily_report(current_date)