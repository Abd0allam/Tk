################################
##Generated with a lot of love##
##    with   EasyPython       ##
##Web site: easycoding.tn     ##
################################
from http.server import BaseHTTPRequestHandler, HTTPServer
from multiprocessing import pool, process
import multiprocessing as mp
from threading import Timer
from time import sleep
import time
import timer
import queue
Request = None
MyFile = None

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global Request, MyFile
    messagetosend = bytes('welcome !',"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    Request = self.requestline
    Request = Request[5 : int(len(Request)-9)]
    print('your request is ')
    print(Request)
    MyFile = open('data.csv','a')
    MyFile.write((''.join([str(x) for x in ['', Request, '\n']])))
    MyFile.close()
    return


print('starting server ......')
server_address_httpd = ('192.168.1.146',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)

# httpd.serve_forever()
# if __name__=='__main__':
#   p=multiprocessing.Process(target=httpd,name="esraa",args=(10,))
#   # p.start()
#   time.sleep(10)
#   p.terminate()
#   p.join()

pool=mp.Pool()
q=queue.Queue()

pool.map(httpd,(q,))