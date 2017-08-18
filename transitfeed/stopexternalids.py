import transitfeed
import problems as problems_module

class StopExternalIds(transitfeed.GtfsObjectBase):
    """Model and validation for stop_external_ids.txt."""

    _REQUIRED_FIELD_NAMES = ["stop_id", "type", "id"]
    _FIELD_NAMES = _REQUIRED_FIELD_NAMES
    _DEPRECATED_FIELD_NAMES = []
    _TABLE_NAME = 'stop_external_ids'

    def __init__(self, field_dict=None):
        self._schedule = None
        if field_dict:
            self.__dict__.update(field_dict)

    # def ValidateStopExternalIdsStopId(self, problems):
    #     return not transitfeed.ValidateLanguageCode(self.stop_id, 'stop_id', problems)

    # def ValidateStopExternalIdsType(self, problems):
    #     return not transitfeed.ValidateURL(self.type, 'type', problems)

    def ValidateStopExternalIdsId(self, problems):
        return not transitfeed.MissingValue(self.type, 'type', problems)

    def ValidateBeforeAdd(self, problems):
        transitfeed.ValidateRequiredFieldsAreNotEmpty(self,
                                                      self._REQUIRED_FIELD_NAMES,
                                                      problems)
        # self.ValidateStopExternalIdsStopId(problems)
        # self.ValidateStopExternalIdsType(problems)
        # self.ValidateStopExternalIdsId(problems)
        return True  # none of the above validations is blocking

    def ValidateAfterAdd(self, problems):
        return

    def Validate(self, problems=problems_module.default_problem_reporter):
        self.ValidateBeforeAdd(problems)
        self.ValidateAfterAdd(problems)
