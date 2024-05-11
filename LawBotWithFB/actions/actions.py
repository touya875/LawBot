# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import json
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import mysql.connector
import random
import pandas as pd

conn = mysql.connector.connect(host="localhost", database="db_rasa_chatbot", user="root", password="", port="3307")
print(conn)
if (conn):
    print("Connected")
else:
    print("Not connected")


class action_law_1_db(Action):
    def name(self):
        return "action_law_1_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_1'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_2_db(Action):
    def name(self):
        return "action_law_2_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_2'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_3_db(Action):
    def name(self):
        return "action_law_3_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_3'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_4_db(Action):
    def name(self):
        return "action_law_4_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_4'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_5_db(Action):
    def name(self):
        return "action_law_5_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_5'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_6_db(Action):
    def name(self):
        return "action_law_6_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_6'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_7_db(Action):
    def name(self):
        return "action_law_7_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_7'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_8_db(Action):
    def name(self):
        return "action_law_8_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_8'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_9_db(Action):
    def name(self):
        return "action_law_9_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_9'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_10_db(Action):
    def name(self):
        return "action_law_10_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_10'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_11_db(Action):
    def name(self):
        return "action_law_11_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_11'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_12_db(Action):
    def name(self):
        return "action_law_12_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_12'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_13_db(Action):
    def name(self):
        return "action_law_13_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_13'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_14_db(Action):
    def name(self):
        return "action_law_14_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_14'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_15_db(Action):
    def name(self):
        return "action_law_15_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_15'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_16_db(Action):
    def name(self):
        return "action_law_16_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_16'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_17_db(Action):
    def name(self):
        return "action_law_17_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_17'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_18_db(Action):
    def name(self):
        return "action_law_18_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_18'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_19_db(Action):
    def name(self):
        return "action_law_19_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_19'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_20_db(Action):
    def name(self):
        return "action_law_20_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_20'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_21_db(Action):
    def name(self):
        return "action_law_21_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_21'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_22_db(Action):
    def name(self):
        return "action_law_22_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_22'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_23_db(Action):
    def name(self):
        return "action_law_23_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_23'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_24_db(Action):
    def name(self):
        return "action_law_24_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_24'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_25_db(Action):
    def name(self):
        return "action_law_25_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_25'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_26_db(Action):
    def name(self):
        return "action_law_26_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_26'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_27_db(Action):
    def name(self):
        return "action_law_27_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_27'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_28_db(Action):
    def name(self):
        return "action_law_28_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_28'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_29_db(Action):
    def name(self):
        return "action_law_29_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_29'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_30_db(Action):
    def name(self):
        return "action_law_30_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_30'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_31_db(Action):
    def name(self):
        return "action_law_31_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_31'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_32_db(Action):
    def name(self):
        return "action_law_32_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_32'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_33_db(Action):
    def name(self):
        return "action_law_33_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_33'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_34_db(Action):
    def name(self):
        return "action_law_34_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_34'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_35_db(Action):
    def name(self):
        return "action_law_35_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_35'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_36_db(Action):
    def name(self):
        return "action_law_36_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_36'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_37_db(Action):
    def name(self):
        return "action_law_37_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_37'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_38_db(Action):
    def name(self):
        return "action_law_38_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_38'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_39_db(Action):
    def name(self):
        return "action_law_39_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_39'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_40_db(Action):
    def name(self):
        return "action_law_40_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_40'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_41_db(Action):
    def name(self):
        return "action_law_41_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_41'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_42_db(Action):
    def name(self):
        return "action_law_42_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_42'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_43_db(Action):
    def name(self):
        return "action_law_43_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_43'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_44_db(Action):
    def name(self):
        return "action_law_44_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_44'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_45_db(Action):
    def name(self):
        return "action_law_45_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_45'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_46_db(Action):
    def name(self):
        return "action_law_46_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_46'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_47_db(Action):
    def name(self):
        return "action_law_47_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_47'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_48_db(Action):
    def name(self):
        return "action_law_48_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_48'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_49_db(Action):
    def name(self):
        return "action_law_49_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_49'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_law_50_db(Action):
    def name(self):
        return "action_law_50_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM tbl_chatbot_responses WHERE intent_group_name = 'law_50'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

