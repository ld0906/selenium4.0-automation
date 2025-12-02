class TestPersonalInfo:
    def return_name(self):
        return "jason"
    
    def return_age(self):
        return 25
    
    def return_job(self):
        return "engineer"
    def test_1(self):
        assert self.return_name() == "jason"
        assert self.return_age() == 25
        assert self.return_job() == "engineer"
