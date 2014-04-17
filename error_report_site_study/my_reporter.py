# coding: utf-8

from  django.views.debug import SafeExceptionReporterFilter

# 自製 Error Reporter 的訊息過律規則, 例如說把 Error Message 內的一些帳號密碼訊息改成 **** 不要給收信者看。
class handler(SafeExceptionReporterFilter):
    def get_traceback_frame_variables(self, request, tb_frame):
        return super(handler, self).get_traceback_frame_variables(request, tb_frame)
