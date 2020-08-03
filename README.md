# CodeWars.Kata.PaginationHelper

For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array. <br/>

The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. The types of values contained within the collection/array are not relevant. <br/>

The following are some examples of how this class is used: <br/>





helper = PaginationHelper(['a','b','c','d','e','f'], 4) <br/>
helper.page_count # should == 2 <br/>
helper.item_count # should == 6 <br/>
helper.page_item_count(0)  # should == 4 <br/>
helper.page_item_count(1) # last page - should == 2 <br/>
helper.page_item_count(2) # should == -1 since the page is invalid <br/>

### page_index takes an item index and returns the page that it belongs on <br/>
helper.page_index(5) # should == 1 (zero based index) <br/>
helper.page_index(2) # should == 0 <br/>
helper.page_index(20) # should == -1 <br/>
helper.page_index(-10) # should == -1 because negative indexes are invalid <br/>
