
class userDetails:

      def __init__(self, name, email):
        self.name =  name
        self.email = email


      def to_dict(self):
        #convert the instance to a dictionary
      return {"userName": self.name, "collegeEmail": self.email}
