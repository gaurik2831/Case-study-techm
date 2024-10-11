class Product:
    def __init__(self, pid, name, category, price):
        self.pid = pid
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self):
        return f"Product(PID: {self.pid}, Name: {self.name}, Category: {self.category}, Price: {self.price})"


class ProductApp:
    def __init__(self):
        self.products = []

    def add_product(self, pid, name, category, price):
        new_product = Product(pid, name, category, price)
        self.products.append(new_product)

    def update_product(self, pid, name=None, category=None, price=None):
        product = self.get_product_by_pid(pid)
        if product:
            if name:
                product.name = name
            if category:
                product.category = category
            if price is not None:
                product.price = price
            return product
        return None

    def delete_product(self, pid):
        product = self.get_product_by_pid(pid)
        if product:
            self.products.remove(product)
            return True
        return False

    def get_product_by_pid(self, pid):
        for product in self.products:
            if product.pid == pid:
                return product
        return None

    def get_all_products(self):
        return self.products

    def get_products_by_category(self, category):
        return [product for product in self.products if product.category == category]

    def get_products_between_prices(self, min_price, max_price):
        return [product for product in self.products if min_price <= product.price <= max_price]


def main():
    app = ProductApp()

    while True:
        print("\nOptions:")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. Get Product By PID")
        print("5. Get All Products")
        print("6. Get Products By Category")
        print("7. Get Products Between Prices")
        print("8. Exit")

        choice = input("Choose an option (1-8): ")

        if choice == '1':
            pid = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            category = input("Enter Product Category: ")
            price = float(input("Enter Product Price: "))
            app.add_product(pid, name, category, price)
            print("Product added.")

        elif choice == '2':
            pid = input("Enter Product ID to update: ")
            name = input("Enter new Product Name (leave blank to skip): ")
            category = input("Enter new Product Category (leave blank to skip): ")
            price_input = input("Enter new Product Price (leave blank to skip): ")
            price = float(price_input) if price_input else None
            updated_product = app.update_product(pid, name or None, category or None, price)
            if updated_product:
                print("Product updated:", updated_product)
            else:
                print("Product not found.")

        elif choice == '3':
            pid = input("Enter Product ID to delete: ")
            if app.delete_product(pid):
                print("Product deleted.")
            else:
                print("Product not found.")

        elif choice == '4':
            pid = input("Enter Product ID: ")
            product = app.get_product_by_pid(pid)
            if product:
                print("Product found:", product)
            else:
                print("Product not found.")

        elif choice == '5':
            print("All Products:", app.get_all_products())

        elif choice == '6':
            category = input("Enter Category: ")
            products = app.get_products_by_category(category)
            print(f"Products in {category}:", products)

        elif choice == '7':
            min_price = float(input("Enter minimum price: "))
            max_price = float(input("Enter maximum price: "))
            products = app.get_products_between_prices(min_price, max_price)
            print(f"Products between {min_price} and {max_price}:", products)

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
