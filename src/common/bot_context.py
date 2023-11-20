'''
The soffosai Python Package
'''

import typing as t
from typing import List
from typing import Union
from io import BufferedReader

SOFFOS_SERVICE_URL = "https://api.soffos.ai/service/"

class ServiceString:
    '''
    Contains the list of Soffos services as attributes
    '''
    ANSWER_SCORING = 'answer-scoring'
    AUDIO_CONVERTER = 'audio-converter'
    CHAT_BOT_CREATE = 'chatbot/create'
    CHAT_BOT = 'chatbot'
    CHAT_BOTS_GET = 'chatbot/get'
    CHAT_BOTS_DELETE = 'chatbot/delete'
    CHAT_BOT_GET_USER_SESSIONS = 'chatbot/sessions/get'
    CHAT_BOT_DELETE_USER_SESSIONS = 'chatbot/sessions/delete'
    DISCUSS_CREATE = 'discuss/create'
    DISCUSS_QUERY = 'discuss'
    DISCUSS_RETRIEVE = 'discuss/count'
    DISCUSS_DELETE = 'discuss/delete'
    DISCUSS_COUNT = 'discuss/count'
    DOCUMENTS_COUNT = 'documents/count'
    DOCUMENTS_INGEST = 'documents/ingest'
    DOCUMENTS_DELETE = 'documents/delete'
    DOCUMENTS_SEARCH = 'documents/search'
    EMAIL_ANALYSIS = 'email-analysis'
    EMOTION_DETECTION = 'emotion-detection'
    FILE_CONVERTER = 'file-converter'
    FLASHCARD_GENERATION = 'flashcard-generation'
    INTENT_CLASSIFICATION = 'intent-classification'
    LANGUAGE_DETECTION = 'language-detection'
    LOGICAL_ERROR_DETECTION = 'logical-error-detection'
    MICROLESSON = 'microlesson'
    NATURAL_S_Q_L_GENERATION = 'natural-sql-generation'
    N_E_R = 'ner'
    PARAPHRASE = 'paraphrase'
    PROFANITY = 'profanity'
    QN_A_GENERATION = 'qna-generation'
    QUESTION_ANSWERING = "question-answering"
    REVIEW_TAGGER = 'review-tagger'
    SEARCH_RECOMMENDATIONS = 'search-recommendations'
    SENTIMENT_ANALYSIS = 'sentiment-analysis'
    SIMPLIFY = 'simplify'
    STRING_SIMILARITY = 'string-similarity'
    SUMMARIZATION = 'summarization'
    TABLE_DELETE = 'natural-sql-generation/table/delete'
    TABLE_GET = 'natural-sql-generation/table/get'
    TABLE_GENERATOR = 'table-generator'
    TABLE_INGEST = 'natural-sql-generation/table/ingest/'
    TAG = 'tag'
    TRANSCRIPT_CORRECTION = 'transcript-correction'
    TRANSLATION = 'translation'
    WEBSITE_CONVERTER = 'website-converter'
    BATCH_SERVICE = 'batch-service2'


FORM_DATA_REQUIRED = [ServiceString.FILE_CONVERTER, ServiceString.AUDIO_CONVERTER]

####

class ServiceIO:
    '''
    Defines the IO of services. The structure is specifically important to determine if
    the input provided by the programmer or other service is acceptable
    '''
    service:ServiceString = None
    required_input_fields = []
    require_one_of_choice = []
    defaults = []
    input_structure = {}
    optional_input_fields = []
    output_structure = {}
    primary_output_field = None

    def __init__(self) -> None:

        self._output_fields = list(self.output_structure.keys())

        if not self.primary_output_field:
            for field in self._output_fields:
                if field != "cost" and field != "charged_character_count":
                    self.primary_output_field = field
                    break
    
    @classmethod
    def special_validation(self, payload):
        return True, None

class AnswerScoringIO(ServiceIO):
    service = ServiceString.ANSWER_SCORING
    required_input_fields = ["context","question","user_answer"]
    optional_input_fields = ["answer"]
    input_structure = {
        "context": str, 
        "question": str, 
        "answer": str, 
        "user_answer": str
    }

    output_structure = {
        "score": float,
        "reasoning": str
    }

class AudioConverterIO(ServiceIO):
    service = ServiceString.AUDIO_CONVERTER
    required_input_fields = []
    optional_input_fields = ["file","url","model"]
    input_structure = {
        # "file": (BufferedReader, str), 
        "url": str, 
        "model": str
    }

    output_structure = {
        "number_of_speakers": int,
        "transcripts": dict,
        "language": str,
        "error": str
    }


    @classmethod
    def special_validation(self, payload):
        
        if payload.get("file") and payload.get('url'):
            return False, "Please provide file or url, not both."
        
        if not payload.get("file") and not payload.get('url'):
            return False, "Please provide the auido file or url of the audio file."

        AVAILABLE_MODELS = ("whisper", "nova 2")

        if payload.get("model"):
            if (payload.get("model")).lower() not in AVAILABLE_MODELS:
                return False, "model field's value can only be 'whisper' or 'nova 2'."

        return super().special_validation(payload)

class ChatBotIO(ServiceIO):
    service = ServiceString.CHAT_BOT
    required_input_fields = ["message","chatbot_id","user_id","mode"]
    optional_input_fields = ["session_id","previous_messages","bot_document_ids","context_document_ids"]
    input_structure = {
        "session_id": str, 
        "message": str, 
        "chatbot_id": str, 
        "previous_messages": list, 
        "user_id": str, 
        "mode": str, 
        "bot_document_ids": list, 
        "context_document_ids": list
    }

    output_structure = {
        "response": str,
        "session_name": str,
        "messages": list,
        "context": str
    }

class ChatBotsDeleteIO(ServiceIO):
    service = ServiceString.CHAT_BOTS_DELETE
    required_input_fields = ["chatbot_ids"]
    optional_input_fields = []
    input_structure = {
        "chatbot_ids": list
    }

    output_structure = {
        "success": bool
    }

class ChatBotsGetIO(ServiceIO):
    service = ServiceString.CHAT_BOTS_GET
    required_input_fields = []
    optional_input_fields = ["chatbot_ids"]
    input_structure = {
        "chatbot_ids": list
    }

    output_structure = {
        "chatbots": list
    }

class ChatBotCreateIO(ServiceIO):
    service = ServiceString.CHAT_BOT_CREATE
    required_input_fields = ["role","chatbot_name"]
    optional_input_fields = ["chatbot_id"]
    input_structure = {
        "role": str, 
        "chatbot_name": str, 
        "chatbot_id": str
    }

    output_structure = {
        "chatbot_id": str
    }

class ChatBotDeleteUserSessionsIO(ServiceIO):
    service = ServiceString.CHAT_BOT_DELETE_USER_SESSIONS
    required_input_fields = ["chatbot_id","user_id"]
    optional_input_fields = ["session_ids"]
    input_structure = {
        "chatbot_id": str, 
        "user_id": str, 
        "session_ids": list
    }

    output_structure = {
        "success": bool
    }

class ChatBotGetUserSessionsIO(ServiceIO):
    service = ServiceString.CHAT_BOT_GET_USER_SESSIONS
    required_input_fields = ["chatbot_id","user_id"]
    optional_input_fields = ["session_ids"]
    input_structure = {
        "chatbot_id": str, 
        "user_id": str, 
        "session_ids": list
    }

    output_structure = {
        "sessions": dict
    }

class DiscussCountIO(ServiceIO):
    service = ServiceString.DISCUSS_COUNT
    required_input_fields = ["return_messages"]
    optional_input_fields = []
    input_structure = {
        "return_messages": bool
    }

    output_structure = {
        "sessions": list,
        "session_count": int
    }

class DiscussCreateIO(ServiceIO):
    service = ServiceString.DISCUSS_CREATE
    required_input_fields = ["context"]
    optional_input_fields = []
    input_structure = {
        "context": str
    }

    output_structure = {

    }

class DiscussDeleteIO(ServiceIO):
    service = ServiceString.DISCUSS_DELETE
    required_input_fields = []
    optional_input_fields = ["session_ids"]
    input_structure = {
        "session_ids": list
    }

    output_structure = {
        "success": bool
    }

class DiscussQueryIO(ServiceIO):
    service = ServiceString.DISCUSS_QUERY
    required_input_fields = ["query"]
    optional_input_fields = []
    input_structure = {
        "query": str
    }

    output_structure = {
        "response": str,
        "context": str,
        "messages": list
    }

class DocumentsCountIO(ServiceIO):
    service = ServiceString.DOCUMENTS_COUNT
    required_input_fields = []
    optional_input_fields = ["filters","date_from","date_until"]
    input_structure = {
        "filters": dict, 
        "date_from": str, 
        "date_until": str
    }

    output_structure = {
        "documents": dict,
        "count": int
    }

class DocumentsDeleteIO(ServiceIO):
    service = ServiceString.DOCUMENTS_DELETE
    required_input_fields = ["document_ids"]
    optional_input_fields = []
    input_structure = {
        "document_ids": list
    }

    output_structure = {
        "success": bool
    }

class DocumentsIngestIO(ServiceIO):
    service = ServiceString.DOCUMENTS_INGEST
    required_input_fields = []
    optional_input_fields = ["document_id","meta","document_name","text","tagged_elements"]
    input_structure = {
        "document_id": str, 
        "meta": dict, 
        "document_name": str, 
        "text": str, 
        "tagged_elements": list
    }

    output_structure = {
        "document_id": str,
        "success": bool,
        "filtered": dict
    }


    @classmethod
    def special_validation(self, payload):
        

        if payload.get('text') is not None and payload.get('tagged_elements') is not None:
            return False, 'Only one of "text" and "tagged_elements" can be provided.'
        if not payload.get('text') and not payload.get('tagged_elements'):
            return False, 'No "text" or "tagged_elements" were provided.'
        if payload.get('tagged_elements'):
            for i, elem_dict in enumerate(payload['tagged_elements']):
                # Validate that "text" is present
                if 'text' not in elem_dict:
                    return False, '"tagged_elements" data is corrupted. '\
                        f'Element at index {i} has no attribute "text".'
                # Validate that "tag" is present
                if 'tag' not in elem_dict:
                    return False, '"tagged_elements" data is corrupted. '\
                        f'Element at index {i} has no attribute "tag".'
                # Validate that "text" is a string
                if not isinstance(elem_dict.get('text'), str):
                    return False, '"tagged_elements" data is corrupted. '\
                        f'Field "text" type is not a string in element at index {i}.'
                # Validate that "tag" is a sting
                if not isinstance(elem_dict.get('tag'), str):
                    return False, '"tagged_elements" data is corrupted. '\
                        f'Field "tag" type is not a string in element at index {i}.'
                if 'heading' not in elem_dict['tag'] and elem_dict['tag'] != 'title':
                    # Validate that non heading elements have a "headings" field
                    if 'headings' not in elem_dict:
                        return False, '"tagged_elements" data is corrupted. ' \
                            f'Element at index {i} has no attribute "headings"'
                    # Validate that "headings" fields contain the right data
                    for heading in elem_dict.get('headings'):
                        if 'text' not in heading:
                            return False, '"tagged_elements" data is corrupted. '\
                                f'Heading in element at index {i} has no attribute "text".'
                        # Validate that "tag" is present
                        if 'tag' not in heading:
                            return False, '"tagged_elements" data is corrupted. '\
                                f'Heading in element at index {i} has no attribute "tag".'
                        # Validate that "text" is a string
                        if not isinstance(heading.get('text'), str):
                            return False, '"tagged_elements" data is corrupted. '\
                                f'Field "text" type is not a string in heading of element at index {i}.'
                        # Validate that "tag" is a sting
                        if not isinstance(heading.get('tag'), str):
                            return False, '"tagged_elements" data is corrupted. '\
                                f'Field "tag" type is not a string in heading of element at index {i}.'

        return super().special_validation(payload)

class DocumentsSearchIO(ServiceIO):
    service = ServiceString.DOCUMENTS_SEARCH
    required_input_fields = []
    optional_input_fields = ["query","document_ids","top_n_keyword","top_n_natural_language","filters","date_from","date_until"]
    input_structure = {
        "query": str, 
        "document_ids": list, 
        "top_n_keyword": int, 
        "top_n_natural_language": int, 
        "filters": dict, 
        "date_from": str, 
        "date_until": str
    }

    output_structure = {
        "passages": list
    }

class EmailAnalysisIO(ServiceIO):
    service = ServiceString.EMAIL_ANALYSIS
    required_input_fields = ["text"]
    optional_input_fields = []
    input_structure = {
        "text": str
    }

    output_structure = {
        "analysis": dict
    }

class EmotionDetectionIO(ServiceIO):
    service = ServiceString.EMOTION_DETECTION
    required_input_fields = ["text","sentence_split","sentence_overlap"]
    optional_input_fields = ["emotion_choices"]
    input_structure = {
        "text": str, 
        "sentence_split": int, 
        "sentence_overlap": bool, 
        "emotion_choices": list
    }

    output_structure = {
        "spans": dict
    }

    @classmethod
    def special_validation(self, payload):
        
        choices = ['joy','trust','fear','surprise','sadness','disgust','anger','anticipation']

        if payload["sentence_split"] == 1 and payload["sentence_overlap"] == True:
            return False, 'Value "sentence_overlap" must be false when "sentence_split" is set to 1.'
        
        if 'emotion_choices' in payload:
            unsupported_emotion = []
            for emotion in payload['emotion_choices']:
                if emotion not in choices:
                    unsupported_emotion.append(emotion)
            if len(unsupported_emotion) > 0:
                return False, f'unsupported emotions: [{", ".join(unsupported_emotion)}].'
            
        payload['sentence_overlap'] = 1 if payload['sentence_overlap'] else 0

        return super().special_validation(payload)

class FileConverterIO(ServiceIO):
    service = ServiceString.FILE_CONVERTER
    required_input_fields = ["file","normalize"]
    optional_input_fields = []
    input_structure = {
        # "file": (BufferedReader, str), 
        "normalize": str
    }

    output_structure = {
        "normalize": str,
        "text": str,
        "tagged_elements": dict,
        "normalized_text": str,
        "normalized_tagged_elements": dict
    }

class LanguageDetectionIO(ServiceIO):
    service = ServiceString.LANGUAGE_DETECTION
    required_input_fields = ["text"]
    optional_input_fields = []
    input_structure = {
        "text": str
    }

    output_structure = {
        "language": dict
    }

class LogicalErrorDetectionIO(ServiceIO):
    service = ServiceString.LOGICAL_ERROR_DETECTION
    required_input_fields = ["text"]
    optional_input_fields = []
    input_structure = {
        "text": str
    }

    output_structure = {
        "logical_errors": dict
    }

class MicrolessonIO(ServiceIO):
    service = ServiceString.MICROLESSON
    required_input_fields = ["content"]
    optional_input_fields = []
    input_structure = {
        "content": list
    }

    output_structure = {
        "microlesson": dict
    }


    @classmethod
    def special_validation(self, payload):
        
        for i, d in enumerate(payload['content']):
            if 'source' not in d:
                return False, f"'source' field missing from element at index {i} in 'content'."
            elif not isinstance(d['source'], str):
                return False, f"'source' field at index {i} in 'content' has wrong type. Expecting str."
            if 'text' not in d:
                return False, f"'text' field missing from element at index {i} in 'content'."
            elif not isinstance(d['text'], str):
                return False, f"'text' field at index {i} in 'content' has wrong type. Expecting str."

        return super().special_validation(payload)

