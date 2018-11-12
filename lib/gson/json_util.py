import calendar
import datetime
from .timestamp import Timestamp


def default(obj):
    if isinstance(obj, datetime.datetime):
        if obj.utcoffset() is not None:
            obj = obj - obj.utcoffset()
        millis = int(calendar.timegm(obj.timetuple()) * 1000 +
                     obj.microsecond / 1000)
        return {"$date": millis}
    if isinstance(obj, Timestamp):
        return {"t": obj.time, "i": obj.inc}
    raise TypeError("%r is not JSON serializable" % obj)
