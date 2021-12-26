from swing_trader.node_class import Node


class SwingTrader:
    def __init__(self, series):
        self.nodes = []
        self.length = len(series)
        self.processHighLows(series)

    def al_sat_mod_hesapla(self):
        son_low = self.lowNodes[0]
        bionceki_low = self.lowNodes[1]
        son_high = self.highNodes[0]
        bionceki_high = self.highNodes[1]

        self.mod = None
        self.neden = None

        if son_low > bionceki_low and son_high > bionceki_high:
            self.mod = 'al'
        else:
            self.mod = 'sat'

        return self.mod

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
            # highCopy = copy.deepcopy(node)
            # lowCopy = copy.deepcopy(node)

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