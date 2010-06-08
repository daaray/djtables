#!/usr/bin/env python
# vim: et ts=4 sw=4


from django import template
register = template.Library()

from ..column import BoundColumn


@register.inclusion_tag("djangotables/cols.html")
def table_cols(table):
    return {
        "columns": [
            BoundColumn(table, column)
            for column in table.columns ] }


@register.inclusion_tag("djangotables/head.html")
def table_head(table):
    return {
        "columns": [
            BoundColumn(table, column)
            for column in table.columns ] }


@register.inclusion_tag("djangotables/body.html")
def table_body(table):
    return {
        "rows": table.rows,
        "num_columns": len(table.columns) }


@register.inclusion_tag("djangotables/foot.html")
def table_foot(table):
    return {
        "pages": [
            PageStub(table, number)
            for number in table.paginator.page_range ],
        "num_columns": len(table.columns) }


class PageStub(object):
    def __init__(self, table, number):
        self.table = table
        self.number = number

    @property
    def is_active(self):
        return self.table._meta.page == self.number

    def url(self):
        return self.table.get_url(page=self.number)