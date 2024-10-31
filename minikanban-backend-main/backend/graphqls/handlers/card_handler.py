from supabase import create_client
import os

class CardHandler:
    def __init__(self):
        # Initialize Supabase client
        SUPABASE_URL = os.getenv("SUPABASE_URL")
        SUPABASE_KEY = os.getenv("SUPABASE_KEY")
        self.supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    def get_card(self, key, listId):
        # Query to fetch cards based on key and listId
        response = self.supabase.table("Cards").select("*").eq("key", key).eq("listId", listId).execute()
        
        # Check for errors in the response
        if response.error:
            print("Error fetching card:", response.error)
            return []
        
        # Return items if query is successful
        return response.data

    def get_all_card(self):
        # Query to fetch all cards
        response = self.supabase.table("Cards").select("*").execute()
        
        # Check for errors in the response
        if response.error:
            print("Error fetching all cards:", response.error)
            return []
        
        # Return items if query is successful
        return response.data




# from database.dynamodb_client import get_dynamodb_client
# from boto3.dynamodb.conditions import Attr

# class CardHandler:
#     def __init__(self):
#         self.dynamodb = get_dynamodb_client(local=True)
#         self.table = self.dynamodb.Table('Cards')

#     def get_card(self, key, listId):
#         response = self.table.scan(
#             FilterExpression=Attr('key').eq(key) & Attr('listId').eq(listId)
#         )
#         return response['Items']

#     def get_all_card(self):
#         response = self.table.scan()
#         return response['Items']
