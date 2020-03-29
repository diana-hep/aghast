# automatically generated by the FlatBuffers compiler, do not modify

# namespace: aghast_generated

import flatbuffers


class SparseRegularBinning(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAsSparseRegularBinning(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SparseRegularBinning()
        x.Init(buf, n + offset)
        return x

    # SparseRegularBinning
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SparseRegularBinning
    def Bins(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Int64Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8),
            )
        return 0

    # SparseRegularBinning
    def BinsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # SparseRegularBinning
    def BinsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SparseRegularBinning
    def BinWidth(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(
                flatbuffers.number_types.Float64Flags, o + self._tab.Pos
            )
        return 0.0

    # SparseRegularBinning
    def Origin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(
                flatbuffers.number_types.Float64Flags, o + self._tab.Pos
            )
        return 0.0

    # SparseRegularBinning
    def Overflow(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = o + self._tab.Pos
            from .RealOverflow import RealOverflow

            obj = RealOverflow()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SparseRegularBinning
    def LowInclusive(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(
                self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
            )
        return True

    # SparseRegularBinning
    def HighInclusive(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(
                self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
            )
        return False

    # SparseRegularBinning
    def Minbin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return -9223372036854775808

    # SparseRegularBinning
    def Maxbin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 9223372036854775807


def SparseRegularBinningStart(builder):
    builder.StartObject(8)


def SparseRegularBinningAddBins(builder, bins):
    builder.PrependUOffsetTRelativeSlot(
        0, flatbuffers.number_types.UOffsetTFlags.py_type(bins), 0
    )


def SparseRegularBinningStartBinsVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)


def SparseRegularBinningAddBinWidth(builder, binWidth):
    builder.PrependFloat64Slot(1, binWidth, 0.0)


def SparseRegularBinningAddOrigin(builder, origin):
    builder.PrependFloat64Slot(2, origin, 0.0)


def SparseRegularBinningAddOverflow(builder, overflow):
    builder.PrependStructSlot(
        3, flatbuffers.number_types.UOffsetTFlags.py_type(overflow), 0
    )


def SparseRegularBinningAddLowInclusive(builder, lowInclusive):
    builder.PrependBoolSlot(4, lowInclusive, 1)


def SparseRegularBinningAddHighInclusive(builder, highInclusive):
    builder.PrependBoolSlot(5, highInclusive, 0)


def SparseRegularBinningAddMinbin(builder, minbin):
    builder.PrependInt64Slot(6, minbin, -9223372036854775808)


def SparseRegularBinningAddMaxbin(builder, maxbin):
    builder.PrependInt64Slot(7, maxbin, 9223372036854775807)


def SparseRegularBinningEnd(builder):
    return builder.EndObject()
