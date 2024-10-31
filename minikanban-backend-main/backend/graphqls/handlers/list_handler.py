from supabase import create_client
import os

class ListHandler:
    def __init__(self):
        # Initialize Supabase client
        SUPABASE_URL = os.getenv("SUPABASE_URL")
        SUPABASE_KEY = os.getenv("SUPABASE_KEY")
        self.supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    def get_list(self, id):
        # Query to fetch a single list item by id
        response = self.supabase.table("Lists").select("*").eq("id", id).single().execute()
        
        # Check for errors in the response
        if response.error:
            print("Error fetching list:", response.error)
            return None
        
        # Return the item if query is successful
        return response.data

    def get_all_list(self):
        # Query to fetch all list items
        response = self.supabase.table("Lists").select("*").execute()
        
        # Check for errors in the response
        if response.error:
            print("Error fetching all lists:", response.error)
            return []
        
        # Return items if query is successful
        return response.data












# from database.dynamodb_client import get_dynamodb_client

# class ListHandler:
#     def __init__(self):
#         self.dynamodb = get_dynamodb_client(local=True)
#         self.table = self.dynamodb.Table('Lists')

#     def get_list(self, id):
#         response = self.table.get_item(Key={'id': id})
#         return response.get('Item')

#     def get_all_list(self):
#         response = self.table.scan()
#         return response['Items']
