import json


try:
    from app import app
    import unittest
except Exception   as e :
    print("Some modules are missing ")



class FlaskTest(unittest.TestCase):
    
    
    # A value which is not present in DB will trigger a call to Nominatim
    def test_trigger_api(self):
        tester = app.test_client(self)
        response = tester.get('/get_address/-34.44076/-60.70521?mock=true')
        statuscode = response.status_code
        self.assertEqual(statuscode,202)

    # A subsequent call for same value wont trigger a call to Nominatim
    def test_trigger_cache(self):
        tester = app.test_client(self)
        response = tester.get('/get_address/-34.44076/-60.70521?mock=true')
        response_data = json.loads(response.text)
        self.assertEqual(response_data.get('lookup'),"CACHE")

    # A call for a value which is present in DB but is older than a day will trigger a call to Nominatim.

    # check for response 200 
    def test_staus200 (self):
        tester = app.test_client(self)
        response = tester.get('/get_address/-34.44076/-58.70521')
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    # check if response if coordinates are wrong/not found
    def test_status_nf(self):
        tester = app.test_client(self)
        response = tester.get('/get_address/-34.44076/1234')
        statuscode = response.status_code
        self.assertEqual(statuscode,404)
    

        
   
    

if __name__ == "__main__":
    unittest.main()