class NERIO(ServiceIO):
    service = ServiceString.N_E_R
    required_input_fields = ["text"]
    optional_input_fields = ["labels"]
    input_structure = {
        "text": str, 
        "labels": dict
    }

    output_structure = {
        "named_entities": list,
        "entity_counts": list
    }

class NaturalSQLGenerationIO(ServiceIO):
    service = ServiceString.NATURAL_S_Q_L_GENERATION
    required_input_fields = []
    optional_input_fields = ["query","messages","tables","notes","classify_tables","table_prefix","table_aliases","boost"]
    input_structure = {
        "query": str, 
        "messages": list, 
        "tables": list, 
        "notes": list, 
        "classify_tables": bool, 
        "table_prefix": str, 
        "table_aliases": list, 
        "boost": bool
    }

    output_structure = {
        "messages": list,
        "boost": bool,
        "sql": str,
        "sql_count": str
    }

    @classmethod
    def special_validation(self, payload):
        
        if payload.get('query') and payload.get('messages'):
            return False, 'Only one of "messages" and "query" can be provided.'
        if not payload.get('query') and not payload.get('messages'):
            return False, 'Please provide either "messages" or "query".'

        return super().special_validation(payload)

class ParaphraseIO(ServiceIO):
    service = ServiceString.PARAPHRASE
    required_input_fields = ["text"]
    optional_input_fields = []
    input_structure = {
        "text": str
    }

    output_structure = {
        "paraphrase": str,
    }

class ProfanityIO(ServiceIO):
    service = ServiceString.PROFANITY
    required_input_fields = ["text"]
    optional_input_fields = []
    input_structure = {
        "text": str
    }

    output_structure = {
        "profanities": list,
        "offensive_probability": float,
        "offensive_prediction": bool
    }

class QnAGenerationIO(ServiceIO):
    service = ServiceString.QN_A_GENERATION
    required_input_fields = ["text"]
    optional_input_fields = ["sentence_split","sentence_overlap"]
    input_structure = {
        "text": str, 
        "sentence_split": int, 
        "sentence_overlap": bool
    }

    output_structure = {
        "qna_list": dict,
        "chunks": dict
    }


    @classmethod
    def special_validation(self, payload):
        
        if payload["sentence_split"] == 1 and payload["sentence_overlap"] == True:
            return False, 'Value "sentence_overlap" must be false when "sentence_split" is set to 1.'

        return super().special_validation(payload)

class QuestionAnsweringIO(ServiceIO):
    service = ServiceString.QUESTION_ANSWERING
    required_input_fields = ["message"]
    optional_input_fields = ["document_text","document_ids","check_ambiguity","check_query_type","generic_response","meta","message_id"]
    input_structure = {
        "message": str, 
        "document_text": str, 
        "document_ids": list, 
        "check_ambiguity": bool, 
        "check_query_type": bool, 
        "generic_response": bool, 
        "meta": dict, 
        "message_id": str
    }

    output_structure = {
        "message_id": str,
        "answer": str,
        "context": str,
        "valid_query": bool,
        "no_answer": bool,
        "highlights": dict,
        "passages": dict
    }

    @classmethod
    def special_validation(self, payload):
        
        document_text: t.Optional[str] = payload.get('document_text')
        document_ids: t.Optional[t.List[str]] = payload.get('document_ids')
        client_id: t.Optional[str] = payload.get('client_id')

        # Validate only 1 of the 3 document fields are supplied.
        if sum(
            0 if document_field is None else 1
            for document_field in [document_text, document_ids]
        ) != 1:
            return False, 'Only 1 of document_text, document_ids must be provided.'

        # Validate all ids are provided.
        if document_ids is not None:
            if client_id is None:
                return False, 'client_id required'

        return super().special_validation(payload)

class ReviewTaggerIO(ServiceIO):
    service = ServiceString.REVIEW_TAGGER
    required_input_fields = ["text"]
    optional_input_fields = []
    input_structure = {
        "text": str
    }

    output_structure = {
        "object": str,
        "action": str,
        "fault": str
    }

class SearchRecommendationsIO(ServiceIO):
    service = ServiceString.SEARCH_RECOMMENDATIONS
    required_input_fields = ["text","document_ids"]
    optional_input_fields = []
    input_structure = {
        "text": str, 
        "document_ids": list
    }

    output_structure = {
        "recommendations": dict,
        "recommendations_no_info": dict
    }

class SentimentAnalysisIO(ServiceIO):
    service = ServiceString.SENTIMENT_ANALYSIS
    required_input_fields = ["text"]
    optional_input_fields = ["sentence_split","sentence_overlap"]
    input_structure = {
        "text": str, 
        "sentence_split": int, 
        "sentence_overlap": bool
    }

    output_structure = {
        "sentiment_breakdown": dict,
        "sentiment_overall": dict,
        "sentiment": str
    }

    @classmethod
    def special_validation(self, payload):
        
        if payload["sentence_split"] == 1 and payload["sentence_overlap"] == True:
            return False, 'Value "sentence_overlap" must be false when "sentence_split" is set to 1.'

        return super().special_validation(payload)

class SimplifyIO(ServiceIO):
    service = ServiceString.SIMPLIFY
    required_input_fields = ["text"]
    optional_input_fields = []
    input_structure = {
        "text": str
    }

    output_structure = {
        "simplify": str
    }

class StringSimilarityIO(ServiceIO):
    service = ServiceString.STRING_SIMILARITY
    required_input_fields = ["a","b"]
    optional_input_fields = []
    input_structure = {
        "a": str, 
        "b": str
    }

    output_structure = {
        "score": float,
        "text_spans": dict
    }

class SummarizationIO(ServiceIO):
    service = ServiceString.SUMMARIZATION
    required_input_fields = ["text","sent_length"]
    optional_input_fields = []
    input_structure = {
        "text": str, 
        "sent_length": int
    }

    output_structure = {
        "summary": str
    }

    @classmethod
    def special_validation(self, payload):
        
        if payload.get('sent_length'):
            if payload['sent_length'] > payload['text'].count("."):
                return False, 'Provided "sent_length" value is larger than the number of sentences in the input text.'

        return super().special_validation(payload)

class TableDeleteIO(ServiceIO):
    service = ServiceString.TABLE_DELETE
    required_input_fields = ["table_ids"]
    optional_input_fields = []
    input_structure = {
        "table_ids": list
    }

    output_structure = {
        "success": bool
    }

class TableGeneratorIO(ServiceIO):
    service = ServiceString.TABLE_GENERATOR
    required_input_fields = ["text","table_format"]
    optional_input_fields = ["topic"]
    input_structure = {
        "text": str, 
        "table_format": str, 
        "topic": str
    }

    output_structure = {
        "tables": dict
    }

class TableGetIO(ServiceIO):
    service = ServiceString.TABLE_GET
    required_input_fields = []
    optional_input_fields = []
    input_structure = {

    }

    output_structure = {
        "tables": list
    }

class TableIngestIO(ServiceIO):
    service = ServiceString.TABLE_INGEST
    required_input_fields = ["table","document_name","description"]
    optional_input_fields = []
    input_structure = {
        "table": list, 
        "document_name": str, 
        "description": str
    }

    output_structure = {
        "table_id": str
    }

class TagIO(ServiceIO):
    service = ServiceString.TAG
    required_input_fields = ["text"]
    optional_input_fields = ["types","n"]
    input_structure = {
        "text": str, 
        "types": str, 
        "n": int
    }

    output_structure = {
        "tags": dict
    }

class TranscriptCorrectionIO(ServiceIO):
    service = ServiceString.TRANSCRIPT_CORRECTION
    required_input_fields = ["text"]
    optional_input_fields = []
    input_structure = {
        "text": str
    }

    output_structure = {
        "corrected": str
    }

class TranslationIO(ServiceIO):
    service = ServiceString.TRANSLATION
    required_input_fields = ["text"]
    optional_input_fields = ["auto_detect","source_language_code","target_language_code"]
    input_structure = {
        "text": str, 
        "auto_detect": bool, 
        "source_language_code": str, 
        "target_language_code": str
    }

    output_structure = {
        "target_language_code": str,
        "translation": dict
    }

    @classmethod
    def special_validation(self, payload):\

        if payload.get("auto_detect") and payload.get("source_language_code"):
            return False, "When specifying a \"source_language_code\", set \"auto_detect\" to false. Note that enabling \"auto_detect\" incurs extra costs."
        if not payload.get("auto_detect") and not payload.get("source_language_code"):
            return False, "Please specify a \"source_language_code\". Otherwise, set \"auto_detect\" to True."
        if payload.get("target_language_code") and payload.get("source_language_code"):
            if payload["target_language_code"] == payload["source_language_code"]:
                return False, "Source and target language code can not be the same."

        return super().special_validation(payload)

class WebsiteConverterIO(ServiceIO):
    service = ServiceString.WEBSITE_CONVERTER
    required_input_fields = ["url"]
    optional_input_fields = []
    input_structure = {
        "url": str
    }

    output_structure = {
        "text": str,
        "links": dict
    }

SERVICE_IO_MAP = {
    'answer-scoring': AnswerScoringIO, 
    'audio-converter': AudioConverterIO, 
    'chatbot/create': ChatBotCreateIO, 
    'chatbot/sessions/delete': ChatBotDeleteUserSessionsIO, 
    'chatbot': ChatBotIO, 
    'chatbot/delete': ChatBotsDeleteIO, 
    'chatbot/get': ChatBotsGetIO, 
    'discuss/count': DiscussCountIO, 
    'discuss/create': DiscussCreateIO, 
    'discuss/delete': DiscussDeleteIO, 
    'discuss': DiscussQueryIO, 
    'documents/count': DocumentsCountIO, 
    'documents/delete': DocumentsDeleteIO, 
    'documents/ingest': DocumentsIngestIO, 
    'documents/search':DocumentsSearchIO, 
    'email-analysis': EmailAnalysisIO, 
    'emotion-detection': EmotionDetectionIO, 
    'file-converter': FileConverterIO, 
    'language-detection': LanguageDetectionIO, 
    'logical-error-detection': LogicalErrorDetectionIO, 
    'microlesson': MicrolessonIO, 
    'ner': NERIO, 
    'paraphrase': ParaphraseIO, 
    'profanity': ProfanityIO, 
    'qna-generation': QnAGenerationIO, 
    'question-answering': QuestionAnsweringIO, 
    'review-tagger': ReviewTaggerIO, 
    'search-recommendations': SearchRecommendationsIO, 
    'sentiment-analysis': SentimentAnalysisIO, 
    'simplify': SimplifyIO, 
    'string-similarity': StringSimilarityIO, 
    'summarization': SummarizationIO, 
    'natural-sql-generation/table/delete': TableDeleteIO, 
    'table-generator': TableGeneratorIO, 
    'natural-sql-generation/table/get': TableGetIO, 
    'natural-sql-generation/table/ingest/': TableIngestIO, 
    'tag': TagIO, 
    'transcript-correction': TranscriptCorrectionIO, 
    'translation': TranslationIO, 
    'website-converter': WebsiteConverterIO
}

import inspect
import soffosai
import io
import abc, requests, os, mimetypes, uuid

visit_docs_message = "Kindly visit https://platform.soffos.ai/playground/docs#/ for guidance."
input_structure_message = "To learn what the input dictionary should look like, access it by <your_service_instance>.input_structure"


def inspect_arguments(func, *args, **kwargs):
    '''
    Given a function, args and kwargs: 
    create a dictionary with keys as the arg names and values as the arg values
    '''
    # Get the list of argument names
    sig = inspect.signature(func)
    arg_names = list(sig.parameters.keys())

    # Combine positional arguments and keyword arguments
    bound_args = sig.bind(*args, **kwargs)
    bound_args.apply_defaults()
    combined_args = bound_args.arguments

    # Filter out positional arguments not present in arg_names
    arguments = {name: combined_args[name] for name in arg_names if name in combined_args}
    unziped_kwargs = {}
    for key,value in arguments.items():
        if key != "kwargs":
            if value != None:
                unziped_kwargs[key] = value
        else:
            for key2, value2 in arguments['kwargs'].items():
                if value2 != None:
                    unziped_kwargs[key2] = value2
    
    if unziped_kwargs.get('name'):
        unziped_kwargs.pop('name')

    return unziped_kwargs


def format_uuid(uuid):
    formatted_uuid = '-'.join([
        uuid[:8],
        uuid[8:12],
        uuid[12:16],
        uuid[16:20],
        uuid[20:]
    ])
    return formatted_uuid


def is_valid_uuid(uuid_string):
    if isinstance(uuid_string, type): # coming from pipeline validation, always True because it will come from Soffos Services
        return True

    if "-" not in uuid_string:
        formatted_uuid = format_uuid(uuid_string)
    else:
        formatted_uuid = uuid_string
    try:
        uuid_obj = uuid.UUID(formatted_uuid)
    except ValueError:
        return False
    return str(uuid_obj) == formatted_uuid


