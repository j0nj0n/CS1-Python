#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrSum as corr
import sum


class TestSum(unittest.TestCase):
    def test_sum(self):
        a = [random.randint(1, 100) for _ in range(5)]
        ans = _("The sum of the {} first integers is {} and you returned {}.")
        for i in range(len(a)):
            stu_ans = sum.sum(a[i])
            corr_ans = corr.sum(a[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(a[i], corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
