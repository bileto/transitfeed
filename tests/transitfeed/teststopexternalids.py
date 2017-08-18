# Unit tests for the stopexternalids module.
from __future__ import absolute_import
from tests import util
import transitfeed


class StopExternalIdsValidationTestCase(util.ValidationTestCase):
  def runTest(self):
    # success case
    stop_ext_id = transitfeed.StopExternalIds()
    repr(stop_ext_id)  # shouldn't crash
    stop_ext_id.stop_id = '123456'
    stop_ext_id.type = 'cis'
    stop_ext_id.id = '56098'
    repr(stop_ext_id)  # shouldn't crash
    stop_ext_id.Validate(self.problems)

    stop_ext_id.id = ''
    self.ValidateAndExpectMissingValue(stop_ext_id, 'id')
    stop_ext_id.id = '56098'
