from hamcrest import equal_to, assert_that


class SecondSteps():
    def verify_stuff(self):
        assert_that(1, equal_to(1))
        pass
