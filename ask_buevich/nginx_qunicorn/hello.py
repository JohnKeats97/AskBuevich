from pprint import pformat
from cgi import parse_qsl

def application(environ, start_response):
	str = ""
	if environ.get("REQUEST_METHOD") == 'GET' and environ["QUERY_STRING"]:
		str += environ["QUERY_STRING"] + '\n'
		print("Get = ", str)
	if environ["REQUEST_METHOD"] == 'POST' and environ["wsgi.input"]:
		str += environ["wsgi.input"].read() + '\n'
		print("Post = ", str)
	status = '200 OK'
    	response_headers = [('Content-type', 'text/plain')]
    	start_response(status, response_headers)	

	return [str]