#############################
#############################

class action_tt_1_db(Action):
    def name(self):
        return "action_tt_1_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt1'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_2_db(Action):
    def name(self):
        return "action_tt_2_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt2'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_3_db(Action):
    def name(self):
        return "action_tt_3_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt3'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_4_db(Action):
    def name(self):
        return "action_tt_4_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt4'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_5_db(Action):
    def name(self):
        return "action_tt_5_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt5'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_6_db(Action):
    def name(self):
        return "action_tt_6_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt6'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_7_db(Action):
    def name(self):
        return "action_tt_7_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt7'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_8_db(Action):
    def name(self):
        return "action_tt_8_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt8'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_9_db(Action):
    def name(self):
        return "action_tt_9_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt9'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_10_db(Action):
    def name(self):
        return "action_tt_10_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt10'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_11_db(Action):
    def name(self):
        return "action_tt_11_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt11'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_12_db(Action):
    def name(self):
        return "action_tt_12_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt12'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_13_db(Action):
    def name(self):
        return "action_tt_13_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt13'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_14_db(Action):
    def name(self):
        return "action_tt_14_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt14'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_15_db(Action):
    def name(self):
        return "action_tt_15_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt15'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_16_db(Action):
    def name(self):
        return "action_tt_16_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt16'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_17_db(Action):
    def name(self):
        return "action_tt_17_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt17'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_18_db(Action):
    def name(self):
        return "action_tt_18_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt18'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_19_db(Action):
    def name(self):
        return "action_tt_19_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt19'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_20_db(Action):
    def name(self):
        return "action_tt_20_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt20'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_21_db(Action):
    def name(self):
        return "action_tt_21_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt21'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_22_db(Action):
    def name(self):
        return "action_tt_22_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt22'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_23_db(Action):
    def name(self):
        return "action_tt_23_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt23'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_24_db(Action):
    def name(self):
        return "action_tt_24_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt24'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_25_db(Action):
    def name(self):
        return "action_tt_25_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt25'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_26_db(Action):
    def name(self):
        return "action_tt_26_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt26'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_27_db(Action):
    def name(self):
        return "action_tt_27_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt27'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_28_db(Action):
    def name(self):
        return "action_tt_28_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt28'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_29_db(Action):
    def name(self):
        return "action_tt_29_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt29'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_30_db(Action):
    def name(self):
        return "action_tt_30_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt30'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_31_db(Action):
    def name(self):
        return "action_tt_31_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt31'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_32_db(Action):
    def name(self):
        return "action_tt_32_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt32'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_33_db(Action):
    def name(self):
        return "action_tt_33_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt33'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_34_db(Action):
    def name(self):
        return "action_tt_34_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt34'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_35_db(Action):
    def name(self):
        return "action_tt_35_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt35'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_36_db(Action):
    def name(self):
        return "action_tt_36_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt36'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_37_db(Action):
    def name(self):
        return "action_tt_37_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt37'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_38_db(Action):
    def name(self):
        return "action_tt_38_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt38'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_39_db(Action):
    def name(self):
        return "action_tt_39_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt39'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_40_db(Action):
    def name(self):
        return "action_tt_40_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt40'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_41_db(Action):
    def name(self):
        return "action_tt_41_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt41'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_42_db(Action):
    def name(self):
        return "action_tt_42_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt42'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_43_db(Action):
    def name(self):
        return "action_tt_43_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt43'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_44_db(Action):
    def name(self):
        return "action_tt_44_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt44'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_45_db(Action):
    def name(self):
        return "action_tt_45_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt45'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_46_db(Action):
    def name(self):
        return "action_tt_46_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt46'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_47_db(Action):
    def name(self):
        return "action_tt_47_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt47'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_48_db(Action):
    def name(self):
        return "action_tt_48_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt48'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_49_db(Action):
    def name(self):
        return "action_tt_49_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt49'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []

class action_tt_50_db(Action):
    def name(self):
        return "action_tt_50_db"

    def run(self, dispatcher, tracker, domain):
        # Get Response from Database.
        query = "SELECT chatbot_responses FROM bltt_chatbot_responses WHERE intent_tt_group_name = 'tt50'"
        responses_list = pd.read_sql_query(query, conn)

        # Randomize multiple responses.
        maxRandomNum = len(responses_list)
        randomnum = random.randint(1, maxRandomNum)
        index = randomnum - 1

        # Setting Response.
        ret = responses_list.at[index, 'chatbot_responses']
        dispatcher.utter_message(text=ret)

        # Returning Response.
        return []
