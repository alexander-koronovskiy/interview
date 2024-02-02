# Запуск GUnicorn

'''bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app'''

'''bash uvicorn main:app --reload --port 5000'''
