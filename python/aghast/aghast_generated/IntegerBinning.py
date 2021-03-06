# automatically generated by the FlatBuffers compiler, do not modify

# namespace: aghast_generated

import flatbuffers


class IntegerBinning(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAsIntegerBinning(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = IntegerBinning()
        x.Init(buf, n + offset)
        return x

    # IntegerBinning
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # IntegerBinning
    def Min(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # IntegerBinning
    def Max(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # IntegerBinning
    def LocUnderflow(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # IntegerBinning
    def LocOverflow(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0


def IntegerBinningStart(builder):
    builder.StartObject(4)


def IntegerBinningAddMin(builder, min):
    builder.PrependInt64Slot(0, min, 0)


def IntegerBinningAddMax(builder, max):
    builder.PrependInt64Slot(1, max, 0)


def IntegerBinningAddLocUnderflow(builder, locUnderflow):
    builder.PrependInt8Slot(2, locUnderflow, 0)


def IntegerBinningAddLocOverflow(builder, locOverflow):
    builder.PrependInt8Slot(3, locOverflow, 0)


def IntegerBinningEnd(builder):
    return builder.EndObject()