#########################
#########################
class act_func(Action):

    def name(self) -> Text:
        return "act_func"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = {
            "text": "Xin chào! Em là LawBot, em sẽ giải đáp các thắc mắc của Quý khách về pháp luật hình sự",
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Hỏi đáp nội dung luật",
                    "payload": "article",

                },
                {
                    "content_type": "text",
                    "title": "Tin tức",
                    "payload": "news",
                },
                # {
                #     "content_type": "text",
                #     "title": "Liên hệ",
                #     "payload": "contact",
                # }
            ]
        }

        dispatcher.utter_message(json_message=message)

        return []


# class act_contact(Action):
#
#     def name(self) -> Text:
#         return "act_contact"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         button = {
#             "type": "phone_number",
#             "title": "Hotline",
#             "payload": "02838354409"
#         }
#
#         button1 = {
#             "type": "web_url",
#             "url": "https://www.sgu.edu.vn/",
#             "title": "Website"
#         }
#         ret_text = "Xin chào! Quý khách có thể liên lạc bằng các phương thức sau:"
#         dispatcher.utter_message(text=ret_text, buttons=[button, button1])
#
#         return []


class act_news(Action):

    def name(self) -> Text:
        return "act_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # These should be got from server , do not do like this
        news_list = []
        news0 = {
            "name": "Đại án Vạn Thịnh Phát",
            "image_url": "https://xdcs.cdnchinhphu.vn/446259493575335936/2024/4/11/anh-1-truong-my-lan-1712831251963-1712831252067443946551.jpg",
            "intro": "Tòa án nhân dân TPHCM tuyên phạt...",
            "link": "https://xaydungchinhsach.chinhphu.vn/dai-an-van-thinh-phat-truy-to-truong-my-lan-va-85-bi-can-119231215145320997.htm",

        }
        news_list.append(news0)
        news1 = {
            "name": "Chuyến bay giải cứu",
            "image_url": "https://bcp.cdnchinhphu.vn/334894974524682240/2023/4/4/2610giaicuu-16805784111661809172872.jpg",
            "intro": "Ngày 27/12, Hội đồng xét xử...",
            "link": "https://xaydungchinhsach.chinhphu.vn/tuyen-an-phuc-tham-vu-chuyen-bay-giai-cuu-119231227150743725.htm",

        }
        news_list.append(news1)
        news2 = {
            "name": "Kỳ án người phụ nữ mất tích suốt 13 năm",
            "image_url": "https://img.cand.com.vn/resize/800x800/NewFiles/Images/2023/12/28/nh_1-1703753393012.jpg",
            "intro": "Sau 13 năm mất tích bí ẩn...",
            "link": "https://cand.com.vn/Vu-an-noi-tieng/noi-am-anh-cua-ke-sat-nhan-sau-13-nam-gay-an-i718601/",

        }
        news_list.append(news2)

        template_items = []
        for news in news_list:
            template_item = {
                "title": news['name'],
                "image_url": news['image_url'],
                "subtitle": news['intro'],
                "default_action": {
                    "type": "web_url",
                    "url": news['link'],
                    "webview_height_ratio": "full"
                },
                "buttons": [
                    {
                        "type": "web_url",
                        "url": news['link'],
                        "title": "Xem ngay"
                    }
                ]
            }
            template_items.append(template_item)

        message_str = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": template_items

                }
            }
        }
        ret_text = "Quý khách có thể đọc thêm về các vụ án dưới đây:"
        print(message_str)
        dispatcher.utter_message(text=ret_text, json_message=message_str)

        return []


class act_guide(Action):

    def name(self) -> Text:
        return "act_guide"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # These should be got from server , do not do like this

        dispatcher.utter_message(text="Dữ liệu tham khảo từ các chuyên gia trong ngành và dựa trên cuốn sách:",
                                 image="https://www.nxbctqg.org.vn/img_data/images/112893832339_BL.jpg");


        return []

