class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.length = len(collection)
        self.remainder = self.item_count() % self.items_per_page
        self.quotient = self.item_count() // self.items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return self.length

    # returns the number of pages
    def page_count(self):
        if self.remainder == 0:
            return self.quotient
        else:
            return self.quotient + 1


    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if -1 < page_index < self.page_count()-1:
            return self.items_per_page
        elif page_index == self.page_count()-1:
            return self.item_count() % self.items_per_page
        else:
            return -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if -1 < item_index < self.length:
            return item_index//self.items_per_page
        else:
            return -1

# Test Unit

collection = range(1,25)
helper = PaginationHelper(collection, 10)

print(helper.page_index(0))
print(helper.page_index(20))
