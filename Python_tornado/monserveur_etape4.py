import tornado.httpserver
import tornado.ioloop
import tornado.web
import platform
import datetime


class MainHandler(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	def get(self):
		serverinfo=platform.uname()
		date=datetime.datetime.now()
		date=str(date)
		self.write("%s" % " ".join(serverinfo))
		self.write("%s" % " ".join(date))
		self.finish()

class InfoHandler(tornado.web.RequestHandler):
	def get(self,index):
		serverinfo=platform.uname()
		self.write(serverinfo[int(index)])

application=tornado.web.Application([
	(r"/",MainHandler),
	(r"/info/([0-5]+)",InfoHandler),
	])
if __name__=='__main__':
	http_server=tornado.httpserver.HTTPServer(application)
	http_server.listen(8080)
	tornado.ioloop.IOLoop.instance().start()
	
