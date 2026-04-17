import psycopg2
#establishing connection to postgres
conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='1234',dbname='myduka')
#object to perform database operations.
cur = conn.cursor()
def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products

product_data = get_products()
print(product_data)

def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales

sales_data = get_sales()
print(sales_data)

def get_stock():
    cur.execute("select * from stock")
    stock = cur.fetchall()
    print(stock)

def sales_per_product():
    cur.execute('''
        SELECT 
            products.name AS p_name,
            SUM(sales.quantity * products.selling_price) AS total_sales
        FROM sales
        JOIN products ON products.id = sales.pid
        GROUP BY products.name;
    ''')
    return cur.fetchall()
def sales_per_day():
    cur.execute("""
        select date(sales.created_at) as day,sum(sales.quantity * products.selling_price) as 
        total_sales from products join sales on sales.pid = products.id group by day;
    """)
    sales_day = cur.fetchall()
    return sales_day

def profit_per_product():
    cur.execute("""
        select products.name, sum((selling_price - buying_price) * quantity) as total_profit
        from sales join products on products.id = sales.pid group by p.id;
    """)
    profit_product = cur.fetchall()
    return profit_product

def profit_per_day():
    cur.execute('''
        select date(sales.created_at) as day, sum((selling_price - buying_price) * quantity) as total_profit
        from sales join products on products.id = sales p.id group by day;
    ''')
    profit_day = cur.fetchall()
    return profit_day