class SoffosAIService:
    '''
    Base service class for all Soffos Services
    '''
    def __init__(self, service:str, **kwargs) -> None:            
        if kwargs.get("apikey"):
            apikey = kwargs['apikey']
        else:
            apikey = soffosai.api_key
            
        self.headers = {
            "x-api-key": apikey,
        }
        self._apikey = apikey
        self._service = service
        self._serviceio:ServiceIO = SERVICE_IO_MAP.get(service)
        # In a pipeline, some payload properties are constants and should be related to the Service's instance
        self._payload = {}
        self.name = None # name is required if called in a pipeline


    @property
    def input_structure(self):
        '''
        These are the valid fields of the src dictionary for this service. Take note that some of the fields should not exist at the same time.
        To view fields that cannot co-exist, access the 'choose_one' property.
        '''
        return self._serviceio.input_structure
    

    @property
    def choose_one(self):
        '''
        These keys cannot co-exist in this service's src.
        '''
        return self._serviceio.require_one_of_choice


    def validate_payload(self, payload):
        '''
        checks if the input type is allowed for the service
        '''
        if not isinstance(payload, dict):
            raise TypeError("payload should be a dictionary")

        # check for missing arguments
        user_from_src = payload.get('user')
        if not user_from_src:
            return False, f"{self._service}: user key is required in the payload"

        if len(self._serviceio.required_input_fields) > 0:
            missing_requirements = []
            for required in self._serviceio.required_input_fields:
                if required not in payload:
                    missing_requirements.append(required)
            if len(missing_requirements) > 0:
                return False, f"{self._service}: Please provide {missing_requirements} on your payload. {visit_docs_message}. {input_structure_message}"
        
        if len(self._serviceio.require_one_of_choice) > 0:
            group_error = []
            for group in self._serviceio.require_one_of_choice:
                found_choices = []
                for choice in group:
                    if choice in payload:
                        found_choices.append(choice)
                if len(found_choices) == 0:
                    group_error.append(f"{self._service}: Please provide one of these values on your payload: {group}")
                elif len(found_choices) > 1:
                    group_error.append(f"{self._service}: Please only include one of these values: {group}")
            
            if len(group_error) > 0:
                return False, group_error

        # check if payload has proper type:
        input_structure = self._serviceio.input_structure
        value_errors = []
        for key, value in payload.items():
            if key in input_structure.keys():

                if isinstance(input_structure[key], tuple):
                    allowed_types = input_structure[key]
                    allowed_types_str = "or ".join([t.__name__ for t in allowed_types])
                    if type(value) not in allowed_types:
                        value_errors.append(f"{key} can have {allowed_types_str} but {type(value)} is provided")
                else:
                    if not isinstance(input_structure[key], type):
                        input_type = type(input_structure[key])
                    else:
                        input_type = input_structure[key]

                    if not isinstance(value, input_type) and value != input_type: # the second condition is for pipeline
                        wrong_type = value if isinstance(value, type) else type(value)
                        value_errors.append(f"{key} requires {input_structure[key]} but {wrong_type} is provided.")
        
        special_validation_passed, error_on_special_validation = self._serviceio.special_validation(payload)
        if not special_validation_passed:
            value_errors.append(error_on_special_validation)
        if len(value_errors) > 0:
            return False, value_errors

        if "document_ids" in payload:
            if isinstance(payload['document_ids'], list):
                for _id in payload["document_ids"]:
                    valid_uuid = is_valid_uuid(_id)
                    if not valid_uuid:
                        return False, f"{_id} is invalid document_id"
        
        return True, None


    def get_data(self, payload):
        '''
        Prepare the json or form data input of the service
        '''
        
        request_data = {}
        for key, value in payload.items():
            if key != 'file':
                request_data[key] = value

        return request_data


    def handle_file(self, file_stream, filename, mime_type):
        # Using read(), seek() and other file like object operations on file_stream 
        buffer = file_stream.read()
        file_stream.seek(0)  # it's a good practice to reset the file pointer
        stream = io.BytesIO(buffer)
        file_tuple = (filename, stream, mime_type)
        return file_tuple


    def get_response(self, payload:dict={}) -> dict:
        '''
        Based on the knowledge/context, Soffos AI will now give you the data you need
        '''
        allow_input, message = self.validate_payload(payload)
        if "question" in payload.keys(): # the api receives the question as message.
            payload['message'] = payload['question']

        if not allow_input:
            raise ValueError(message)
        
        if not self._service:
            raise ValueError("Please provide the service you need from Soffos AI.")

        response = None
        data = self.get_data(payload)
        apikey = payload.get("apikey")
        if apikey:
            self.headers["x-api-key"] = apikey
            payload.pop("apikey")

        if self._service not in FORM_DATA_REQUIRED:
            self.headers["content-type"] = "application/json"
            try:
                response = requests.post(
                    url = SOFFOS_SERVICE_URL + self._service + "/",
                    headers = self.headers,
                    json = data,
                    timeout = 120
                )
                response.raise_for_status()
            except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, 
                    requests.exceptions.Timeout, requests.exceptions.RequestException) as err:
                return_value = {
                    "status": 'Error',
                    "error": str(err)
                }
                try:
                    return_value['detail'] = response.text
                except AttributeError:
                    pass
                return return_value
            
        else:
            file_obj = payload.get('file')
            if isinstance(file_obj, str):
                filename = str(os.path.basename(file_obj))
                mime_type, _ = mimetypes.guess_type(file_obj)
                with open(file_obj, 'rb') as file:
                    files = {
                        "file": (filename, file, mime_type)
                    }
                    try:
                        response = requests.post(
                            url = SOFFOS_SERVICE_URL + self._service + "/",
                            headers = self.headers,
                            data = data,
                            files = files,
                            timeout=120
                        )
                        response.raise_for_status()
                    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, 
                            requests.exceptions.Timeout, requests.exceptions.RequestException) as err:
                        return {
                            "status": 'Error',
                            "error": str(err)
                        }

            else:
                if hasattr(file_obj, "filename"): # handle Flask and Fast API
                    filename = file_obj.filename
                elif hasattr(file_obj, "name"): # django. Flask also have name attribute so we checked filename first
                    filename = file_obj.name
                mime_type, _ = mimetypes.guess_type(filename)
                files = {'file': (filename, file_obj, mime_type)}
                try:
                    response = requests.post(
                        url = SOFFOS_SERVICE_URL + self._service + "/",
                        headers = self.headers,
                        data = data,
                        files = files,
                        timeout=120
                    )
                    response.raise_for_status()
                except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, 
                        requests.exceptions.Timeout, requests.exceptions.RequestException) as err:
                    return {
                        "status": 'Error',
                        "error": str(err)
                    }
        
        if response.ok:
            return response.json()
        else:
            return {
                "status": response.status_code,
                "error": response.text
            }


    def clean_payload(self, raw_payload):
        payload = {}
        if len(raw_payload) == 0:
            raise ValueError("There is no payload")

        for k, v in raw_payload.items():
            if v != None: # if the value is None, we don't pass it to the payload
                payload[k] = v
                if k == "document_name" or k == "chatbot_name":
                    payload["name"] = v
                elif k == "question":
                    payload['message'] = v
        
        return payload


    def __call__(self, **kwargs:dict)->dict:
        payload = self.clean_payload(kwargs)
        return self.get_response(payload=payload)


    @classmethod
    def call(cls, **kwargs):
        instance = cls()
        payload = instance.clean_payload(kwargs)
        return instance.get_response(payload)


    def __str__(self) -> str:
        return self._service


    @abc.abstractmethod
    def provide_output_type(self):
        '''
        Sends back the output datatype of the service
        '''
    

    @abc.abstractmethod
    def provide_source_type(self):
        '''
        Sends back the accepted source datatype of the service
        '''


    @abc.abstractmethod
    def get_default_output_key(self):
        '''
        Sends back the output type of the service
        '''

    def set_input_configs(self, name, **source):
        '''
        Before using a SoffosAIService into a SoffosPipeline, you must setup the service's input configuration.
        '''
        self.name = name
        self.source = source

class InputConfig:
    '''
    Input Configuration for Pipeline Nodes.
    When sequencing Nodes within a Pipeline this helps configure which Node's output is used as
    which Node's input.
    '''

    def __init__(self, source:str, field:str, pre_process:callable=None):
        """
        :param source: The name of the SoffosAIService or SoffosPipeline from \
            where the input of the current SoffosAIService should be taken from.\
            It can also be "user_input" if the input will come from the user and \
            not from a Service/SoffosPipeline.
        :param field: The name of the output field of the "source".
        :param pre_process (optional): A function to preprocess the data from source[field].
        """
        self.source = source
        self.field = field
        self.pre_process = pre_process
        if pre_process:
            if not callable(pre_process):
                raise TypeError("pre_process should be callable.")



class AnswerScoringService(SoffosAIService):
    '''
    This module will mark the user's answer based on the provided context, the
    question and, optionally, the expected correct answer. Typical string
    similarity methods often fail to accurately capture the similarity in meaning
    and semantics, especially in cases where a single word can alter the entire
    meaning of a sentence. This module not only addresses this issue, but the fact
    that the underlying AI understands the context and question also enables it to
    evaluate an answer even if the expected correct answer is not provided.
    However, when provided, the evaluation will give it more weight than the
    information in the context. The score is a value between 0 and 1, with 0 being
    completely wrong and 1 being perfectly accurate. Additionally, the reasoning
    behind the score is provided. The Answer Scoring module is a perfect fit to
    supplement the Q&A generation module by marking users' answers to AI-generated
    question-answer pairs. Together they can power a wide range of educational and
    retention-assessment applications.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.ANSWER_SCORING
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, context:str, question:str, user_answer:str, answer:str=None) -> dict:
        '''
        Call the Answer Scoring Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param context: This should be the passage with the information that is related to the
            question and answer.
        :param question: The question to answer.
        :param user_answer: The user's answer which will be marked.
        :param answer: Optionally provide the expected answer.
        :return: score: A value between 0 and 1 indicating the correctness of the answer.
        reasoning: A concise explanation of how the AI arrived to the predicted score.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/answer_scoring.py>`_
        '''
        return super().__call__(user=user, context=context, question=question, user_answer=user_answer, answer=answer)

    def set_input_configs(self, name:str, context:Union[str, InputConfig], question:Union[str, InputConfig], user_answer:Union[str, InputConfig], answer:Union[str, InputConfig]=None):
        super().set_input_configs(name=name, context=context, question=question, user_answer=user_answer, answer=answer)

    @classmethod
    def call(self, user:str, context:str, question:str, user_answer:str, answer:str=None) -> dict:
        '''
        Call the Answer Scoring Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param context: This should be the passage with the information that is related to the
            question and answer.
        :param question: The question to answer.
        :param user_answer: The user's answer which will be marked.
        :param answer: Optionally provide the expected answer.
        :return: score: A value between 0 and 1 indicating the correctness of the answer.
        reasoning: A concise explanation of how the AI arrived to the predicted score.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/answer_scoring.py>`_
        '''
        return super().call(user=user, context=context, question=question, user_answer=user_answer, answer=answer)


class AudioConverterService(SoffosAIService):
    '''
    Transcribes the given audio. It also detects the language, detects number of
    speakers, and diarizes. "file" or "url" is required, but not both should be
    provided.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.AUDIO_CONVERTER
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, file:Union[str, BufferedReader]=None, url:str=None, model:str=None) -> dict:
        '''
        Call the Audio Converter Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param file: The audio file to be transcribed.
        :param url: The location of the audio file to be transcribed. Make sure it can be
            accessed publicly. If not, include the athentication strings of the url.
        :param model: The model to be used by the audio converter. Can be 'nova 2' or 'whisper'.
            Defaults to 'nova 2'.
        :return: number_of_speakers: The number of speakers detected.
        transcripts: The transcription of the audio file or url.
        language: The detected language used by the speakers.
        error: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/audio_converter.py>`_
        '''
        return super().__call__(user=user, file=file, url=url, model=model)

    def set_input_configs(self, name:str, file:Union[str, BufferedReader, InputConfig]=None, url:Union[str, InputConfig]=None, model:Union[str, InputConfig]=None):
        super().set_input_configs(name=name, file=file, url=url, model=model)

    @classmethod
    def call(self, user:str, file:Union[str, BufferedReader]=None, url:str=None, model:str=None) -> dict:
        '''
        Call the Audio Converter Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param file: The audio file to be transcribed.
        :param url: The location of the audio file to be transcribed. Make sure it can be
            accessed publicly. If not, include the athentication strings of the url.
        :param model: The model to be used by the audio converter. Can be 'nova 2' or 'whisper'.
            Defaults to 'nova 2'.
        :return: number_of_speakers: The number of speakers detected.
        transcripts: The transcription of the audio file or url.
        language: The detected language used by the speakers.
        error: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/audio_converter.py>`_
        '''
        return super().call(user=user, file=file, url=url, model=model)


class ChatBotService(SoffosAIService):
    '''
    The Chatbot module enables you to create custom chatbots. You can give it a
    name, a purpose and connect it to your document repository so that it informs
    its responses to users from your ingested documents.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.CHAT_BOT
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, message:str, chatbot_id:str, user_id:str, mode:str, session_id:str=None, previous_messages:list=None, bot_document_ids:list=None, context_document_ids:list=None) -> dict:
        '''
        Call the Chat Bot Service
        
        :param user: The ID of the user accessing the Soffos API.
            This string will be used for throttling and profanity tracking.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        :param message: The user's message to the chatbot
        :param chatbot_id: The chatbot's id.
        :param user_id: A unique user id. It is recommended that your provide a UUID.
        :param mode: The value can only be one of: open, closed, hybrid.
        :param session_id: A unique session id for mapping the records to your application.
            It is recommended that you provide a UUID. If not provided, the
            system will not store any information regarding the call and
            will use the value of "previous_messages" as the conversation
            history.
        :param previous_messages: This field can be used to provide the conversation history. It
            is ignored if a "session_id" is provided, in which case the
            system will used the stored interactions from that session as
            conversation history.
        :param bot_document_ids: Here you can specify documents that describe the bot's
            background and its perception of itself.
        :param context_document_ids: Pass the ids of the documents that you wish to inform your bot
            with for the specific user/session. Applicable for closed and
            hybrid modes as described above.
        :return: response: The agent's response
        session_name: The session's name which is generated after 3 interactions.
        messages: A list of the conversation's messages so far.
        context: The context that was made available to the agent for responding
            to the user's last message.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services>`_
        '''
        return super().__call__(user=user, message=message, chatbot_id=chatbot_id, user_id=user_id, mode=mode, session_id=session_id, previous_messages=previous_messages, bot_document_ids=bot_document_ids, context_document_ids=context_document_ids)

    def set_input_configs(self, name:str, message:Union[str, InputConfig], chatbot_id:Union[str, InputConfig], user_id:Union[str, InputConfig], mode:Union[str, InputConfig], session_id:Union[str, InputConfig]=None, previous_messages:Union[list, InputConfig]=None, bot_document_ids:Union[list, InputConfig]=None, context_document_ids:Union[list, InputConfig]=None):
        super().set_input_configs(name=name, message=message, chatbot_id=chatbot_id, user_id=user_id, mode=mode, session_id=session_id, previous_messages=previous_messages, bot_document_ids=bot_document_ids, context_document_ids=context_document_ids)

    @classmethod
    def call(self, user:str, message:str, chatbot_id:str, user_id:str, mode:str, session_id:str=None, previous_messages:list=None, bot_document_ids:list=None, context_document_ids:list=None) -> dict:
        '''
        Call the Chat Bot Service
        
        :param user: The ID of the user accessing the Soffos API.
            This string will be used for throttling and profanity tracking.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        :param message: The user's message to the chatbot
        :param chatbot_id: The chatbot's id.
        :param user_id: A unique user id. It is recommended that your provide a UUID.
        :param mode: The value can only be one of: open, closed, hybrid.
        :param session_id: A unique session id for mapping the records to your application.
            It is recommended that you provide a UUID. If not provided, the
            system will not store any information regarding the call and
            will use the value of "previous_messages" as the conversation
            history.
        :param previous_messages: This field can be used to provide the conversation history. It
            is ignored if a "session_id" is provided, in which case the
            system will used the stored interactions from that session as
            conversation history.
        :param bot_document_ids: Here you can specify documents that describe the bot's
            background and its perception of itself.
        :param context_document_ids: Pass the ids of the documents that you wish to inform your bot
            with for the specific user/session. Applicable for closed and
            hybrid modes as described above.
        :return: response: The agent's response
        session_name: The session's name which is generated after 3 interactions.
        messages: A list of the conversation's messages so far.
        context: The context that was made available to the agent for responding
            to the user's last message.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/chat_bot.py>`_
        '''
        return super().call(user=user, message=message, chatbot_id=chatbot_id, user_id=user_id, mode=mode, session_id=session_id, previous_messages=previous_messages, bot_document_ids=bot_document_ids, context_document_ids=context_document_ids)

class ChatBotsDeleteService(SoffosAIService):
    '''
    Deleting a chatbot will also delete all the conversation history for that
    chatbot.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.CHAT_BOTS_DELETE
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, chatbot_ids:list) -> dict:
        '''
        Call the Chat Bots Delete Service
        
        :param user: The ID of the user accessing the Soffos API.
            This string will be used for throttling and profanity tracking.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        :param chatbot_ids: List of the ids of the chatbots to be deleted.
        :return: success: Determines if the API call is successful or not.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/chat_bots_delete.py>`_
        '''
        return super().__call__(user=user, chatbot_ids=chatbot_ids)

    def set_input_configs(self, name:str, chatbot_ids:Union[list, InputConfig]):
        super().set_input_configs(name=name, chatbot_ids=chatbot_ids)

    @classmethod
    def call(self, user:str, chatbot_ids:list) -> dict:
        '''
        Call the Chat Bots Delete Service
        
        :param user: The ID of the user accessing the Soffos API.
            This string will be used for throttling and profanity tracking.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        :param chatbot_ids: List of the ids of the chatbots to be deleted.
        :return: success: Determines if the API call is successful or not.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/chat_bots_delete.py>`_
        '''
        return super().call(user=user, chatbot_ids=chatbot_ids)


