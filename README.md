# sat-bot-backed

API Endpoints:-

1. api/upload/
   Methods- POST, 
   for ex: curl -X POST -F "pdf_file=@C:/Users/singl/OneDrive/Desktop/pdf.pdf" http://localhost:8080/api/upload/
   creates a vecotr db of the pdf uploaded and stores the embeddings locally 
