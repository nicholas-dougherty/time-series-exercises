import pandas as pd
import requests
import os

def get_items_df(use_cache=True):
    '''
    This function creates a request from the REST API at https://api.data.codeup.com/api/v1/stores
    and transforms the response into a pandas dataframe named items. It then saves the data as a csv file.
    '''
    # If the cached parameter is True, read the csv file on disk in the same folder as this file 
    if os.path.exists('items_df.csv') and use_cache:
        print('Using cached CSV')
        return pd.read_csv('items_df.csv')
   
    # Otherwise, proceed with the following
    print('CSV not present, initializating acquisition')
    
    # create the empty list which will be appended with data with each iteration 
    items = []

    # define the url from where the data is stored
    domain = 'https://api.data.codeup.com'
    endpoint = '/api/v1/items'
    url = domain + endpoint
    
    # define the response by the request
    response = requests.get(url)
    # convert the response to json
    data = response.json()
    # define the number of pages based on the max_page value 
    n = data['payload']['max_page']
    # Create a loop to iterate through each page starting with page 1 and ending on page n + 1
    # be sure to include the last page.
    # p is the page number
    for p in range(1, n+1):
        # define the new url returned for next page
        new_url = url+"?page="+str(p)
        # define the response requested
        response = requests.get(new_url)
        # convert response to json
        data = response.json()
        #create the variable to hold the items returned from the response
        page_items = data['payload']['items']
        # add the items from the page to the items list and continue to iterate through n pages
        page_items = items.extend(data['payload']['items'])
    
        # Create a dataframe of the items_list that now hold all the items from all pages
    items_df = pd.DataFrame(items)
    
    print('iteration complete, creating CSV')
        #also cache the data we read from the REST API to a file on disk
    items_df.to_csv('items_df.csv', index=False)
        

    print('DataFrame available for use')
    
    return items_df


def get_stores_df(use_cache=True):
    '''
    This function creates a request from the REST API at https://api.data.codeup.com/api/v1/stores
    and transforms the response into a pandas dataframe named items. It then saves the data as a csv file.
    '''
    # If the cached parameter is True, read the csv file on disk in the same folder as this file 
    if os.path.exists('stores_df.csv') and use_cache:
        print('Using cached CSV')
        return pd.read_csv('stores_df.csv')
   
    print('CSV not present, initializating acquisition')
    
    # create the empty list which will be appended with data with each iteration 
    store_list = []
    print('Creating store list')
    # define the url from where the data is stored
    domain = 'https://python.zgulde.net'
    endpoint = '/api/v1/stores'
    url = domain + endpoint

    # define the response by the request
    response = requests.get(url)
    # convert the response to json
    data = response.json()
    # define the number of pages based on the max_page value 
    n = data['payload']['max_page']
    
    print('Iterating through webpages and appending content to store list')
    # Create a loop to iterate through each page starting with page 1 and ending on page n + 1
    # be sure to include the last page.
    # p is the page number
    for p in range(1, n+1):
        # define the new url returned for next page
        new_url = url+"?page="+str(p)
        # define the response requested
        response = requests.get(new_url)
        # convert response to json
        data = response.json()
        #create the variable to hold the items returned from the response
        page_stores = data['payload']['stores']
        # add the items from the page to the items list and continue to iterate through n pages
        page_stores = store_list.extend(data['payload']['stores'])
        
    print('iteration complete, creating CSV')
        # Create a dataframe of the items_list that now hold all the items from all pages
        
    stores_df = pd.DataFrame(store_list)
        
    stores_df.to_csv('stores_df.csv', index=False)
    
    print('DataFrame available for use')
    
    return stores_df

# assuming stores is supposed to just be ten rows, moving forward.
def get_sales_df(use_cache=True):
    '''
    This function creates a request from the REST API at https://api.data.codeup.com/api/v1/stores
    and transforms the response into a pandas dataframe named items. It then saves the data as a csv file.
    '''
    # If the cached parameter is True, read the csv file on disk in the same folder as this file 
    if os.path.exists('sales_df.csv') and use_cache:
        print('Using cached CSV')
        return pd.read_csv('sales_df.csv')
   
    print('CSV not present, initializating acquisition')
    
    # create the empty list which will be appended with data with each iteration 
    sales_list = []
    print('Creating sales list')
    
    # define the url from where the data is stored
    domain = 'https://python.zgulde.net'
    endpoint = '/api/v1/sales'
    url = domain + endpoint

    # define the response by the request
    response = requests.get(url)
    # convert the response to json
    data = response.json()
    # define the number of pages based on the max_page value 
    n = data['payload']['max_page']
    
    print('Iterating through webpages and appending content to store list')
    # Create a loop to iterate through each page starting with page 1 and ending on page n + 1
    # be sure to include the last page.
    # p is the page number
    for p in range(1, n+1):
        # define the new url returned for next page
        new_url = url+"?page="+str(p)
        # define the response requested
        response = requests.get(new_url)
        # convert response to json
        data = response.json()
        #create the variable to hold the items returned from the response
        page_sales = data['payload']['sales']
        # add the items from the page to the items list and continue to iterate through n pages
        page_sales = sales_list.extend(data['payload']['sales'])
        
    print('iteration complete, creating CSV')
        # Create a dataframe of the items_list that now hold all the items from all pages
        
    sales_df = pd.DataFrame(sales_list)
    # Noticed some keys need to be fixed
    #sales_df.rename(columns={'item':'item_id','store':'store_id'},inplace=True)
    sales_df = sales_df.rename(columns={'item':'item_id','store':'store_id'})
        
    sales_df.to_csv('sales_df.csv', index=False)
    
    print('DataFrame available for use')
    
    return sales_df

def get_combined_df(use_cache=True):
    '''
    This function creates a request from the REST API at https://api.data.codeup.com/api/v1/stores
    and transforms the response into a pandas dataframe named items. It then saves the data as a csv file.
    '''
    # If the cached parameter is True, read the csv file on disk in the same folder as this file 
    if os.path.exists('sales_stores_items.csv') and use_cache:
        print('Using cached CSV')
        return pd.read_csv('sales_stores_items.csv')
    
    #Otherwise, create the DF using previous cached CSVs.
    print('Using cached CSVs to created a dataframe')
    
    #hashes can be removed in case of error. Used to check status. 
    sales = get_sales_df()
    #print('SALES')
    #print(sales.shape)
    #print(sales.columns)
    stores = get_stores_df()
    #print('STORES')
    #print(stores.shape)
    #print(stores.columns) 
    #print('ITEMS')
    items = get_items_df()
    #print(items.shape)
    #print(items.columns)
    
    # I went back to my previous function and renamed the columns items and sale to their appropriate ids, so now these can be merged
    print('combining sales and stores on store_id')
    #sales_stores = sales.merge(stores, how='inner', on='store_id')
    cronenberg = sales.merge(stores, on='store_id')
    
    print('combining again on item_id')
    combined_df = cronenberg.merge(items, how='inner', on='item_id')
    
    print('Dataframe ready, sending to a CSV')
    # CSV from CVS
    combined_df.to_csv('sales_stores_items.csv')
    
    return combined_df