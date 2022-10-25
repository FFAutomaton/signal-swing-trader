class SimpleNode:
    def __init__(self, candle, i):
        self.index = i
        self.open_ts_int = candle.get("open_ts_int")
        self.open_ts_str = candle.get("open_ts_str")
        self.open = candle.get("open")
        self.high = candle.get("high")
        self.low = candle.get("low")
        self.close = candle.get("close")


class Node(SimpleNode):
    def __init__(self, element, index, nodes):
        super().__init__(element, index)
        self.isHigh = False
        self.isLow = False
        self.next = None
        self.next2nd = None
        self.prev = None
        self.prev2nd = None
        self.connect(nodes)

    def connect(self, nodes):
        if len(nodes) >= 1:
            next = nodes[self.index - 1]
            self.next = next
            next.prev = self

        if len(nodes) >= 2:
            next2nd = nodes[self.index - 2]
            self.next2nd = next2nd
            next2nd.prev2nd = self

    def calculateMinors(self):
        self.isGreen = self._isGreen()
        self.isRed = self._isRed()
        self.isHigh = self._isHigh()
        self.isLow = self._isLow()

    def _isGreen(self):
        if self.close > self.open:
            return True
        return False

    def _isRed(self):
        if self.open > self.close:
            return True
        return False

    def _isHigh(self):
        resistance = False

        if not self.prev or not self.prev2nd or not self.next or not self.next2nd:
            return resistance

        if self.next and self.next2nd:
            self_high = self.close if self._isGreen() else self.open
            prev_high = self.prev.close if self.prev._isGreen() else self.prev.open
            prev_2nd_high = self.prev2nd.close if self.prev2nd._isGreen() else self.prev2nd.open
            next_high = self.next.close if self.next._isGreen() else self.next.close
            next_2nd_high = self.next2nd.close if self.next2nd._isGreen() else self.next2nd.close

            resistance = self_high >= prev_high and self_high >= next_high \
                and self_high >= next_2nd_high and self_high >= prev_2nd_high

        return resistance

    def _isLow(self):
        support = False
        if not self.prev or not self.prev2nd or not self.next or not self.next2nd:
            return support

        if self.next and self.next2nd:
            self_low = self.close if self._isRed() else self.open
            prev_low = self.prev.close if self.prev._isRed() else self.prev.open
            prev_2nd_low = self.prev2nd.close if self.prev2nd._isRed() else self.prev2nd.open
            next_low = self.next.close if self.next._isRed() else self.next.close
            next_2nd_low = self.next2nd.close if self.next2nd._isRed() else self.next2nd.close

            support = self_low <= prev_low and self_low <= next_low \
            and self_low <= next_2nd_low and self_low <= prev_2nd_low

        return support

    def _isMajorHigh(self):
        resistance = False
        if not self.prev or not self.prev2nd or not self.next or not self.next2nd:
            return resistance

        if self.next and self.next2nd:
            resistance = self.high >= self.prev.high and self.high >= self.next.high \
                         and self.high >= self.next2nd.high and self.high >= self.prev2nd.high

        elif self.next and not self.next2nd:
            resistance = self.high >= self.prev.high and self.high >= self.next.high \
                         and self.high >= self.prev2nd.high
        elif not self.next and not self.next2nd:
            resistance = self.high >= self.prev.high and self.high >= self.prev2nd.high

        return resistance

    def _isMajorLow(self):
        support = False
        if not self.prev or not self.prev2nd or not self.next or not self.next2nd:
            return support

        if self.next and self.next2nd:
            support = self.low <= self.prev.low and self.low <= self.next.low \
                      and self.low <= self.next2nd.low and self.low <= self.prev2nd.low
        elif self.next and not self.next2nd:
            support = self.low <= self.prev.low and self.low <= self.next.low \
                      and self.low <= self.prev2nd.low
        elif not self.next and not self.next2nd:
            support = self.low <= self.prev.low and self.low <= self.prev2nd.low

        return support
