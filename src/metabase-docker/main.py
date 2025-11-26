from models import Base, Product, get_engine, get_session
from datetime import datetime, timedelta
import random


def create_tables():
    """Create all tables in the database"""
    engine = get_engine()
    Base.metadata.create_all(engine)
    print("✓ Tables created successfully")


def insert_sample_data():
    """Insert sample products into the database"""
    session = get_session()

    try:
        # Product categories and sample products
        products_data = [
            # Electronics
            ("Laptop Dell XPS 15", "Electronics", 1299.99, 45),
            ("iPhone 15 Pro", "Electronics", 999.99, 120),
            ("Samsung 4K TV 55\"", "Electronics", 699.99, 35),
            ("Sony Headphones WH-1000XM5", "Electronics", 349.99, 78),
            ("Apple Watch Series 9", "Electronics", 429.99, 92),
            
            # Clothing
            ("Nike Air Max Sneakers", "Clothing", 129.99, 156),
            ("Levi's 501 Jeans", "Clothing", 79.99, 203),
            ("Adidas Running Jacket", "Clothing", 89.99, 87),
            ("H&M Cotton T-Shirt", "Clothing", 19.99, 421),
            ("Zara Winter Coat", "Clothing", 159.99, 64),
            
            # Home & Kitchen
            ("KitchenAid Stand Mixer", "Home & Kitchen", 449.99, 38),
            ("Nespresso Coffee Machine", "Home & Kitchen", 199.99, 92),
            ("Dyson Vacuum Cleaner", "Home & Kitchen", 549.99, 47),
            ("Air Fryer 5L", "Home & Kitchen", 119.99, 134),
            ("Le Creuset Dutch Oven", "Home & Kitchen", 299.99, 52),
            
            # Books
            ("The Great Gatsby", "Books", 14.99, 287),
            ("1984 by George Orwell", "Books", 16.99, 312),
            ("Harry Potter Collection", "Books", 89.99, 145),
            ("The Lean Startup", "Books", 24.99, 198),
            ("Atomic Habits", "Books", 19.99, 267),
            
            # Sports & Outdoors
            ("Yoga Mat Premium", "Sports & Outdoors", 39.99, 178),
            ("Dumbbells Set 20kg", "Sports & Outdoors", 79.99, 95),
            ("Mountain Bike 27.5\"", "Sports & Outdoors", 599.99, 42),
            ("Camping Tent 4-Person", "Sports & Outdoors", 199.99, 67),
            ("Running Shoes Asics", "Sports & Outdoors", 119.99, 142),
        ]

        products = []
        base_date = datetime.now() - timedelta(days=90)  # Last 90 days
        
        for name, category, price, qty_base in products_data:
            # Randomize sale date within last 90 days
            days_offset = random.randint(0, 89)
            sale_date = base_date + timedelta(days=days_offset)
            
            # Add some randomness to quantity sold
            quantity_sold = qty_base + random.randint(-10, 20)
            quantity_sold = max(1, quantity_sold)  # Ensure at least 1
            
            # Calculate revenue
            revenue = round(price * quantity_sold, 2)
            
            product = Product(
                name=name,
                category=category,
                price=price,
                quantity_sold=quantity_sold,
                revenue=revenue,
                sale_date=sale_date
            )
            products.append(product)

        session.add_all(products)
        session.commit()
        print(f"✓ Inserted {len(products)} products successfully")

        # Display summary by category
        print("\n📊 Sales Summary by Category:")
        for category in ["Electronics", "Clothing", "Home & Kitchen", "Books", "Sports & Outdoors"]:
            category_products = [p for p in products if p.category == category]
            total_revenue = sum(p.revenue for p in category_products)
            total_quantity = sum(p.quantity_sold for p in category_products)
            print(f"  {category}:")
            print(f"    - Total Revenue: ${total_revenue:,.2f}")
            print(f"    - Total Units Sold: {total_quantity}")

        # Query and display sample data
        print("\n📦 Sample Products (first 5):")
        sample_products = session.query(Product).limit(5).all()
        for product in sample_products:
            print(f"  - {product}")

    except Exception as e:
        session.rollback()
        print(f"✗ Error: {e}")
        raise
    finally:
        session.close()


if __name__ == "__main__":
    print("Creating tables...")
    create_tables()

    print("\nInserting sample data...")
    insert_sample_data()

    print("\n✓ Done! You can now:")
    print("  1. Access Metabase at http://localhost:3000")
    print("  2. Connect with DBeaver to see the data")
    print("  3. Create dashboards and visualizations in Metabase")
