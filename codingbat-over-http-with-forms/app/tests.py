from django.test import SimpleTestCase


class TestFrontTimesView(SimpleTestCase):
    def test_chocolate_front_times_2(self):
        response = self.client.get(
            "/warmup-2/front-times/", {"string": "Chocolate", "integer": 2}
        )
        self.assertContains(response, "ChoCho")

    def test_chocolate_front_times_3(self):
        response = self.client.get(
            "/warmup-2/front-times/", {"string": "Chocolate", "integer": 3}
        )
        self.assertContains(response, "ChoChoCho")

    def test_abc_front_times_3(self):
        response = self.client.get(
            "/warmup-2/front-times/", {"string": "Abc", "integer": 3}
        )
        self.assertContains(response, "AbcAbcAbc")


class TestNoTeenView(SimpleTestCase):
    def test_no_teen_sum_1(self):
        response = self.client.get(
            "/logic-2/no-teen-sum/", {"integer_1": 1, "integer_2": 2, "integer_3": 3}
        )
        self.assertContains(response, "6")

    def test_no_teen_sum_2(self):
        response = self.client.get(
            "/logic-2/no-teen-sum/", {"integer_1": 2, "integer_2": 13, "integer_3": 1}
        )
        self.assertContains(response, "3")

    def test_no_teen_sum_3(self):
        response = self.client.get(
            "/logic-2/no-teen-sum/", {"integer_1": 2, "integer_2": 1, "integer_3": 14}
        )
        self.assertContains(response, "3")


class TestXYZThereView(SimpleTestCase):
    def test_xyz_there_true(self):
        response = self.client.get("/string-2/xyz-there/", {"string": "abcxyz"})
        self.assertContains(response, "True")

    def test_xyz_there_false_1(self):
        response = self.client.get("/string-2/xyz-there/", {"string": "abc.xyz"})
        self.assertContains(response, "False")

    def test_xyz_there_true_2(self):
        response = self.client.get("/string-2/xyz-there/", {"string": "xyz.abc"})
        self.assertContains(response, "True")


class TestCenteredAverageView(SimpleTestCase):
    def test_centered_average_1(self):
        response = self.client.get("/list-2/centered-average/", {"nums": "1,2,3,4,100"})
        self.assertContains(response, "3")

    def test_centered_average_2(self):
        response = self.client.get(
            "/list-2/centered-average/", {"nums": "1,1,5,5,10,8,7"}
        )
        self.assertContains(response, "5")

    def test_centered_average_3(self):
        response = self.client.get(
            "/list-2/centered-average/", {"nums": "-10,-4,-2,-4,-2,0"}
        )
        self.assertContains(response, "-3")
