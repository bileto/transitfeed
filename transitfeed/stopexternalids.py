import util
from gtfsobjectbase import GtfsObjectBase

class StopExternalIds(GtfsObjectBase):
    """Model and validation for stop_external_ids.txt."""

    _REQUIRED_FIELD_NAMES = ["stop_id", "type", "id"]
    _FIELD_NAMES = _REQUIRED_FIELD_NAMES
    _DEPRECATED_FIELD_NAMES = []
    _TABLE_NAME = 'stop_external_ids'

    def __init__(self, stop_id=None, type=None, id=None, field_dict=None, **kwargs):
        self._schedule = None
        if not field_dict:
            if stop_id:
                kwargs['stop_id'] = stop_id
            if id:
                kwargs['id'] = id
            if type:
                kwargs['type'] = type
            field_dict = kwargs
        self.__dict__.update(field_dict)

    def ValidateStopExternalIdsMissingId(self, problems):
        if not self.id:
            problems.MissingValue('id')
        if self.id is not None:
            value = self.id
            try:
                if not isinstance(value, int):
                    self.id = util.FloatStringToFloat(value, problems)
            except (ValueError, TypeError):
                problems.InvalidValue('id', value)
                del self.id

    def Validate(self, problems):
        found_problem = False
        found_problem = ((not util.ValidateRequiredFieldsAreNotEmpty(
                        self, self._REQUIRED_FIELD_NAMES, problems))
                         or found_problem)
        found_problem = self.ValidateStopExternalIdsMissingId(problems) or found_problem
        return not found_problem

    def ValidateBeforeAdd(self, problems):
        return True

    def ValidateAfterAdd(self, problems):
        self.Validate(problems)

