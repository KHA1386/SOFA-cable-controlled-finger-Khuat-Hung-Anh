#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import Sofa.Core


class FingerControllerTime(Sofa.Core.Controller):
    """
    Controller điều khiển độ co dây cáp tự động theo thời gian mô phỏng.
    Sử dụng hàm Sin để tạo chuyển động co/duỗi mượt mà.
    """
    def __init__(self, *a, **kw):
        Sofa.Core.Controller.__init__(self, *a, **kw)
        self.listening = True  # Ép bật nhận sự kiện thời gian
        self.node = kw["node"]
        
        # Cấu hình biên độ kéo cáp tối đa (mm) và tốc độ co duỗi
        self.max_displacement = kw.get("maxDisplacement", 25.0)
        self.speed = kw.get("speed", 5)

    def onAnimateBeginEvent(self, event):
        # Lấy thời gian mô phỏng hiện tại từ root node
        t = self.node.getRoot().time.value

        # Hàm Sin biến thiên từ 0 đến max_displacement
        # math.sin đi từ -1 đến 1 -> (1 + sin) đi từ 0 đến 2
        displacement = (self.max_displacement / 2.0) * (1.0 + math.sin(self.speed * t - math.pi / 2.0))

        # Cập nhật độ kéo cáp vào actuator
        self.node.aCableActuator.value = [displacement]
