from tornado.web import RequestHandler


class NotFoundHandler(RequestHandler):
  def get(self):
    self.render("404.html")
