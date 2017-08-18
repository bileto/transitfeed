# Unit tests for the stopexternalids module.
from __future__ import absolute_import
from tests import util
import transitfeed


class StopExternalIdsValidationTestCase(util.ValidationTestCase):
    def runTest(self):
        stop_ext_id = transitfeed.StopExternalIds()
        stop_ext_id.stop_id = '123456'
        stop_ext_id.type = 'cis'
        stop_ext_id.id = '56098'
        stop_ext_id.Validate(self.problems)
        self.accumulator.AssertNoMoreExceptions()

        # TODO: PROBLEM..
        # stop_ext_id.id = None
        # self.ValidateAndExpectMissingValue(stop_ext_id, 'id')
        # stop_ext_id.id = '56098'

        stop_ext_id.id = 'X'
        self.ValidateAndExpectInvalidValue(stop_ext_id, 'id')
        stop_ext_id.id = '56098'

        # success case
        stop_ext_id = transitfeed.StopExternalIds(stop_id='123456', type='cis', id='59035')
        self.ExpectNoProblems(stop_ext_id)

        # TODO: NO IDEA WHERE IS THE PROBLEM.. AND WHY GOOGLE CODE IS SO UGLY
        # bad agency
        # stop_ext_id = transitfeed.StopExternalIds(stop_id='123456', type='cis', id='')
        # self.ValidateAndExpectMissingValue(stop_ext_id, 'id')
