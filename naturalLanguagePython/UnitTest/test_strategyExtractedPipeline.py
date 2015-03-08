from unittest import TestCase

__author__ = 'Antoine'


class TestStrategyExtractedPipeline(TestCase):

    def test_extractStrategyWhenHavingNoSpecifiedStrategyInQuestionShouldReturnEmptyList(self):
        strategyExtractedPipeline = StrategyExtractedPipeline()