class ChatBotsGetService(SoffosAIService):
    '''
    This endpoint allows you to get the information of previously created chatbots.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.CHAT_BOTS_GET
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, chatbot_ids:list=None) -> dict:
        '''
        Call the Chat Bots Get Service
        
        :param user: The ID of the user accessing the Soffos API.
            This string will be used for throttling and profanity tracking.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        :param chatbot_ids: Specify the id of the chatbots you need to see the details for.
            Don't pass this parameter if you wish to see all your created
            chatbots.
        :return: chatbots: A list of dictionaries with details about your chatbots.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/chat_bots_get.py>`_
        '''
        return super().__call__(user=user, chatbot_ids=chatbot_ids)

    def set_input_configs(self, name:str, chatbot_ids:Union[list, InputConfig]=None):
        super().set_input_configs(name=name, chatbot_ids=chatbot_ids)

    @classmethod
    def call(self, user:str, chatbot_ids:list=None) -> dict:
        '''
        Call the Chat Bots Get Service
        
        :param user: The ID of the user accessing the Soffos API.
            This string will be used for throttling and profanity tracking.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        :param chatbot_ids: Specify the id of the chatbots you need to see the details for.
            Don't pass this parameter if you wish to see all your created
            chatbots.
        :return: chatbots: A list of dictionaries with details about your chatbots.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/chat_bots_get.py>`_
        '''
        return super().call(user=user, chatbot_ids=chatbot_ids)


class ChatBotCreateService(SoffosAIService):
    '''
    Creates a chatbot and returns its ID. The id will later be used to allow users
    to interact with it.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.CHAT_BOT_CREATE
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, role:str, chatbot_name:str, chatbot_id:str=None) -> dict:
        '''
        Call the Chat Bot Create Service
        
        :param user: The ID of the user accessing the Soffos API.
            This string will be used for throttling and profanity tracking.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        :param role: A description of your bot's purpose. You may also describe its
            tone when responding. The system may not be able to follow
            complex instructions specified in this field.
        :param chatbot_name: The name/identity of your chatbot.
        :param chatbot_id: The chatbot's id. Provided when you create the chatbot. If you
            provide this, the chatbot with this ID's will be updated. The
            role and name will be updated.
        :return: chatbot_id: The chatbot's id. Provided when you create the chatbot. If you
            provide this, the chatbot with this ID's will be updated. The
            role and name will be updated.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/chat_bot_create.py>`_
        '''
        return super().__call__(user=user, role=role, chatbot_name=chatbot_name, chatbot_id=chatbot_id)

    def set_input_configs(self, name:str, role:Union[str, InputConfig], chatbot_name:Union[str, InputConfig], chatbot_id:Union[str, InputConfig]=None):
        super().set_input_configs(name=name, role=role, chatbot_name=chatbot_name, chatbot_id=chatbot_id)

    @classmethod
    def call(self, user:str, role:str, chatbot_name:str, chatbot_id:str=None) -> dict:
        '''
        Call the Chat Bot Create Service
        
        :param user: The ID of the user accessing the Soffos API.
            This string will be used for throttling and profanity tracking.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        :param role: A description of your bot's purpose. You may also describe its
            tone when responding. The system may not be able to follow
            complex instructions specified in this field.
        :param chatbot_name: The name/identity of your chatbot.
        :param chatbot_id: The chatbot's id. Provided when you create the chatbot. If you
            provide this, the chatbot with this ID's will be updated. The
            role and name will be updated.
        :return: chatbot_id: The chatbot's id. Provided when you create the chatbot. If you
            provide this, the chatbot with this ID's will be updated. The
            role and name will be updated.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/chat_bot_create.py>`_
        '''
        return super().call(user=user, role=role, chatbot_name=chatbot_name, chatbot_id=chatbot_id)


class ChatBotDeleteUserSessionsService(SoffosAIService):
    '''
    Delete user sessions
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.CHAT_BOT_DELETE_USER_SESSIONS
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, chatbot_id:str, user_id:str, session_ids:list=None) -> dict:
        '''
        Call the Chat Bot Delete User Sessions Service
        
        :param user: The ID of the user accessing the Soffos API.
            This string will be used for throttling and profanity tracking.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        :param chatbot_id: The chatbot's id.
        :param user_id: A unique user id. It is recommended that your provide a UUID.
        :param session_ids: List of the ids of the user sessions to be deleted.
        :return: success: Determines if the API call is successful or not.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/chat_bot_delete_user_sessions.py>`_
        '''
        return super().__call__(user=user, chatbot_id=chatbot_id, user_id=user_id, session_ids=session_ids)

    def set_input_configs(self, name:str, chatbot_id:Union[str, InputConfig], user_id:Union[str, InputConfig], session_ids:Union[list, InputConfig]=None):
        super().set_input_configs(name=name, chatbot_id=chatbot_id, user_id=user_id, session_ids=session_ids)

    @classmethod
    def call(self, user:str, chatbot_id:str, user_id:str, session_ids:list=None) -> dict:
        '''
        Call the Chat Bot Delete User Sessions Service
        
        :param user: The ID of the user accessing the Soffos API.
            This string will be used for throttling and profanity tracking.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        :param chatbot_id: The chatbot's id.
        :param user_id: A unique user id. It is recommended that your provide a UUID.
        :param session_ids: List of the ids of the user sessions to be deleted.
        :return: success: Determines if the API call is successful or not.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/chat_bot_delete_user_sessions.py>`_
        '''
        return super().call(user=user, chatbot_id=chatbot_id, user_id=user_id, session_ids=session_ids)


class ChatBotGetUserSessionsService(SoffosAIService):
    '''
    Get user sessions
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.CHAT_BOT_GET_USER_SESSIONS
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, chatbot_id:str, user_id:str, session_ids:list=None) -> dict:
        '''
        Call the Chat Bot Get User Sessions Service
        
        :param user: The ID of the user accessing the Soffos API.
            This string will be used for throttling and profanity tracking.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        :param chatbot_id: The chatbot's id.
        :param user_id: A unique user id. It is recommended that your provide a UUID.
        :param session_ids: Specify the id of the sessions you need to get.
        :return: sessions: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/chat_bot_get_user_sessions.py>`_
        '''
        return super().__call__(user=user, chatbot_id=chatbot_id, user_id=user_id, session_ids=session_ids)

    def set_input_configs(self, name:str, chatbot_id:Union[str, InputConfig], user_id:Union[str, InputConfig], session_ids:Union[list, InputConfig]=None):
        super().set_input_configs(name=name, chatbot_id=chatbot_id, user_id=user_id, session_ids=session_ids)

    @classmethod
    def call(self, user:str, chatbot_id:str, user_id:str, session_ids:list=None) -> dict:
        '''
        Call the Chat Bot Get User Sessions Service
        
        :param user: The ID of the user accessing the Soffos API.
            This string will be used for throttling and profanity tracking.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        :param chatbot_id: The chatbot's id.
        :param user_id: A unique user id. It is recommended that your provide a UUID.
        :param session_ids: Specify the id of the sessions you need to get.
        :return: sessions: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/chat_bot_get_user_sessions.py>`_
        '''
        return super().call(user=user, chatbot_id=chatbot_id, user_id=user_id, session_ids=session_ids)



class DiscussCountService(SoffosAIService):
    '''
    The Let's Discuss module allows the user to have a conversation with the AI
    about the content provided by the user. The main difference between this module
    and the Question Answering module is that Let's Discuss keeps a history of the
    interactions, allowing it to take in account what was previously discussed when
    generating a response. Unlike Question Answering which is mainly used for
    information retrieval, the Let's Discuss module creates a more natural
    experience similar to having a conversation with a person at the expense of the
    size of the content it can process at a time.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.DISCUSS_COUNT
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, return_messages:bool) -> dict:
        '''
        Call the Discuss Count Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param return_messages: When set to true, in addition to returning all the session records, it
            will also return all the messages associated with each session.
        :return: sessions: List of sessions. Each session contains the following data: context: The
            content discussed in the session. session_id: Session's ID. messages: If
            return_messages is true, this list will contain a list of dictionaries
            representing the interactions between the system and the user. Each
            dictionary contains the user's query, the system's response and the
            interaction's ID as message_id, which is an integer indicating their
            order.
        session_count: The count of sessions for your organization. It is important to map
            sessions to your users at the application level.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/discuss.py>`_
        '''
        return super().__call__(user=user, return_messages=return_messages)

    def set_input_configs(self, name:str, return_messages:Union[bool, InputConfig]):
        super().set_input_configs(name=name, return_messages=return_messages)

    @classmethod
    def call(self, user:str, return_messages:bool) -> dict:
        '''
        Call the Discuss Count Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param return_messages: When set to true, in addition to returning all the session records, it
            will also return all the messages associated with each session.
        :return: sessions: List of sessions. Each session contains the following data: context: The
            content discussed in the session. session_id: Session's ID. messages: If
            return_messages is true, this list will contain a list of dictionaries
            representing the interactions between the system and the user. Each
            dictionary contains the user's query, the system's response and the
            interaction's ID as message_id, which is an integer indicating their
            order.
        session_count: The count of sessions for your organization. It is important to map
            sessions to your users at the application level.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/discuss.py>`_
        '''
        return super().call(user=user, return_messages=return_messages)



class DiscussCreateService(SoffosAIService):
    '''
    The Let's Discuss module allows the user to have a conversation with the AI
    about the content provided by the user. The main difference between this module
    and the Question Answering module is that Let's Discuss keeps a history of the
    interactions, allowing it to take in account what was previously discussed when
    generating a response. Unlike Question Answering which is mainly used for
    information retrieval, the Let's Discuss module creates a more natural
    experience similar to having a conversation with a person at the expense of the
    size of the content it can process at a time.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.DISCUSS_CREATE
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, context:str) -> dict:
        '''
        Call the Discuss Create Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param context: The content to discuss about.
        :return: 
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/discuss.py>`_
        '''
        return super().__call__(user=user, context=context)

    def set_input_configs(self, name:str, context:Union[str, InputConfig]):
        super().set_input_configs(name=name, context=context)

    @classmethod
    def call(self, user:str, context:str) -> dict:
        '''
        Call the Discuss Create Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param context: The content to discuss about.
        :return: 
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/discuss.py>`_
        '''
        return super().call(user=user, context=context)



class DiscussDeleteService(SoffosAIService):
    '''
    The Let's Discuss module allows the user to have a conversation with the AI
    about the content provided by the user. The main difference between this module
    and the Question Answering module is that Let's Discuss keeps a history of the
    interactions, allowing it to take in account what was previously discussed when
    generating a response. Unlike Question Answering which is mainly used for
    information retrieval, the Let's Discuss module creates a more natural
    experience similar to having a conversation with a person at the expense of the
    size of the content it can process at a time.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.DISCUSS_DELETE
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, session_ids:list=None) -> dict:
        '''
        Call the Discuss Delete Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param session_ids: A list with the IDs of the sessions to be deleted.
        :return: success: Indicates whether the sessions have been successfuly deleted.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/discuss.py>`_
        '''
        return super().__call__(user=user, session_ids=session_ids)

    def set_input_configs(self, name:str, session_ids:Union[list, InputConfig]=None):
        super().set_input_configs(name=name, session_ids=session_ids)

    @classmethod
    def call(self, user:str, session_ids:list=None) -> dict:
        '''
        Call the Discuss Delete Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param session_ids: A list with the IDs of the sessions to be deleted.
        :return: success: Indicates whether the sessions have been successfuly deleted.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/discuss.py>`_
        '''
        return super().call(user=user, session_ids=session_ids)



class DiscussQueryService(SoffosAIService):
    '''
    The Let's Discuss module allows the user to have a conversation with the AI
    about the content provided by the user. The main difference between this module
    and the Question Answering module is that Let's Discuss keeps a history of the
    interactions, allowing it to take in account what was previously discussed when
    generating a response. Unlike Question Answering which is mainly used for
    information retrieval, the Let's Discuss module creates a more natural
    experience similar to having a conversation with a person at the expense of the
    size of the content it can process at a time.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.DISCUSS_QUERY
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, query:str) -> dict:
        '''
        Call the Discuss Query Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param query: User's message.
        :return: response: None
        context: None
        messages: A list of dictionaries representing all the messages exchanged between the
            user and the system for the specific session. The messages are sorted in
            chronological order. Each dictionary contains the following fields: text:
            The message. source: The source of the message, which is either the user
            or Soffos.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/discuss.py>`_
        '''
        return super().__call__(user=user, query=query)

    def set_input_configs(self, name:str, query:Union[str, InputConfig]):
        super().set_input_configs(name=name, query=query)

    @classmethod
    def call(self, user:str, query:str) -> dict:
        '''
        Call the Discuss Query Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param query: User's message.
        :return: response: None
        context: None
        messages: A list of dictionaries representing all the messages exchanged between the
            user and the system for the specific session. The messages are sorted in
            chronological order. Each dictionary contains the following fields: text:
            The message. source: The source of the message, which is either the user
            or Soffos.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/discuss.py>`_
        '''
        return super().call(user=user, query=query)



