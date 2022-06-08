from swing_trader.node_class import Node


class SwingTrader:
    def __init__(self, series):
        self.nodes = []
        self.length = len(series)
        self.processHighLows(series)

    def processHighLows(self, series):
        self.createNodes(series)
        self.markHighLows()

    def createNodes(self, series):
        self.nodes = []
        for i in range(0, self.length):
            node = Node(series.iloc[i], i, self.nodes)
            self.nodes.append(node)

    def markHighLows(self):
        self.highNodes = []
        self.lowNodes = []
        for node in self.nodes:
            node.calculateMinors()
            node._isMajorHigh()
            node._isMajorLow()

            if node.isMajorHigh:
                self.majorHighs.append(node)
            if node.isMajorLow:
                self.majorLows.append(node)
            if node.isHigh:
                self.highNodes.append(node)
            if node.isLow:
                self.lowNodes.append(node)
        self.connectNodes(self.highNodes)
        self.connectNodes(self.lowNodes)

    @staticmethod
    def connectNodes(nodeList):
        _len = len(nodeList)
        for i in range(0, _len):
            prev2nd = nodeList[i + 2] if i < _len - 2 else None
            next2nd = nodeList[i - 2] if i - 2 >= 0 else None
            nodeList[i].prev2nd = prev2nd
            nodeList[i].next2nd = next2nd
            next = nodeList[i - 1] if i - 1 >= 0 else None
            prev = nodeList[i + 1] if i < _len - 1 else None
            nodeList[i].next = next
            nodeList[i].prev = prev

    def markMajors(self, that):
        self.lastMajorHigh = None
        self.lastMajorLow = None
        self.prevMajorHigh = None
        self.prevMajorLow = None
        self.majorHighs = []
        self.majorLows = []
        for i in range(0, len(self.highNodes)):
        # while i >= 0:
            node = self.highNodes[i]
            node.calculateMajors("high", that)
            if node.isMajorHigh:
                self.majorHighs.append(node)

        for k in range(0, len(self.lowNodes)):
        # while k >= 0:
            node = self.lowNodes[k]
            node.calculateMajors("low", that)
            if node.isMajorLow:
                self.majorLows.append(node)
