class TestPersonalInfo:
    def return_name(self):
        return "jason"
    
    def return_age(self):
        return 25
    
    def return_job(self):
        return "engineer"
    def setup(self):
        print("this is the setup function.")
    def teardown(self):
        print("this is the tear down function.")
    def test_1(self):
        assert self.return_name() == "jason"
        assert self.return_age() == 25
        assert self.return_job() == "engineer"
    
    def test_2(self):
        assert self.return_name() == "jason"
        assert self.return_age() == 25
        assert self.return_job() == "engineer"