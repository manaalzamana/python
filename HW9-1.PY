import psutil
from wsgiref.simple_server import make_server

vmem= psutil.cpu_times()


def hello_world_app(environ, start_response):
	message=""
	status = '200 OK'
	headers = [('Content-type', 'html; charset=utf-8')]
	start_response(status, headers)
	message += "<h1>CPU Times</h1>"
	message += ("<table width='40%' border=0><tr><td>User : </td><td>"+str(vmem.user)+"</td>")
	message += ("</tr><tr><td>NICE information: </td><td>"+str(vmem.nice)+"</td>")
	message += ("<tr><td>SYSTEM :</td></tr><td>"+str(vmem.system)+"</td>")
	message += ("<tr><td>idle information: </td><td>"+str(vmem.idle)+"</td></table>")
	return[bytes(message,'utf-8')]

httpd = make_server('', 8000, hello_world_app)
print("Serving on port 8000...")


httpd.serve_forever()
