from models import Electronics, Grocery


class InventoryIterator:
    def __init__(self, products):
        self._products = list(products.values())
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._products):
            raise StopIteration
        item = self._products[self._index]
        self._index += 1
        return item


class Inventory:
    def __init__(self):
        self.__products = {}

    def __iter__(self):
        return InventoryIterator(self.__products)

    def add_product(self, product):
        pid = product.get_id()
        if pid in self.__products:
            raise ValueError("Product ID already exists!")
        self.__products[pid] = product

    def remove_product(self, product_id):
        if product_id not in self.__products:
            raise KeyError("Product not found!")
        del self.__products[product_id]

    def get_product(self, product_id):
        return self.__products.get(product_id)

    def update_stock(self, product_id, qty, mode="add"):
        product = self.get_product(product_id)
        if not product:
            raise KeyError("Product not found!")

        if mode == "add":
            product.add_stock(qty)
        elif mode == "remove":
            product.remove_stock(qty)
        else:
            raise ValueError("Invalid stock mode!")

    def search(self, keyword):
        keyword = keyword.lower()
        results = []
        for product in self.__products.values():
            if keyword in product.get_name().lower() or keyword in product.get_id().lower():
                results.append(product)
        return results

    def to_list(self):
        return [p.to_dict() for p in self.__products.values()]

    def load_from_list(self, data):
        self.__products = {}
        for item in data:
            if item["type"] == "Electronics":
                p = Electronics(
                    item["id"], item["name"], item["price"], item["stock"],
                    item["brand"], item["warranty_years"]
                )
            elif item["type"] == "Grocery":
                p = Grocery(
                    item["id"], item["name"], item["price"], item["stock"],
                    item["expiry_date"]
                )
            else:
                continue
            self.__products[p.get_id()] = p