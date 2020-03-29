# automatically generated by the FlatBuffers compiler, do not modify

# namespace: aghast_generated

import flatbuffers


class Ntuple(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAsNtuple(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Ntuple()
        x.Init(buf, n + offset)
        return x

    # Ntuple
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Ntuple
    def Columns(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Column import Column

            obj = Column()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Ntuple
    def ColumnsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Ntuple
    def Instances(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .NtupleInstance import NtupleInstance

            obj = NtupleInstance()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Ntuple
    def InstancesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Ntuple
    def ColumnStatistics(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Statistics import Statistics

            obj = Statistics()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Ntuple
    def ColumnStatisticsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Ntuple
    def ColumnCovariances(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Covariance import Covariance

            obj = Covariance()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Ntuple
    def ColumnCovariancesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Ntuple
    def FunctionsLookup(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4)
            )
        return ""

    # Ntuple
    def FunctionsLookupLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Ntuple
    def Functions(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .FunctionObject import FunctionObject

            obj = FunctionObject()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Ntuple
    def FunctionsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0


def NtupleStart(builder):
    builder.StartObject(6)


def NtupleAddColumns(builder, columns):
    builder.PrependUOffsetTRelativeSlot(
        0, flatbuffers.number_types.UOffsetTFlags.py_type(columns), 0
    )


def NtupleStartColumnsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def NtupleAddInstances(builder, instances):
    builder.PrependUOffsetTRelativeSlot(
        1, flatbuffers.number_types.UOffsetTFlags.py_type(instances), 0
    )


def NtupleStartInstancesVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def NtupleAddColumnStatistics(builder, columnStatistics):
    builder.PrependUOffsetTRelativeSlot(
        2, flatbuffers.number_types.UOffsetTFlags.py_type(columnStatistics), 0
    )


def NtupleStartColumnStatisticsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def NtupleAddColumnCovariances(builder, columnCovariances):
    builder.PrependUOffsetTRelativeSlot(
        3, flatbuffers.number_types.UOffsetTFlags.py_type(columnCovariances), 0
    )


def NtupleStartColumnCovariancesVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def NtupleAddFunctionsLookup(builder, functionsLookup):
    builder.PrependUOffsetTRelativeSlot(
        4, flatbuffers.number_types.UOffsetTFlags.py_type(functionsLookup), 0
    )


def NtupleStartFunctionsLookupVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def NtupleAddFunctions(builder, functions):
    builder.PrependUOffsetTRelativeSlot(
        5, flatbuffers.number_types.UOffsetTFlags.py_type(functions), 0
    )


def NtupleStartFunctionsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def NtupleEnd(builder):
    return builder.EndObject()
