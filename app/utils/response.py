class Response:
    @staticmethod
    def success(status, message, data):
        return {
        "status": status, 
        "message": message, 
        "data": data, 
        "errors": None
        }
    
    @staticmethod
    def error(status, message, errors):
        return {
        "status": status, 
        "message": message, 
        "data": None, 
        "errors": errors
        }