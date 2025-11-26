import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def connect_to_database():
    """Connect to the SQLite database"""
    try:
        conn = sqlite3.connect("sales_data.db")
        print("✅ Successfully connected to the database!")
        return conn
    except sqlite3.Error as e:
        print(f"❌ Error connecting to database: {e}")
        return None

def run_sales_queries(conn):
    """Run SQL queries to get sales summary"""
    
    # Query 1: Total quantity and revenue by product
    query1 = """
    SELECT 
        product, 
        SUM(quantity) AS total_quantity,
        SUM(quantity * price) AS total_revenue
    FROM sales 
    GROUP BY product
    ORDER BY total_revenue DESC
    """
    
    # Query 2: Overall sales summary
    query2 = """
    SELECT 
        COUNT(*) AS total_transactions,
        SUM(quantity) AS overall_quantity,
        SUM(quantity * price) AS overall_revenue
    FROM sales
    """
    
    # Execute first query and load into pandas
    df_products = pd.read_sql_query(query1, conn)
    
    # Execute second query
    df_overall = pd.read_sql_query(query2, conn)
    
    return df_products, df_overall

def display_results(df_products, df_overall):
    """Display the query results"""
    
    print("=" * 50)
    print("📊 SALES SUMMARY REPORT")
    print("=" * 50)
    
    print("\n📈 PRODUCT PERFORMANCE:")
    print("-" * 40)
    print(df_products.to_string(index=False))
    
    print("\n🏆 OVERALL SALES SUMMARY:")
    print("-" * 40)
    print(f"Total Transactions: {df_overall['total_transactions'].iloc[0]}")
    print(f"Total Quantity Sold: {df_overall['overall_quantity'].iloc[0]}")
    print(f"Total Revenue: ${df_overall['overall_revenue'].iloc[0]:.2f}")

def create_bar_chart(df_products):
    """Create a bar chart showing revenue by product"""
    
    plt.figure(figsize=(10, 6))
    
    # Create bar chart
    bars = plt.bar(df_products['product'], df_products['total_revenue'], 
                   color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
    
    # Customize the chart
    plt.title('Total Revenue by Product', fontsize=16, fontweight='bold')
    plt.xlabel('Products', fontsize=12)
    plt.ylabel('Revenue ($)', fontsize=12)
    plt.xticks(rotation=45)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'${height:,.0f}',
                ha='center', va='bottom')
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Save the chart
    plt.savefig('sales_chart.png', dpi=300, bbox_inches='tight')
    print("✅ Chart saved as 'sales_chart.png'")
    
    # Display the chart
    plt.show()

def main():
    """Main function to run the sales analysis"""
    
    print("🚀 Starting Sales Analysis...")
    
    # Step 1: Connect to database
    conn = connect_to_database()
    if not conn:
        return
    
    try:
        # Step 2: Run queries
        df_products, df_overall = run_sales_queries(conn)
        
        # Step 3: Display results
        display_results(df_products, df_overall)
        
        # Step 4: Create visualization
        print("\n📊 Creating sales chart...")
        create_bar_chart(df_products)
        
    except Exception as e:
        print(f"❌ Error during analysis: {e}")
    
    finally:
        # Close database connection
        conn.close()
        print("\n✅ Analysis complete! Database connection closed.")

# Run the main function
if __name__ == "__main__":
    main()