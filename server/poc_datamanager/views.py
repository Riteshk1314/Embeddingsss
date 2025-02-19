import os
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PDFUploadSerializer
from .utils import process_pdf
from langchain_core.messages import HumanMessage
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import time
# from langchain_chroma import Chroma
# from langchain_openai import OpenAIEmbeddings
class PDFUploadView(APIView):
    def post(self, request, format=None):
        serializer = PDFUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            pdf_file = serializer.data['pdf_file']
            pdf_file = pdf_file.replace('/media', '').replace('\\', '/')
            pdf_path = settings.MEDIA_ROOT + pdf_file
            print(pdf_path)
            
            start_time = time.time()
            process_pdf(pdf_path)
            end_time = time.time()
            
            print(f"Time taken to process PDF: {end_time - start_time} seconds")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
# class ChatBot(APIView):
#     SYSTEM_TEMPLATE = """
#     Answer the user's questions based on the below context. 
#     If the context doesn't contain any relevant information to the question, don't make something up and just say "I don't know":

#     <context>
#     {context}
#     </context>
#     """
#     chat = "add a model here "
#     docs = WebBaseLoader().load()
#     question_answering_prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             SYSTEM_TEMPLATE,
#         ),
#         MessagesPlaceholder(variable_name="messages"),
#     ]
# )

#     document_chain = create_stuff_documents_chain(chat, question_answering_prompt)
#     document_chain.invoke(
#         {
#             "context": docs,
#             "messages": [
#                 HumanMessage(content="Can LangSmith help test my LLM applications?")
#             ],
#         }
#     )
#     def post(self, request, format=None):
#         return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
#     def get(self, request):
#         return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)