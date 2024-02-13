import azure.functions as func
import logging
from utils.line import line_handler, handler


app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="line_endpoint")
def line_endpoint(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    signature = req.headers['X-Line-Signature']
    logging.info(signature)

    body = req.get_json()
    logging.info("Request body: " + body)

    line_handler(signature, body)
    
    return 'OK'



    return func.HttpResponse("cape", status_code=200)


# @app.route(route="line_endpoint")
# def line_endpoint(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')
#
#     name = req.params.get('name')
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')
#
#     if name:
#         return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
#     else:
#         return func.HttpResponse(
#              "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
#              status_code=200
#         )