class DocumentsCountService(SoffosAIService):
    '''
    General HTTP service client.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.DOCUMENTS_COUNT
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, filters:dict=None, date_from:str=None, date_until:str=None) -> dict:
        '''
        Call the Documents Count Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param filters: None
        :param date_from: None
        :param date_until: None
        :return: documents: None
        count: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/documents_count.py>`_
        '''
        return super().__call__(user=user, filters=filters, date_from=date_from, date_until=date_until)

    def set_input_configs(self, name:str, filters:Union[dict, InputConfig]=None, date_from:Union[str, InputConfig]=None, date_until:Union[str, InputConfig]=None):
        super().set_input_configs(name=name, filters=filters, date_from=date_from, date_until=date_until)

    @classmethod
    def call(self, user:str, filters:dict=None, date_from:str=None, date_until:str=None) -> dict:
        '''
        Call the Documents Count Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param filters: None
        :param date_from: None
        :param date_until: None
        :return: documents: None
        count: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/documents_count.py>`_
        '''
        return super().call(user=user, filters=filters, date_from=date_from, date_until=date_until)



class DocumentsDeleteService(SoffosAIService):
    '''
    General HTTP service client.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.DOCUMENTS_DELETE
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, document_ids:list) -> dict:
        '''
        Call the Documents Delete Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param document_ids: A list of the document_ids of the documents to be deleted.
        :return: success: Flag that identifies if the API call succeeded or not.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/documents.py>`_
        '''
        return super().__call__(user=user, document_ids=document_ids)

    def set_input_configs(self, name:str, document_ids:Union[list, InputConfig]):
        super().set_input_configs(name=name, document_ids=document_ids)

    @classmethod
    def call(self, user:str, document_ids:list) -> dict:
        '''
        Call the Documents Delete Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param document_ids: A list of the document_ids of the documents to be deleted.
        :return: success: Flag that identifies if the API call succeeded or not.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/documents.py>`_
        '''
        return super().call(user=user, document_ids=document_ids)



class DocumentsIngestService(SoffosAIService):
    '''
    The Documents module enables ingestion of contnent into Soffos. The content is
    pre-processed and stored alongside its representations and metadata required
    for searching using natural language. Queries can be as simple as questions
    that someone would ask a human. Additionally, content can be filtered based on
    the metadata provided by the user when ingesting a document. The combination of
    basic filtering similar to how most databases work in combination with natural
    language search, both keyword-based and semantic using machine learning, makes
    this module a very useful tool for any type of use-case that requires lighning
    fast information extraction from large knowledge bases.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.DOCUMENTS_INGEST
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, document_id:str=None, meta:dict=None, document_name:str=None, text:str=None, tagged_elements:list=None) -> dict:
        '''
        Call the Documents Ingest Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param document_id: The reference ID of the uploaded document.
        :param meta: None
        :param document_name: The name of the document.
        :param text: The text content of the document.
        :param tagged_elements: A list of dictionaries representing tagged spans of text extracted from a
            document file.
        :return: document_id: The reference ID of the uploaded document.
        success: Flag that identifies if the API call succeeded or not.
        filtered: List of passages not included in ingestion due to some profanity or errors.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/documents.py>`_
        '''
        return super().__call__(user=user, document_id=document_id, meta=meta, document_name=document_name, text=text, tagged_elements=tagged_elements)

    def set_input_configs(self, name:str, document_id:Union[str, InputConfig]=None, meta:Union[dict, InputConfig]=None, document_name:Union[str, InputConfig]=None, text:Union[str, InputConfig]=None, tagged_elements:Union[list, InputConfig]=None):
        super().set_input_configs(name=name, document_id=document_id, meta=meta, document_name=document_name, text=text, tagged_elements=tagged_elements)

    @classmethod
    def call(self, user:str, document_id:str=None, meta:dict=None, document_name:str=None, text:str=None, tagged_elements:list=None) -> dict:
        '''
        Call the Documents Ingest Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param document_id: The reference ID of the uploaded document.
        :param meta: None
        :param document_name: The name of the document.
        :param text: The text content of the document.
        :param tagged_elements: A list of dictionaries representing tagged spans of text extracted from a
            document file.
        :return: document_id: The reference ID of the uploaded document.
        success: Flag that identifies if the API call succeeded or not.
        filtered: List of passages not included in ingestion due to some profanity or errors.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/documents.py>`_
        '''
        return super().call(user=user, document_id=document_id, meta=meta, document_name=document_name, text=text, tagged_elements=tagged_elements)



class DocumentsSearchService(SoffosAIService):
    '''
    General HTTP service client.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.DOCUMENTS_SEARCH
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, query:str=None, document_ids:list=None, top_n_keyword:int=5, top_n_natural_language:int=5, filters:dict=None, date_from:str=None, date_until:str=None) -> dict:
        '''
        Call the Documents Search Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param query: The text to be used to match passages from ingested documents.
        :param document_ids: Passing document IDs will confine the search to those documents.
        :param top_n_keyword: The number of document passages to be retrieved using keyword search.
        :param top_n_natural_language: The number of document passages to be retrieved using Machine
            Learning-based semantic search.
        :param filters: The filters field can be used to narrow down the search to only the
            documents meeting certain metadata-based criteria, or even returning all
            the filtered documents when query is left null.
        :param date_from: Filters passages to those ingested at or after the specified ISO-8601
            formatted date.
        :param date_until: Filters passages to those ingested before the specified ISO-8601 formatted
            date.
        :return: items: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/documents.py>`_
        '''
        return super().__call__(user=user, query=query, document_ids=document_ids, top_n_keyword=top_n_keyword, top_n_natural_language=top_n_natural_language, filters=filters, date_from=date_from, date_until=date_until)

    def set_input_configs(self, name:str, query:Union[str, InputConfig]=None, document_ids:Union[list, InputConfig]=None, top_n_keyword:Union[int, InputConfig]=5, top_n_natural_language:Union[int, InputConfig]=5, filters:Union[dict, InputConfig]=None, date_from:Union[str, InputConfig]=None, date_until:Union[str, InputConfig]=None):
        super().set_input_configs(name=name, query=query, document_ids=document_ids, top_n_keyword=top_n_keyword, top_n_natural_language=top_n_natural_language, filters=filters, date_from=date_from, date_until=date_until)

    @classmethod
    def call(self, user:str, query:str=None, document_ids:list=None, top_n_keyword:int=5, top_n_natural_language:int=5, filters:dict=None, date_from:str=None, date_until:str=None) -> dict:
        '''
        Call the Documents Search Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param query: The text to be used to match passages from ingested documents.
        :param document_ids: Passing document IDs will confine the search to those documents.
        :param top_n_keyword: The number of document passages to be retrieved using keyword search.
        :param top_n_natural_language: The number of document passages to be retrieved using Machine
            Learning-based semantic search.
        :param filters: The filters field can be used to narrow down the search to only the
            documents meeting certain metadata-based criteria, or even returning all
            the filtered documents when query is left null.
        :param date_from: Filters passages to those ingested at or after the specified ISO-8601
            formatted date.
        :param date_until: Filters passages to those ingested before the specified ISO-8601 formatted
            date.
        :return: items: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/documents.py>`_
        '''
        return super().call(user=user, query=query, document_ids=document_ids, top_n_keyword=top_n_keyword, top_n_natural_language=top_n_natural_language, filters=filters, date_from=date_from, date_until=date_until)



class EmailAnalysisService(SoffosAIService):
    '''
    This module extracts key information from the body of an e-mail.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.EMAIL_ANALYSIS
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str) -> dict:
        '''
        Call the Email Analysis Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: The e-mail body text.
        :return: analysis: A dictionary containing the following key information: key points: string
            list topics: string list sender: string receiver: string list mentions:
            string list sentiment: string urgency: string dates: string list
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/email_analysis.py>`_
        '''
        return super().__call__(user=user, text=text)

    def set_input_configs(self, name:str, text:Union[str, InputConfig]):
        super().set_input_configs(name=name, text=text)

    @classmethod
    def call(self, user:str, text:str) -> dict:
        '''
        Call the Email Analysis Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: The e-mail body text.
        :return: analysis: A dictionary containing the following key information: key points: string
            list topics: string list sender: string receiver: string list mentions:
            string list sentiment: string urgency: string dates: string list
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/email_analysis.py>`_
        '''
        return super().call(user=user, text=text)



class EmotionDetectionService(SoffosAIService):
    '''
    The Emotion Detection module can detect selected emotions within the provided
    text. The original text is chunked to passages of a specified sentence length.
    Smaller chunks yield better accuracy.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.EMOTION_DETECTION
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str, sentence_split:int=None, sentence_overlap:bool=True, emotion_choices:list=['joy', 'trust', 'fear', 'surprise', 'sadness', 'disgust', 'anger', 'anticipation']) -> dict:
        '''
        Call the Emotion Detection Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to detect emotions from.
        :param sentence_split: The number of sentences of each chunk when splitting the input text.
        :param sentence_overlap: Whether to overlap adjacent chunks by 1 sentence. For example, with
            sentence_split=3 and sentence_overlap=true : [[s1, s2, s3], [s3, s4, s5],
            [s5, s6, s7]]
        :param emotion_choices: List of emotions to detect in the text. If the field is not provided in
            the payload, or set as null or empty list, it will default to all emotion
            choices. Currently supported emotions are listed above in the default
            emotion values.
        :return: spans: A list of spans resulting from the specified chunking parameters. Each
            span contains the following fields: text: The text of the span.
            detected_emotions: A list of the emotions detected for the specific span.
            span_start: The starting character index of the span in the original input
            text. span_end: The ending character index of the span in the original
            input text.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/emotion_detection.py>`_
        '''
        return super().__call__(user=user, text=text, sentence_split=sentence_split, sentence_overlap=sentence_overlap, emotion_choices=emotion_choices)

    def set_input_configs(self, name:str, text:Union[str, InputConfig], sentence_split:Union[int, InputConfig], sentence_overlap:Union[bool, InputConfig], emotion_choices:Union[str, InputConfig]=['joy', 'trust', 'fear', 'surprise', 'sadness', 'disgust', 'anger', 'anticipation']):
        super().set_input_configs(name=name, text=text, sentence_split=sentence_split, sentence_overlap=sentence_overlap, emotion_choices=emotion_choices)

    @classmethod
    def call(self, user:str, text:str, sentence_split:int=None, sentence_overlap:bool=True, emotion_choices:list=['joy', 'trust', 'fear', 'surprise', 'sadness', 'disgust', 'anger', 'anticipation']) -> dict:
        '''
        Call the Emotion Detection Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to detect emotions from.
        :param sentence_split: The number of sentences of each chunk when splitting the input text.
        :param sentence_overlap: Whether to overlap adjacent chunks by 1 sentence. For example, with
            sentence_split=3 and sentence_overlap=true : [[s1, s2, s3], [s3, s4, s5],
            [s5, s6, s7]]
        :param emotion_choices: List of emotions to detect in the text. If the field is not provided in
            the payload, or set as null or empty list, it will default to all emotion
            choices. Currently supported emotions are listed above in the default
            emotion values.
        :return: spans: A list of spans resulting from the specified chunking parameters. Each
            span contains the following fields: text: The text of the span.
            detected_emotions: A list of the emotions detected for the specific span.
            span_start: The starting character index of the span in the original input
            text. span_end: The ending character index of the span in the original
            input text.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/emotion_detection.py>`_
        '''
        return super().call(user=user, text=text, sentence_split=sentence_split, sentence_overlap=sentence_overlap, emotion_choices=emotion_choices)


class FileConverterService(SoffosAIService):
    '''
    The File Converter extracts text from various types of files. It tags elements
    within structured DOCX documents and provides a list of labelled text spans.
    Additionally, the normalize feature is available which uses a machine learning
    approach to organize messy outputs as well as tag and label document elements
    based on the whitespace formatting (new lines, spaces, etc.) and the content
    itself. The normalize feature is more suited for unstructured documents such as
    plain text or PDFs (scanned and searchable) that are almost impossible to
    process reliably with a single rule-based approach due to their inconsistent
    and often complicated formatting. Note: Character volume is not charged when
    calling this module unless the normalize feature is enabled. When enabled,
    characters in the normalized_text output field are charged. Otherwise, only the
    base API call cost is charged. Tip: DOCX documents are well structured and can
    be processed reliably without enabling normalize. DOCX is the only type of
    document that produces tagged_elements. Use the normalize feature only with
    DOCX documents that do not have a good heading/list structure such as DOCX that
    have been converted from PDF.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.FILE_CONVERTER
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, file:BufferedReader, normalize:str) -> dict:
        '''
        Call the File Converter Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param file: None
        :param normalize: None
        :return: normalize: None
        text: Raw text extracted from the document.
        tagged_elements: A list of dictionaries of all the extracted text snippets and their tags.
            Each dictionary has the following fields: text: The text of the snippet.
            tag: A tag. Detectable elements: paragraph, heading, bullet_list,
            table_of_contents. headings: A list of dictionaries representing the
            headings which this element is under. Each dictionary contains the text
            and tag fields of each heading. This is useful for sorting and labelling
            the content. Other element-specific fields: bullets: Available only
            bullet_list elements. Contains all bullets and their sub-bullets in a
            nested structure. contents: Available only in table_of_content elements.
            Contains the headings and sub-headings of the document's table of
            contents. heading: Available only in table_of_content elements. It is the
            heading of the document's table of contents.
        normalized_text: Resulting text after normalization.
        normalized_tagged_elements: Similar to the standard tagged_elements. Detectable elements: paragraph,
            heading, bullet_list, quote.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/file_converter.py>`_
        '''
        return super().__call__(user=user, file=file, normalize=normalize)

    def set_input_configs(self, name:str, file:Union[str, BufferedReader, InputConfig], normalize:Union[str, InputConfig]):
        super().set_input_configs(name=name, file=file, normalize=normalize)

    @classmethod
    def call(self, user:str, file:BufferedReader, normalize:str) -> dict:
        '''
        Call the File Converter Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param file: None
        :param normalize: None
        :return: normalize: None
        text: Raw text extracted from the document.
        tagged_elements: A list of dictionaries of all the extracted text snippets and their tags.
            Each dictionary has the following fields: text: The text of the snippet.
            tag: A tag. Detectable elements: paragraph, heading, bullet_list,
            table_of_contents. headings: A list of dictionaries representing the
            headings which this element is under. Each dictionary contains the text
            and tag fields of each heading. This is useful for sorting and labelling
            the content. Other element-specific fields: bullets: Available only
            bullet_list elements. Contains all bullets and their sub-bullets in a
            nested structure. contents: Available only in table_of_content elements.
            Contains the headings and sub-headings of the document's table of
            contents. heading: Available only in table_of_content elements. It is the
            heading of the document's table of contents.
        normalized_text: Resulting text after normalization.
        normalized_tagged_elements: Similar to the standard tagged_elements. Detectable elements: paragraph,
            heading, bullet_list, quote.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/file_converter.py>`_
        '''
        return super().call(user=user, file=file, normalize=normalize)



class LanguageDetectionService(SoffosAIService):
    '''
    The Language Detection module detects the dominant language in the provided
    text.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.LANGUAGE_DETECTION
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str) -> dict:
        '''
        Call the Language Detection Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to be classified under a language.
        :return: language: The language code of the detected language.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/language_detection.py>`_
        '''
        return super().__call__(user=user, text=text)

    def set_input_configs(self, name:str, text:Union[str, InputConfig]):
        super().set_input_configs(name=name, text=text)

    @classmethod
    def call(self, user:str, text:str) -> dict:
        '''
        Call the Language Detection Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to be classified under a language.
        :return: language: The language code of the detected language.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/language_detection.py>`_
        '''
        return super().call(user=user, text=text)



