from scrapy.conf import settings
from scrapy.contrib.exporter import CsvItemExporter


class OrderCsvItemExporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
        fields_to_export = settings.get('FIELDS_TO_EXPORT', [])
        if fields_to_export:
            kwargs['fields_to_export'] = fields_to_export
        super(OrderCsvItemExporter, self).__init__(*args, **kwargs)