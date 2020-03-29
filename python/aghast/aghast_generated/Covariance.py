# automatically generated by the FlatBuffers compiler, do not modify

# namespace: aghast_generated

import flatbuffers


class Covariance(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAsCovariance(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Covariance()
        x.Init(buf, n + offset)
        return x

    # Covariance
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Covariance
    def Xindex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Covariance
    def Yindex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Covariance
    def SumwxyType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Covariance
    def Sumwxy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            from flatbuffers.table import Table

            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # Covariance
    def Weightpower(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # Covariance
    def Filter(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            x = o + self._tab.Pos
            from .StatisticFilter import StatisticFilter

            obj = StatisticFilter()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None


def CovarianceStart(builder):
    builder.StartObject(6)


def CovarianceAddXindex(builder, xindex):
    builder.PrependInt32Slot(0, xindex, 0)


def CovarianceAddYindex(builder, yindex):
    builder.PrependInt32Slot(1, yindex, 0)


def CovarianceAddSumwxyType(builder, sumwxyType):
    builder.PrependUint8Slot(2, sumwxyType, 0)


def CovarianceAddSumwxy(builder, sumwxy):
    builder.PrependUOffsetTRelativeSlot(
        3, flatbuffers.number_types.UOffsetTFlags.py_type(sumwxy), 0
    )


def CovarianceAddWeightpower(builder, weightpower):
    builder.PrependInt8Slot(4, weightpower, 0)


def CovarianceAddFilter(builder, filter):
    builder.PrependStructSlot(
        5, flatbuffers.number_types.UOffsetTFlags.py_type(filter), 0
    )


def CovarianceEnd(builder):
    return builder.EndObject()