class LogicalErrorDetectionService(SoffosAIService):
    '''
    Identifies illogical statements in text and explains why they are illogical.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.LOGICAL_ERROR_DETECTION
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str) -> dict:
        '''
        Call the Logical Error Detection Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Input text to analyze for logical errors.
        :return: logical_errors: A list of dictionaries representing detected logical errors. Each
            dictionary contains the following fields: text: The illogical text. start:
            Starting character index in the original text. end: Ending chracter index
            in the original text. explanation: The reasoning behind why the text span
            is illogical.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/logical_error_detection.py>`_
        '''
        return super().__call__(user=user, text=text)

    def set_input_configs(self, name:str, text:Union[str, InputConfig]):
        super().set_input_configs(name=name, text=text)

    @classmethod
    def call(self, user:str, text:str) -> dict:
        '''
        Call the Logical Error Detection Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Input text to analyze for logical errors.
        :return: logical_errors: A list of dictionaries representing detected logical errors. Each
            dictionary contains the following fields: text: The illogical text. start:
            Starting character index in the original text. end: Ending chracter index
            in the original text. explanation: The reasoning behind why the text span
            is illogical.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/logical_error_detection.py>`_
        '''
        return super().call(user=user, text=text)



class MicrolessonService(SoffosAIService):
    '''
    Accepts a list of texts, each one labelled with its source and creates a
    concise microlesson including a short summary, key points, learning objectives
    and tasks that aim to help the learner achieve the learning objectives.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.MICROLESSON
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, content:list) -> dict:
        '''
        Call the Microlesson Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param content: A list of dictionaries. Each dictionary should contain the 'source' and
            'text' fields, where 'source' is the name of the
            document/article/website/etc. and 'text' is the actual content. Providing
            the source names enables the microlesson to include the source for the key
            points extracted from the content.
        :return: microlesson: A concise, structured microlesson containing a summary, key points,
            learning objectives and tasks.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/microlesson.py>`_
        '''
        return super().__call__(user=user, content=content)

    def set_input_configs(self, name:str, content:Union[list, InputConfig]):
        super().set_input_configs(name=name, content=content)

    @classmethod
    def call(self, user:str, content:list) -> dict:
        '''
        Call the Microlesson Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param content: A list of dictionaries. Each dictionary should contain the 'source' and
            'text' fields, where 'source' is the name of the
            document/article/website/etc. and 'text' is the actual content. Providing
            the source names enables the microlesson to include the source for the key
            points extracted from the content.
        :return: microlesson: A concise, structured microlesson containing a summary, key points,
            learning objectives and tasks.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/microlesson.py>`_
        '''
        return super().call(user=user, content=content)



class NERService(SoffosAIService):
    '''
    Identifies named entities in text. It supports custom labels. Below are the
    default entities and their labels: | tag | type | | ----------- |
    -------------------- | | CARDINAL | cardinal value | | DATE | date value | |
    EVENT | event name | | FAC | building name | | GPE | geo-political entity | |
    LANGUAGE | language name | | LAW | law name | | LOC | location name | | MONEY |
    money name | | NORP | affiliation | | ORDINAL | ordinal value | | ORG |
    organization name | | PERCENT | percent value | | PERSON | person name | |
    PRODUCT | product name | | QUANTITY | quantity value | | TIME | time value | |
    WORK_OF_ART | name of work of art | However, this module is extremely versatile
    as the labels can be defined by the user. See the below example on how this can
    be applied to a medical use-case.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.N_E_R
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str, labels:dict=None) -> dict:
        '''
        Call the N E R Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Input text to be analyzed for named entities.
        :param labels: When providing labels, the module will extract entities that match your
            labels and descriptions. This gives enough flexibility to deal with any
            use-case.
        :return: named_entities: A list of dictionaries representing identified named entities. Each
            dictionary contains the following fields: text: The text of the entity.
            tag: Label of the entity. span: A list with the start and end offset of
            the entity in the original text.
        entity_counts: A list of dictionaries with entities and their counts. The dictionaries
            contain the following fields: text: The name of the entity. tag: Label of
            the entity. count: Number of occurrences of the entity in the text.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/named_entity_recognition.py>`_
        '''
        return super().__call__(user=user, text=text, labels=labels)

    def set_input_configs(self, name:str, text:Union[str, InputConfig], labels:Union[dict, InputConfig]=None):
        super().set_input_configs(name=name, text=text, labels=labels)

    @classmethod
    def call(self, user:str, text:str, labels:dict=None) -> dict:
        '''
        Call the N E R Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Input text to be analyzed for named entities.
        :param labels: When providing labels, the module will extract entities that match your
            labels and descriptions. This gives enough flexibility to deal with any
            use-case.
        :return: named_entities: A list of dictionaries representing identified named entities. Each
            dictionary contains the following fields: text: The text of the entity.
            tag: Label of the entity. span: A list with the start and end offset of
            the entity in the original text.
        entity_counts: A list of dictionaries with entities and their counts. The dictionaries
            contain the following fields: text: The name of the entity. tag: Label of
            the entity. count: Number of occurrences of the entity in the text.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/named_entity_recognition.py>`_
        '''
        return super().call(user=user, text=text, labels=labels)



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



class ParaphraseService(SoffosAIService):
    '''
    Paraphrase and Simplify are available as two different flavors of the same
    module. While the Paraphrase module attempts to change the wording while
    keeping the same level of complexity, the Simplify module outputs more commonly
    used words without altering the meaning of the original text.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.PARAPHRASE
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str) -> dict:
        '''
        Call the Paraphrase Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to be paraphrased/simplified.
        :return: paraphrase: None
        simplify: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/paraphrase.py>`_
        '''
        return super().__call__(user=user, text=text)

    def set_input_configs(self, name:str, text:Union[str, InputConfig]):
        super().set_input_configs(name=name, text=text)

    @classmethod
    def call(self, user:str, text:str) -> dict:
        '''
        Call the Paraphrase Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to be paraphrased/simplified.
        :return: paraphrase: None
        simplify: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/paraphrase.py>`_
        '''
        return super().call(user=user, text=text)



class ProfanityService(SoffosAIService):
    '''
    Profanity related serializer
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.PROFANITY
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str) -> dict:
        '''
        Call the Profanity Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: None
        :return: profanities: None
        offensive_probability: None
        offensive_prediction: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/profanity.py>`_
        '''
        return super().__call__(user=user, text=text)

    def set_input_configs(self, name:str, text:Union[str, InputConfig]):
        super().set_input_configs(name=name, text=text)

    @classmethod
    def call(self, user:str, text:str) -> dict:
        '''
        Call the Profanity Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: None
        :return: profanities: None
        offensive_probability: None
        offensive_prediction: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/profanity.py>`_
        '''
        return super().call(user=user, text=text)



class QnAGenerationService(SoffosAIService):
    '''
    The Q&A Generation module splits large documents in chunks from which it
    generates multiple question-answer pairs. The chunk length is configurable.
    Usually more questions can be generated when segmenting the text to smaller
    chunks, while longer chunks help retain more context, in cases where a topic is
    discussed over multiple sentences in the context. To address cases where the
    topic is split mid-way, the module supports overlapping the chunks by a
    configurable amount of sentences. This gives a lot of flexibility to cater to
    your specific use case.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.QN_A_GENERATION
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str, sentence_split:int=3, sentence_overlap:bool=None) -> dict:
        '''
        Call the Qn A Generation Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: The input text from which the question-answer pairs will be generated.
        :param sentence_split: The number of sentences of each chunk when splitting the input text.
        :param sentence_overlap: Whether to overlap adjacent chunks by 1 sentence. For example, with
            sentence_split 3 and sentence_overlap=true : [[s1, s2, s3], [s3, s4, s5],
            [s5, s6, s7]]
        :return: qna_list: A list of dictionaries representing question-answer pairs. Each dictionary
            contains the fields question, answer and chunk_index which is the index of
            the chunk the question-answer pair was generated from. chunk_index maps to
            the chunk with the same value in the key index.
        chunks: A list of dictionaries representing the chunks as they were split from the
            original according to the splitting parameters given in the request. Each
            dictionary contains the fields text, index as well as the span_start and
            span_end fields which are the starting and ending position of the chunk in
            the originally provided text.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/qn_a_generation.py>`_
        '''
        return super().__call__(user=user, text=text, sentence_split=sentence_split, sentence_overlap=sentence_overlap)

    def set_input_configs(self, name:str, text:Union[str, InputConfig], sentence_split:Union[int, InputConfig]=3, sentence_overlap:Union[bool, InputConfig]=None):
        super().set_input_configs(name=name, text=text, sentence_split=sentence_split, sentence_overlap=sentence_overlap)

    @classmethod
    def call(self, user:str, text:str, sentence_split:int=3, sentence_overlap:bool=None) -> dict:
        '''
        Call the Qn A Generation Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: The input text from which the question-answer pairs will be generated.
        :param sentence_split: The number of sentences of each chunk when splitting the input text.
        :param sentence_overlap: Whether to overlap adjacent chunks by 1 sentence. For example, with
            sentence_split 3 and sentence_overlap=true : [[s1, s2, s3], [s3, s4, s5],
            [s5, s6, s7]]
        :return: qna_list: A list of dictionaries representing question-answer pairs. Each dictionary
            contains the fields question, answer and chunk_index which is the index of
            the chunk the question-answer pair was generated from. chunk_index maps to
            the chunk with the same value in the key index.
        chunks: A list of dictionaries representing the chunks as they were split from the
            original according to the splitting parameters given in the request. Each
            dictionary contains the fields text, index as well as the span_start and
            span_end fields which are the starting and ending position of the chunk in
            the originally provided text.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/qn_a_generation.py>`_
        '''
        return super().call(user=user, text=text, sentence_split=sentence_split, sentence_overlap=sentence_overlap)



class QuestionAnsweringService(SoffosAIService):
    '''
    This module is a combination of various sub-modules that enable users to get
    accurate answers on questions posed on a large amount of content. It includes
    basic intent recognition capabilities to enable appropriate responses to
    incorrect or profane language, or typical personal questions like "How are
    you?" and greetings.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.QUESTION_ANSWERING
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, question:str, document_text:str=None, document_ids:list=None, check_ambiguity:bool=True, check_query_type:bool=True, generic_response:bool=None, meta:dict=None, message_id:str=None) -> dict:
        '''
        Call the Question Answering Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param question: A natural language query/question.
        :param document_text: The text to be used as the context to formulate the answer.
        :param document_ids: A list of unique IDs referencing pre-ingested documents to be used as the
            context to formulate the answer.
        :param check_ambiguity: None
        :param check_query_type: None
        :param generic_response: None
        :param meta: None
        :param message_id: None
        :return: message_id: None
        answer: None
        context: None
        valid_query: None
        no_answer: None
        highlights: None
        passages: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/question_answering.py>`_
        '''
        return super().__call__(user=user, question=question, document_text=document_text, document_ids=document_ids, check_ambiguity=check_ambiguity, check_query_type=check_query_type, generic_response=generic_response, meta=meta, message_id=message_id)

    def set_input_configs(self, name:str, question:Union[str, InputConfig], document_text:Union[str, InputConfig]=None, document_ids:Union[list, InputConfig]=None, check_ambiguity:Union[bool, InputConfig]=True, check_query_type:Union[bool, InputConfig]=True, generic_response:Union[bool, InputConfig]=None, meta:Union[dict, InputConfig]=None, message_id:Union[str, InputConfig]=None):
        super().set_input_configs(name=name, question=question, document_text=document_text, document_ids=document_ids, check_ambiguity=check_ambiguity, check_query_type=check_query_type, generic_response=generic_response, meta=meta, message_id=message_id)

    @classmethod
    def call(self, user:str, question:str, document_text:str=None, document_ids:list=None, check_ambiguity:bool=True, check_query_type:bool=True, generic_response:bool=None, meta:dict=None, message_id:str=None) -> dict:
        '''
        Call the Question Answering Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param question: A natural language query/question.
        :param document_text: The text to be used as the context to formulate the answer.
        :param document_ids: A list of unique IDs referencing pre-ingested documents to be used as the
            context to formulate the answer.
        :param check_ambiguity: None
        :param check_query_type: None
        :param generic_response: None
        :param meta: None
        :param message_id: None
        :return: message_id: None
        answer: None
        context: None
        valid_query: None
        no_answer: None
        highlights: None
        passages: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/question_answering.py>`_
        '''
        return super().call(user=user, question=question, document_text=document_text, document_ids=document_ids, check_ambiguity=check_ambiguity, check_query_type=check_query_type, generic_response=generic_response, meta=meta, message_id=message_id)



class ReviewTaggerService(SoffosAIService):
    '''
    This module extracts key information from negative product reviews. It attempts
    to find the referred object, it's fault and an action/verb that is associated
    with it. If any of the information is not present, it returns "n/a". This is
    useful for organizations who want to analyze product reviews in order to
    identify and prioritize the most important issues.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.REVIEW_TAGGER
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str) -> dict:
        '''
        Call the Review Tagger Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: The review text.
        :return: object: The faulty object. This could be the product itself, or a component, e.g.
            'door handle'. If 'n/a' is returned, it's assumed that the object is the
            product itself.
        action: The action/verb associated with that object, e.g. 'squeaks'
        fault: The fault (or strength) of the object, e.g. 'loose' or 'broken'.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/review_tagger.py>`_
        '''
        return super().__call__(user=user, text=text)

    def set_input_configs(self, name:str, text:Union[str, InputConfig]):
        super().set_input_configs(name=name, text=text)

    @classmethod
    def call(self, user:str, text:str) -> dict:
        '''
        Call the Review Tagger Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: The review text.
        :return: object: The faulty object. This could be the product itself, or a component, e.g.
            'door handle'. If 'n/a' is returned, it's assumed that the object is the
            product itself.
        action: The action/verb associated with that object, e.g. 'squeaks'
        fault: The fault (or strength) of the object, e.g. 'loose' or 'broken'.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/review_tagger.py>`_
        '''
        return super().call(user=user, text=text)



