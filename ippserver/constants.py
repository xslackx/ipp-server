from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

try:
    from enum import IntEnum
except ImportError:
    IntEnum = object


class SectionEnum(IntEnum):
    # delimiters (sections)
    SECTIONS      = 0x00
    SECTIONS_MASK = 0xf0
    operation     = 0x01
    job           = 0x02
    END           = 0x03
    printer       = 0x04
    unsupported   = 0x05

    @classmethod
    def is_section_tag(cls, tag):
        return (tag & cls.SECTIONS_MASK) == cls.SECTIONS


class TagEnum(IntEnum):
    unsupported_value     = 0x10
    unknown_value         = 0x12
    no_value              = 0x13

    # int types
    integer               = 0x21
    boolean               = 0x22
    enum                  = 0x23

    # string types
    octet_str             = 0x30
    datetime_str          = 0x31
    resolution            = 0x32
    range_of_integer      = 0x33
    text_with_language    = 0x35
    name_with_language    = 0x36

    text_without_language = 0x41
    name_without_language = 0x42
    keyword               = 0x44
    uri                   = 0x45
    uri_scheme            = 0x46
    charset               = 0x47
    natural_language      = 0x48
    mime_media_type       = 0x49


class StatusCodeEnum(IntEnum):
    # https://tools.ietf.org/html/rfc2911#section-13.1
    ok = 0x0000
    server_error_internal_error = 0x0500
    server_error_operation_not_supported = 0x0501
    server_error_job_canceled = 0x508
    ok_ignored_or_substituted_attributes = 0x0001
    ok_conflicting_attributes = 0x0002

class StatusClientCodeErrorEnum(IntEnum):
    # https://datatracker.ietf.org/doc/html/rfc2911#section-13.1.4
    bad_request = 0x0400
    forbidden = 0x0401
    not_authenticated = 0x0402
    not_authorized = 0x0403
    timeout = 0x0405
    not_found = 0x0406
    gone = 0x0407
    request_entity_too_large = 0x0408
    request_value_too_long = 0x0409
    document_format_not_supported = 0x040A
    attributes_or_values_not_supported = 0x040B
    uri_scheme_not_supported = 0x040C
    charset_not_supported = 0x040D
    conflicting_attributes = 0x040E
    compression_not_supported = 0x040F
    compression_error = 0x0410
    document_format_error = 0x0411
    document_access_error = 0x0412

class StatusServerCodeErrorEnum(IntEnum):
    # https://datatracker.ietf.org/doc/html/rfc2911#section-13.1.5
    internal_error = 0x0500
    operation_not_supported = 0x0501
    service_unavailable = 0x0502
    version_not_supported = 0x503
    device_error = 0x0504
    temporary_error = 0x0505
    not_accepting_jobs = 0x0506
    busy = 0x0507
    job_canceled = 0x0508
    multiple_document_jobs_not_supported = 0x0509
    

class OperationEnum(IntEnum):
    # https://tools.ietf.org/html/rfc2911#section-4.4.15
    print_job = 0x0002
    validate_job = 0x0004
    cancel_job = 0x0008
    get_job_attributes = 0x0009
    get_jobs = 0x000a
    get_printer_attributes = 0x000b

    # 0x4000 - 0xFFFF is for extensions
    # CUPS extensions listed here:
    # https://web.archive.org/web/20061024184939/http://uw714doc.sco.com/en/cups/ipp.html
    cups_get_default = 0x4001
    cups_list_all_printers = 0x4002


class JobStateEnum(IntEnum):
    # https://tools.ietf.org/html/rfc2911#section-4.3.7
    pending = 3
    pending_held = 4
    processing = 5
    processing_stopped = 6
    canceled = 7
    aborted = 8
    completed = 9
