'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Updated at: 2023-10-09
Purpose: Easily use Natural S Q L Generation Service
-----------------------------------------------------
'''
from .service import SoffosAIService
from .input_config import InputConfig
from soffosai.common.constants import ServiceString
from typing import Union



class NaturalSQLGenerationService(SoffosAIService):
    '''
    The Natural SQL Generation module converts your natural language messages into
    SQL queries that can be used to query your database. All you need to do is
    ingest the schema of your database in a defined format described below and then
    ask it to give you the data you need. The output of the module is a raw SQL
    snippet that can be executed immediately. In cases where the system cannot
    generate a relevant SQL query, it will ask for clarifications. The module can
    be set up as an interactive session by providing it all previous interactions,
    informing it better how to respond. However, unlike our chatbot module, it does
    not store the session history internally - that's something that needs to be
    done on the application level.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.NATURAL_S_Q_L_GENERATION
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, query:str=None, messages:list=None, tables:list=None, notes:list=None, classify_tables:bool=None, table_prefix:str=None, table_aliases:list=None, boost:bool=True) -> dict:
        '''
        Call the Natural S Q L Generation Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param query: None
        :param messages: A list of dictionaries representing the conversation history. Each message
            should contain the `role` key, which can be either 'user' or 'assistant'
            and the `content` key which contains the message.
        :param tables: Each item in the list represents a column. There are 2 mandatory fields
            for each dictionary: 'column': the column's name 'type': the column's data
            type Moreover, there are 3 optional parameters: 'children': This is
            applicable for Primary Key columns - the id of the object. It's a list of
            the columns that inherit from this. The format should be `<table
            name>.<column name>`. Make sure to add the correct table and column names
            to avoid mistakes in the generated SQL. 'parents': This is a list of
            columns that this specific column points to. Usually it points to the
            Primary Keys of other tables. As above, the format should be `<table
            name>.<column name>`. 'notes': This is a list of strings, where each
            string is a 'note', a piece of information that might be useful for the
            system to know. Certain things are difficult to be inferred from the
            schema alone, like relationships that are not defined by PK/FK keys, and
            datatype formats such as choice fields that have a limited set of possible
            values. Such rules are usually set by the application rather than the
            database. Therefore, we need to inform the system.
        :param notes: A list of extra information for the system. Experiment with this field to
            optimize the system for the best responses.
        :param classify_tables: When the size of your tables reaches the limit of our AI models, you'll
            get an error. By setting this to `true` it will allow the system to
            handpick the tables needed for generating the SQL without processing your
            entire schema. This may reduce the accuracy, but will overcome the input
            length limit.
        :param table_prefix: Use this field to instruct the model to prefix the names of the tables
            with the specified string. This allows you to ingest the table names
            without the prefix, and change the prefix only if needed.
        :param table_aliases: None
        :param boost: Use an enhanced version of the system that is more accurate but slower for
            an increased price when set to `true`.
        :return: messages: A list of dictionaries representing the conversation history. Each message
            should contain the `role` key, which can be either 'user' or 'assistant'
            and the `content` key which contains the message.
        boost: Use an enhanced version of the system that is more accurate but slower for
            an increased price when set to `true`.
        sql: None
        sql_count: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/natural_s_q_l_generation.py>`_
        '''
        return super().__call__(user=user, query=query, messages=messages, tables=tables, notes=notes, classify_tables=classify_tables, table_prefix=table_prefix, table_aliases=table_aliases, boost=boost)

    def set_input_configs(self, name:str, query:Union[str, InputConfig]=None, messages:Union[list, InputConfig]=None, tables:Union[list, InputConfig]=None, notes:Union[list, InputConfig]=None, classify_tables:Union[bool, InputConfig]=None, table_prefix:Union[str, InputConfig]=None, table_aliases:Union[list, InputConfig]=None, boost:Union[bool, InputConfig]=True):
        '''
        Before using a SoffosAIService into a SoffosPipeline, you must setup the service's input configuration.
        '''
        super().set_input_configs(name=name, query=query, messages=messages, tables=tables, notes=notes, classify_tables=classify_tables, table_prefix=table_prefix, table_aliases=table_aliases, boost=boost)

    @classmethod
    def call(self, user:str, query:str=None, messages:list=None, tables:list=None, notes:list=None, classify_tables:bool=None, table_prefix:str=None, table_aliases:list=None, boost:bool=True) -> dict:
        '''
        Call the Natural S Q L Generation Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param query: None
        :param messages: A list of dictionaries representing the conversation history. Each message
            should contain the `role` key, which can be either 'user' or 'assistant'
            and the `content` key which contains the message.
        :param tables: Each item in the list represents a column. There are 2 mandatory fields
            for each dictionary: 'column': the column's name 'type': the column's data
            type Moreover, there are 3 optional parameters: 'children': This is
            applicable for Primary Key columns - the id of the object. It's a list of
            the columns that inherit from this. The format should be `<table
            name>.<column name>`. Make sure to add the correct table and column names
            to avoid mistakes in the generated SQL. 'parents': This is a list of
            columns that this specific column points to. Usually it points to the
            Primary Keys of other tables. As above, the format should be `<table
            name>.<column name>`. 'notes': This is a list of strings, where each
            string is a 'note', a piece of information that might be useful for the
            system to know. Certain things are difficult to be inferred from the
            schema alone, like relationships that are not defined by PK/FK keys, and
            datatype formats such as choice fields that have a limited set of possible
            values. Such rules are usually set by the application rather than the
            database. Therefore, we need to inform the system.
        :param notes: A list of extra information for the system. Experiment with this field to
            optimize the system for the best responses.
        :param classify_tables: When the size of your tables reaches the limit of our AI models, you'll
            get an error. By setting this to `true` it will allow the system to
            handpick the tables needed for generating the SQL without processing your
            entire schema. This may reduce the accuracy, but will overcome the input
            length limit.
        :param table_prefix: Use this field to instruct the model to prefix the names of the tables
            with the specified string. This allows you to ingest the table names
            without the prefix, and change the prefix only if needed.
        :param table_aliases: None
        :param boost: Use an enhanced version of the system that is more accurate but slower for
            an increased price when set to `true`.
        :return: messages: A list of dictionaries representing the conversation history. Each message
            should contain the `role` key, which can be either 'user' or 'assistant'
            and the `content` key which contains the message.
        boost: Use an enhanced version of the system that is more accurate but slower for
            an increased price when set to `true`.
        sql: None
        sql_count: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/natural_s_q_l_generation.py>`_
        '''
        return super().call(user=user, query=query, messages=messages, tables=tables, notes=notes, classify_tables=classify_tables, table_prefix=table_prefix, table_aliases=table_aliases, boost=boost)