class SearchRecommendationsService(SoffosAIService):
    '''
    General HTTP service client.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.SEARCH_RECOMMENDATIONS
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str, document_ids:list) -> dict:
        '''
        Call the Search Recommendations Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: None
        :param document_ids: None
        :return: recommendations: None
        recommendations_no_info: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/search_recommendations.py>`_
        '''
        return super().__call__(user=user, text=text, document_ids=document_ids)

    def set_input_configs(self, name:str, text:Union[str, InputConfig], document_ids:Union[list, InputConfig]):
        super().set_input_configs(name=name, text=text, document_ids=document_ids)

    @classmethod
    def call(self, user:str, text:str, document_ids:list) -> dict:
        '''
        Call the Search Recommendations Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: None
        :param document_ids: None
        :return: recommendations: None
        recommendations_no_info: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/search_recommendations.py>`_
        '''
        return super().call(user=user, text=text, document_ids=document_ids)



class SentimentAnalysisService(SoffosAIService):
    '''
    This module processes the text to measure whether it is negative, positive or
    neutral. The text is processed in segments of user-defined length and it
    provides scores for each segment as well as the overall score of the whole
    text.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.SENTIMENT_ANALYSIS
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str, sentence_split:int=4, sentence_overlap:bool=None) -> dict:
        '''
        Call the Sentiment Analysis Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to be analyzed for sentiment.
        :param sentence_split: The number of sentences of each chunk when splitting the input text.
        :param sentence_overlap: Whether to overlap adjacent chunks by 1 sentence. For example, with
            sentence_split=3 and sentence_overlap=true: [[s1, s2, s3], [s3, s4, s5],
            [s5, s6, s7]]
        :return: sentiment_breakdown: A list of dictionaries representing the score of each segment of text.
            Each dictionary contains the following fields: text: The text of the
            segment. start: The starting character index of the segment in the
            original text. end: The ending character index of the segment in the
            original text. sentiment: A dictionary containing the scores for negative,
            neutral and positive.
        sentiment_overall: Contains the overall negative, neutral and positive score for the provided
            text.
        sentiment: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/sentiment_analysis.py>`_
        '''
        return super().__call__(user=user, text=text, sentence_split=sentence_split, sentence_overlap=sentence_overlap)

    def set_input_configs(self, name:str, text:Union[str, InputConfig], sentence_split:Union[int, InputConfig]=4, sentence_overlap:Union[bool, InputConfig]=None):
        super().set_input_configs(name=name, text=text, sentence_split=sentence_split, sentence_overlap=sentence_overlap)

    @classmethod
    def call(self, user:str, text:str, sentence_split:int=4, sentence_overlap:bool=None) -> dict:
        '''
        Call the Sentiment Analysis Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to be analyzed for sentiment.
        :param sentence_split: The number of sentences of each chunk when splitting the input text.
        :param sentence_overlap: Whether to overlap adjacent chunks by 1 sentence. For example, with
            sentence_split=3 and sentence_overlap=true: [[s1, s2, s3], [s3, s4, s5],
            [s5, s6, s7]]
        :return: sentiment_breakdown: A list of dictionaries representing the score of each segment of text.
            Each dictionary contains the following fields: text: The text of the
            segment. start: The starting character index of the segment in the
            original text. end: The ending character index of the segment in the
            original text. sentiment: A dictionary containing the scores for negative,
            neutral and positive.
        sentiment_overall: Contains the overall negative, neutral and positive score for the provided
            text.
        sentiment: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/sentiment_analysis.py>`_
        '''
        return super().call(user=user, text=text, sentence_split=sentence_split, sentence_overlap=sentence_overlap)


class SimplifyService(SoffosAIService):
    '''
    Paraphrase and Simplify are available as two different flavors of the same
    module. While the Paraphrase module attempts to change the wording while
    keeping the same level of complexity, the Simplify module outputs more commonly
    used words without altering the meaning of the original text.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.SIMPLIFY
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str) -> dict:
        '''
        Call the Simplify Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to be paraphrased/simplified.
        :return: paraphrase: None
        simplify: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/simplify.py>`_
        '''
        return super().__call__(user=user, text=text)

    def set_input_configs(self, name:str, text:Union[str, InputConfig]):
        super().set_input_configs(name=name, text=text)

    @classmethod
    def call(self, user:str, text:str) -> dict:
        '''
        Call the Simplify Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to be paraphrased/simplified.
        :return: paraphrase: None
        simplify: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/simplify.py>`_
        '''
        return super().call(user=user, text=text)



class StringSimilarityService(SoffosAIService):
    '''
    This module measures the similarity in meaning between two strings. It also
    returns text spans that are similar between the two string, which can be useful
    for highlighting. Although the service accepts srtings up to 5000 characters
    long, it is intended for smaller strings and use-cases such as answer scoring,
    given the correct answer and the learner's answer to a question.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.STRING_SIMILARITY
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, a:str, b:str) -> dict:
        '''
        Call the String Similarity Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param a: A string to be compared with `b`. Has a limit of 5000 characters.
        :param b: A string to be compared with `a`. Has a limit of 5000 characters.
        :return: score: A value between `0` and `100` indicating the percentage of similarity
            between the two strings. Since the comparison assesses the similarity in
            entailment/meaning, the score will be very close to 0, or very close to
            100 most of the time. More ambiguous cases are scored somewhere in the
            middle.
        text_spans: A list of dictionaries representing instances where a sub-string of `a` is
            similar to one or more substrings of `b`. Each dictionary contains the
            folowing fields: a_text_span: A dictionary of the span in `a` containing
            its `text` and `span` index offsets. b_text_span: A list of dictionaries
            of all spans similar to `a_text_span`, each containing their `text` and
            `span`.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/string_similarity.py>`_
        '''
        return super().__call__(user=user, a=a, b=b)

    def set_input_configs(self, name:str, a:Union[str, InputConfig], b:Union[str, InputConfig]):
        super().set_input_configs(name=name, a=a, b=b)

    @classmethod
    def call(self, user:str, a:str, b:str) -> dict:
        '''
        Call the String Similarity Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param a: A string to be compared with `b`. Has a limit of 5000 characters.
        :param b: A string to be compared with `a`. Has a limit of 5000 characters.
        :return: score: A value between `0` and `100` indicating the percentage of similarity
            between the two strings. Since the comparison assesses the similarity in
            entailment/meaning, the score will be very close to 0, or very close to
            100 most of the time. More ambiguous cases are scored somewhere in the
            middle.
        text_spans: A list of dictionaries representing instances where a sub-string of `a` is
            similar to one or more substrings of `b`. Each dictionary contains the
            folowing fields: a_text_span: A dictionary of the span in `a` containing
            its `text` and `span` index offsets. b_text_span: A list of dictionaries
            of all spans similar to `a_text_span`, each containing their `text` and
            `span`.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/string_similarity.py>`_
        '''
        return super().call(user=user, a=a, b=b)



class SummarizationService(SoffosAIService):
    '''
    The summarization module utilizes Natural Language Generation (NLG) to generate
    an abstractive summary of a specified length. In contrast to extractive
    summarization methods, which simply calculate the centrality of sentences or
    passages in the original text and concatenate the highest rated ones,
    abstractive summaries are often more concise and accurate. The end result isn't
    necessarily a sum of word-for-word copies of passages from the original text,
    but a combination of all key points formulated as a new text.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.SUMMARIZATION
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str, sent_length:int) -> dict:
        '''
        Call the Summarization Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to be summarized.
        :param sent_length: The desired sentence length of the summary. The service will respond with
            a 403 error if the value is larger than the number of sentences in the
            text.
        :return: summary: The summary.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/summarization.py>`_
        '''
        return super().__call__(user=user, text=text, sent_length=sent_length)

    def set_input_configs(self, name:str, text:Union[str, InputConfig], sent_length:Union[int, InputConfig]):
        super().set_input_configs(name=name, text=text, sent_length=sent_length)

    @classmethod
    def call(self, user:str, text:str, sent_length:int) -> dict:
        '''
        Call the Summarization Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to be summarized.
        :param sent_length: The desired sentence length of the summary. The service will respond with
            a 403 error if the value is larger than the number of sentences in the
            text.
        :return: summary: The summary.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/summarization.py>`_
        '''
        return super().call(user=user, text=text, sent_length=sent_length)


class TableDeleteService(SoffosAIService):
    '''
    General HTTP service client.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.TABLE_DELETE
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, table_ids:list) -> dict:
        '''
        Call the Table Delete Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param table_ids: None
        :return: success: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/table_delete.py>`_
        '''
        return super().__call__(user=user, table_ids=table_ids)

    def set_input_configs(self, name:str, table_ids:Union[list, InputConfig]):
        super().set_input_configs(name=name, table_ids=table_ids)

    @classmethod
    def call(self, user:str, table_ids:list) -> dict:
        '''
        Call the Table Delete Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param table_ids: None
        :return: success: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/table_delete.py>`_
        '''
        return super().call(user=user, table_ids=table_ids)


class TableGeneratorService(SoffosAIService):
    '''
    The table generator module enables applications to extract numerical and
    statistical data from raw text in a tabular format. For use-cases where data
    has to be manually reviewed and cross-referenced, this module can bring
    enormous value.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.TABLE_GENERATOR
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str, table_format:str, topic:str=None) -> dict:
        '''
        Call the Table Generator Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to extract tables from.
        :param table_format: A string indicating the table output format. Formats supported: markdown,
            CSV
        :param topic: None
        :return: tables: A list of dictionaries representing tables. Each dictionary contains the
            following fields: title: A descriptive title for the table table: The
            table in a raw markdown or CSV formatted string. note: Useful notes for
            table interpretation.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/table_generator.py>`_
        '''
        return super().__call__(user=user, text=text, table_format=table_format, topic=topic)

    def set_input_configs(self, name:str, text:Union[str, InputConfig], table_format:Union[str, InputConfig], topic:Union[str, InputConfig]=None):
        super().set_input_configs(name=name, text=text, table_format=table_format, topic=topic)

    @classmethod
    def call(self, user:str, text:str, table_format:str, topic:str=None) -> dict:
        '''
        Call the Table Generator Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to extract tables from.
        :param table_format: A string indicating the table output format. Formats supported: markdown,
            CSV
        :param topic: None
        :return: tables: A list of dictionaries representing tables. Each dictionary contains the
            following fields: title: A descriptive title for the table table: The
            table in a raw markdown or CSV formatted string. note: Useful notes for
            table interpretation.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/table_generator.py>`_
        '''
        return super().call(user=user, text=text, table_format=table_format, topic=topic)


class TableGetService(SoffosAIService):
    '''
    General HTTP service client.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.TABLE_GET
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str) -> dict:
        '''
        Call the Table Get Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :return: tables: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/table_get.py>`_
        '''
        return super().__call__(user=user)

    def set_input_configs(self, name:str):
        super().set_input_configs(name=name)

    @classmethod
    def call(self, user:str) -> dict:
        '''
        Call the Table Get Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :return: tables: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/table_get.py>`_
        '''
        return super().call(user=user)


class TableIngestService(SoffosAIService):
    '''
    General HTTP service client.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.TABLE_INGEST
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, table:list, document_name:str, description:str) -> dict:
        '''
        Call the Table Ingest Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param table: None
        :param document_name: None
        :param description: None
        :return: table_id: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/table_ingest.py>`_
        '''
        return super().__call__(user=user, table=table, document_name=document_name, description=description)

    def set_input_configs(self, name:str, table:Union[list, InputConfig], document_name:Union[str, InputConfig], description:Union[str, InputConfig]):
        super().set_input_configs(name=name, table=table, document_name=document_name, description=description)

    @classmethod
    def call(self, user:str, table:list, document_name:str, description:str) -> dict:
        '''
        Call the Table Ingest Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param table: None
        :param document_name: None
        :param description: None
        :return: table_id: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/table_ingest.py>`_
        '''
        return super().call(user=user, table=table, document_name=document_name, description=description)


class TagService(SoffosAIService):
    '''
    This module can generate tags for a piece of text that can aid with content
    search in certain use-cases. It allows to specify a number of tags to be
    generated for each of the categories "topic", "domain", "audience", "entity".
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.TAG
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str, types:str=None, n:int=None) -> dict:
        '''
        Call the Tag Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to extract keywords from.
        :param types: List of types of keywords to extract. Supported types: topic: Tags
            relating to the subject matter of the text. domain: Tags relating to the
            domain of the text. For example, 'AI', or 'Science fiction'. audience:
            Tags relating to the type of audience the text is intended for. entity:
            Entities such as people, places, products, etc. mentioned in the text.
        :param n: The number of tags to be generated for each of the specified tag types.
        :return: tags: A dictionary containing the tags grouped by the type of tag. A confidence
            score is provided also for each tag.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/tag.py>`_
        '''
        return super().__call__(user=user, text=text, types=types, n=n)

    def set_input_configs(self, name:str, text:Union[str, InputConfig], types:Union[str, InputConfig]=None, n:Union[int, InputConfig]=None):
        super().set_input_configs(name=name, text=text, types=types, n=n)

    @classmethod
    def call(self, user:str, text:str, types:str=None, n:int=None) -> dict:
        '''
        Call the Tag Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to extract keywords from.
        :param types: List of types of keywords to extract. Supported types: topic: Tags
            relating to the subject matter of the text. domain: Tags relating to the
            domain of the text. For example, 'AI', or 'Science fiction'. audience:
            Tags relating to the type of audience the text is intended for. entity:
            Entities such as people, places, products, etc. mentioned in the text.
        :param n: The number of tags to be generated for each of the specified tag types.
        :return: tags: A dictionary containing the tags grouped by the type of tag. A confidence
            score is provided also for each tag.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/tag.py>`_
        '''
        return super().call(user=user, text=text, types=types, n=n)


class TranscriptCorrectionService(SoffosAIService):
    '''
    This module cleans up and corrects poorly transcribed text from Speech-To-Text
    (STT) systems. It can handle cases where STT produced the wrong word or phrase
    by taking into account the surrounding context and choosing the most fitting
    replacement. Although this is meant for correcting STT outpus, it can also be
    used to correct grammar, misspellings and syntactical errors.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.TRANSCRIPT_CORRECTION
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str) -> dict:
        '''
        Call the Transcript Correction Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to be corrected.
        :return: corrected: Corrected text.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/transcript_correction.py>`_
        '''
        return super().__call__(user=user, text=text)

    def set_input_configs(self, name:str, text:Union[str, InputConfig]):
        super().set_input_configs(name=name, text=text)

    @classmethod
    def call(self, user:str, text:str) -> dict:
        '''
        Call the Transcript Correction Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to be corrected.
        :return: corrected: Corrected text.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/transcript_correction.py>`_
        '''
        return super().call(user=user, text=text)


class TranslationService(SoffosAIService):
    '''
    General HTTP service client.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.TRANSLATION
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str, auto_detect:bool=True, source_language_code:str=None, target_language_code:str=None) -> dict:
        '''
        Call the Translation Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Missing Documentation
        :param auto_detect: Missing Documentation
        :param source_language_code: Missing Documentation
        :param target_language_code: Missing Documentation
        :return: target_language_code: Missing Documentation
        translation: Missing Documentation
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/translation.py>`_
        '''
        return super().__call__(user=user, text=text, auto_detect=auto_detect, source_language_code=source_language_code, target_language_code=target_language_code)

    def set_input_configs(self, name:str, text:Union[str, InputConfig], auto_detect:Union[bool, InputConfig]=None, source_language_code:Union[str, InputConfig]=None, target_language_code:Union[str, InputConfig]=None):
        super().set_input_configs(name=name, text=text, auto_detect=auto_detect, source_language_code=source_language_code, target_language_code=target_language_code)

    @classmethod
    def call(self, user:str, text:str, auto_detect:bool=None, source_language_code:str=None, target_language_code:str=None) -> dict:
        '''
        Call the Translation Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Missing Documentation
        :param auto_detect: Missing Documentation
        :param source_language_code: Missing Documentation
        :param target_language_code: Missing Documentation
        :return: target_language_code: Missing Documentation
        translation: Missing Documentation
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/translation.py>`_
        '''
        return super().call(user=user, text=text, auto_detect=auto_detect, source_language_code=source_language_code, target_language_code=target_language_code)


class WebsiteConverterService(SoffosAIService):
    '''
    The Website Converter module offers basic functionality for extracting
    meaningful text from websites. This can be a useful tool for processing website
    content with other modules. Note: Character volume is not charged for this
    module.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.WEBSITE_CONVERTER
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, url:str) -> dict:
        '''
        Call the Website Converter Service
        
        :param user: The ID of the user accessing the Soffos API.
            This string will be used for throttling and profanity tracking.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        :param url: The url to extract text from.
        :return: text: Raw text extracted from the website.
        links: A dictionary containing a list of `internal` and a list of
            `external` links found on the website. `internal`: Links found
            on the page that are under the same domain as the provided url.
            `external`: Links found on the page that belong to different
            domains.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/website_converter.py>`_
        '''
        return super().__call__(user=user, url=url)

    def set_input_configs(self, name:str, url:Union[str, InputConfig]):
        super().set_input_configs(name=name, url=url)

    @classmethod
    def call(self, user:str, url:str) -> dict:
        '''
        Call the Website Converter Service
        
        :param user: The ID of the user accessing the Soffos API.
            This string will be used for throttling and profanity tracking.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        :param url: The url to extract text from.
        :return: text: Raw text extracted from the website.
        links: A dictionary containing a list of `internal` and a list of
            `external` links found on the website. `internal`: Links found
            on the page that are under the same domain as the provided url.
            `external`: Links found on the page that belong to different
            domains.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/website_converter.py>`_
        '''
        return super().call(user=user, url=url)

def is_service_input(value):
    if not isinstance(value, dict):
        return False
    return "source" in value and "field" in value


class SoffosPipeline:
    '''
    A controller for consuming multiple Services called stages.
    It validates all inputs of all stages before sending the first Soffos API request to ensure
    that the Pipeline will not waste credits.
    
    ** use_defaults=True means that stages will take input from the previous stages' 
    output of the same field name prioritizing the latest stage's output. 
    If the previous stages does not have it, it will take from the
    pipeline's user_input.  Also, the stages will only be supplied with the required fields + default
    of the require_one_of_choice fields.
    '''
    def __init__(self, services:List[SoffosAIService], use_defaults:bool=False, name=None, **kwargs) -> None:
        self._apikey = kwargs['apikey'] if kwargs.get('apikey') else soffosai.api_key
        self._stages = services
        
        self._input:dict = {}
        self._infos = []
        self._use_defaults = use_defaults
        self._execution_codes = []
        self._termination_codes = []

        error_messages = []
        if not isinstance(services, list):
            error_messages.append('stages field should be a list of SoffosAIService instances')

        service_names = [service.name for service in services]
        for service in services:
            if not isinstance(service, SoffosAIService) and not isinstance(service, SoffosPipeline):
                error_messages.append(f'{service} is not an instance of SoffosAIService or SoffosPipeline.')
            
            if service_names.count(service.name) > 1:
                error_messages.append(f"Service name '{service.name}' is not unique.")

        if len(error_messages) > 0:
            raise ValueError("\\n".join(error_messages))

        # when a pipeline is used as another pipeline's input, it needs a name
        self.name = name

    
    def run(self, user_input):
        original_user_input = user_input.copy()
        if not isinstance(user_input, dict):
            raise ValueError("User input should be a dictionary.")

        if "user" not in user_input:
            raise ReferenceError("'user' is not defined in the user_input.")

        if "text" in user_input:
            user_input['document_text'] = user_input['text']

        if "question" in user_input:
            user_input['message'] = user_input['question']

        if self._use_defaults:
            stages = self.set_defaults(self._stages, user_input)
        else:
            stages = self._stages

        self.validate_pipeline(stages, user_input)

        # termination referencing
        execution_code = user_input.get("execution_code")
        if execution_code:
            execution_code = self._apikey + execution_code
            if execution_code in self._execution_codes:
                raise ValueError("This execution code is still being used in an existing pipeline run.")
            else:
                self._execution_codes.append(execution_code)

        # Initialization of values
        infos = {}
        infos['user_input'] = user_input
        total_cost = 0.00

        # Execute per stage
        for stage in stages:
            # premature termination
            if execution_code in self._termination_codes:
                self._termination_codes.remove(execution_code)
                self._execution_codes.remove(execution_code)
                infos['total_cost'] = total_cost
                infos['warning'] = "This Soffos Pipeline has been prematurely terminated"
                infos['user_input'] = original_user_input
                return infos

            if isinstance(stage, SoffosPipeline):
                stage: SoffosPipeline
                response = stage.run(user_input)
                print(f"Response ready for {stage.name}.")
                pipe_output = {
                    'costs': {}
                }
                for key, value in response.items():
                    if key != 'total_call_cost':
                        for subkey, subvalue in value.items():
                            if subkey == 'cost':
                                pipe_output['costs'][key] = subvalue
                            elif subkey == 'charged_character_count':
                                pipe_output['costs'][key]['charged_character_count'] = subvalue
                            elif subkey == 'unit_price':
                                pipe_output['costs'][key]['unit_price'] = subvalue
                            else:
                                pipe_output[subkey] = subvalue
                    else:
                        total_cost += value
                infos[stage.name] = pipe_output
                continue

            stage: SoffosAIService
            # execute
            print(f"running {stage.name}.")
            tmp_source: dict = stage.source
            payload = {}
            for key, notation in tmp_source.items():
                # prepare payload
                if isinstance(notation, InputConfig):
                    input_dict = {
                        "source": notation.source,
                        "field": notation.field,
                    }
                    if notation.pre_process:
                        input_dict['pre_process'] = notation.pre_process
                    notation = input_dict
                
                if is_service_input(notation): # value is pointing to another Service
                    value = infos[notation['source']][notation['field']]
                    if "pre_process" in notation:
                        if callable(notation['pre_process']):
                            payload[key] = notation['pre_process'](value)
                        else:
                            raise ValueError(f"{stage.name}: pre_process value should be a function.")
                    
                    else:
                        payload[key] = value
                else:
                    payload[key] = notation

            if 'user' not in payload:
                payload["user"] = user_input['user']
            
            payload['apikey'] = self._apikey
            cleaned_payload = stage.clean_payload(payload)
            response = stage.get_response(cleaned_payload)
            if "error" in response:
                infos[stage.name] = response
                infos['total_cost'] = total_cost
                return infos
            
            print(f"Response ready for {stage.name}")
            infos[stage.name] = response
            total_cost += response['cost']['total_cost']

        infos['total_cost'] = total_cost
        infos["user_input"] = original_user_input

        # remove this execution code from execution codes in effect:
        if execution_code:
            self._execution_codes.remove(execution_code)

        return infos


    def validate_pipeline(self, stages, user_input):
        '''
        Before running the first service, the Pipeline will validate all SoffosAIServices if they will all be
        executed successfully with the exception of database and server issues.
        '''
        if not isinstance(user_input, dict):
            raise ValueError("User input should be a dictionary.")

        if "user" not in user_input:
            raise ReferenceError("'user' is not defined in the user_input.")

        if "text" in user_input:
            user_input['document_text'] = user_input['text']

        error_messages = []

        for stage in stages:
            if isinstance(stage, SoffosPipeline):
                stage:SoffosPipeline
                
                if stage._use_defaults:
                    sub_pipe_stages = stage.set_defaults(stage._stages, user_input)
                else:
                    sub_pipe_stages = stage._stages

                stage.validate_pipeline(sub_pipe_stages, user_input)
                continue

            # If stage is a SoffosAIService:
            stage: SoffosAIService
            serviceio = stage._serviceio
            # checking required_input_fields is already handled in the Service's set_input_configs method

            # check if require_one_of_choices is present and not more than one
            if len(serviceio.require_one_of_choice) > 0:
                group_errors = []
                for group in serviceio.require_one_of_choice:
                    found_choices = [choice for choice in group if choice in stage.source]
                    if not found_choices:
                        group_errors.append(f"{stage.name}: Please provide one of these values on your payload: {group}.")
                    elif len(found_choices) > 1:
                        group_errors.append(f"Please include only one of these values: {group}.")
                    
                if len(group_errors) > 0:
                    error_messages.append(". ".join(group_errors))
            
            # check if datatypes are correct:
            for key, notation in stage.source.items():
                required_datatype = serviceio.input_structure.get(key)
                if not required_datatype:
                    continue
                required_datatype = self.get_serviceio_datatype(required_datatype)
                
                # convert InputConfig to dict
                if isinstance(notation, InputConfig): # backwards compatibility
                    input_dict = {
                        "source": notation.source,
                        "field": notation.field,
                    }
                    if notation.pre_process:
                        input_dict['pre_process'] = notation.pre_process
                    notation = input_dict

                if is_service_input(notation):
                    if "pre_process" in notation:
                        continue # will not check for type if there is a helper function
                    
                    if notation['source'] == "user_input":
                        user_input_type = type(user_input[notation['field']])
                        if required_datatype == tuple:
                            allowed_data_types = list(stage._serviceio.input_structure[key])
                            allowed_data_types_str = " or ".join([t.__name__ for t in allowed_data_types])
                            if user_input_type not in allowed_data_types:
                                if notation['field'] == "file":
                                    # TODO: special handling because django, flask, fast api, and regular python has different datatypes for in memory files.
                                    # TODO: should create list of datatypes and put in on file fields of serviceio of all services accepting file
                                    pass
                                else:
                                    error_messages.append(f"{stage.name}:  {user_input_type} required for '{key}' field: but {user_input_type} is provided.")
                        else:
                            if user_input_type != required_datatype:
                                if notation['field'] == "file":
                                    # TODO: special handling because django, flask, fast api, and regular python has different datatypes for in memory files.
                                    pass
                                else:
                                    error_messages.append(f"{stage.name}: {required_datatype} required on user_input '{key}' field but {user_input_type} is provided.")
                    else:
                        source_found = False
                        for subservice in stages:
                            subservice: SoffosAIService
                            if notation['source'] == subservice.name:
                                source_found = True
                                if isinstance(subservice, SoffosPipeline):
                                    break  
                                output_datatype = self.get_serviceio_datatype(subservice._serviceio.output_structure[notation['field']])
                                
                                if type(output_datatype) == tuple:
                                    allowed_data_types = list(stage._serviceio.input_structure[key])
                                    allowed_data_types_str = " or ".join([t.__name__ for t in allowed_data_types])
                                    if user_input_type not in allowed_data_types:
                                        if notation['field'] == "file":
                                            # TODO: special handling because django, flask, fast api, and regular python has different datatypes for in memory files.
                                            # TODO: should create list of datatypes and put in on file fields of serviceio of all services accepting file
                                            pass
                                        else:
                                            error_messages.append(f"{stage.name}:  {user_input_type} required for '{key}' field: but {user_input_type} is provided.")

                                elif output_datatype != required_datatype:
                                    error_messages.append(f"On {stage.name} service: The input datatype required for field ${key} is {required_datatype}. This does not match the datatype to be given by service {subservice.name}'s {notation['field']} field which is {output_datatype}.")
                                break
                        if not source_found:
                            error_messages.append(f"Cannot find service '{notation['source']}'")
                
                else:
                    if required_datatype == tuple:
                        allowed_data_types = list(stage.service._serviceio.input_structure[key])
                        allowed_data_types_str = " or ".join([t.__name__ for t in allowed_data_types])
                        if notation['field'] == "file":
                            # TODO: special handling because django, flask, fast api, and regular python has different datatypes for in memory files.
                            # TODO: should create list of datatypes and put in on file fields of serviceio of all services accepting file
                            pass
                        else:
                            if type(notation) not in allowed_data_types:
                                error_messages.append(f"{stage.name}: {allowed_data_types_str} required for user_input '{key}' field:  but {type(notation).__name__} is provided.")
                    else:
                        if type(notation) != required_datatype and notation!= None:
                            error_messages.append(f"On {stage.name} service: {key} requires ${required_datatype} but ${type(notation)} is provided.")

        if len(error_messages) > 0:
            raise ValueError(error_messages)
        
        return True


    def add_service(self, service):
        if isinstance(service, SoffosAIService) or isinstance(service, SoffosPipeline):
            self._stages.append(service)
        else:
            raise ValueError(f"{service} is not a SoffosAIService instance")

    
    def set_defaults(self, stages, user_input):
        defaulted_stages = []
        for i, stage in enumerate(stages):
            if isinstance(stage, SoffosPipeline):
                continue

            stage: SoffosAIService
            stage_source = {}
            required_keys = stage._serviceio.required_input_fields
            require_one_choices = stage._serviceio.require_one_of_choice
            if len(require_one_choices) > 0:
                for choices in require_one_choices:
                    required_keys.append(choices[0]) # the default argument is the first one
            
            for required_key in required_keys:
                check_key = stage.source.get(required_key)
                if check_key and check_key != "default":
                    stage_source[required_key] = check_key
                    continue

                found_input = False
                for j in range(i-1, -1, -1):
                    stage_for_output:SoffosAIService = stages[j]
                    stage_for_output_output_fields = stage_for_output._serviceio.output_structure
                    if required_key in stage_for_output_output_fields:
                        stage_source[required_key] = {
                            "source": stage_for_output.name,
                            "field": required_key
                        }
                        found_input = True
                
                    # special considerations:
                    elif required_key == "context" and "text" in stage_for_output_output_fields:
                        stage_source["context"] = {
                            "source": stage_for_output.name,
                            "field": "text"
                        }
                        found_input = True

                    elif required_key == "document_text" and "text" in stage_for_output_output_fields:
                        stage_source["document_text"] = {
                            "source": stage_for_output.name,
                            "field": "text"
                        }
                        found_input = True
                    
                if not found_input:
                    if required_key in user_input:
                        stage_source[required_key] = user_input[required_key]
                        stage_source[required_key] = {
                            "source": "user_input",
                            "field": required_key
                        }
                    else:
                        raise ReferenceError(f"Please add {required_key} to user input. The previous Services' outputs do not provide this data.")

            defaulted_stage = stage.set_input_configs(stage.name, stage_source)
            defaulted_stages.append(defaulted_stage)
        
        return defaulted_stages

    
    def terminate(self, termination_code):
        if termination_code:
            self._termination_codes.append(self._apikey + termination_code)
            return {"message": f"Request to terminate job {termination_code} received."}

        return {"message": f"Request to terminate job is not valid (execution code missing)."}


    def get_serviceio_datatype(self, key):
        if isinstance(key, type):
            return key
        return type(key)
    
    def __call__(self, **kwargs):
        return self.run(kwargs)


def get_text_from_passages(passages):
    text = ""
    for passage in passages:
        text = text + passage['content']
    return text


class DocumentSummaryPipeline(SoffosPipeline):
    '''
    A Soffos Pipeline that takes document_ids, then summarizes the content.
    The output is a list containing the output object of file converter and summarization.
    '''
    def __init__(self, **kwargs) -> None:
        document_search = DocumentsSearchService().set_input_configs(
            name = "doc_search",
            document_ids= {"source": "user_input", "field": "document_ids"}
        )
        
        summarization = SummarizationService().set_input_configs(
            name = "summarization",
            text = InputConfig("doc_search", "passages", get_text_from_passages),
            sent_length = InputConfig("user_input", "sent_length")
        )

        services = [document_search, summarization]
        use_defaults = False
        super().__init__(services=services, use_defaults=use_defaults, **kwargs)


    def __call__(self, user, document_ids, sent_length):
        return super().__call__(user=user, document_ids=document_ids, sent_length=sent_length)
